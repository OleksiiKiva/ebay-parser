# Headers
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# CSS selectors
PRODUCT_NAME = ".x-item-title__mainTitle > span"
PRODUCT_LINK = "link[href*='https://www.ebay.com/itm/']"
PRODUCT_PHOTO_URL = "link[href*='https://i.ebayimg.com/images/']"
SELLER_NAME = ".x-sellercard-atf__info__about-seller"
PRODUCT_PRICE_IN_USD = ".x-price-primary > span"
PRODUCT_PRICE_APPROXIMATELY = (
    ".x-price-approx > [class='x-price-approx__price']"
)
SHIPPING_PRICE_IN_USD = ".ux-labels-values__values-content > div > [class='ux-textspans ux-textspans--BOLD']"
SHIPPING_PRICE_APPROXIMATELY = ".ux-labels-values__values-content > div > [class='ux-textspans ux-textspans--SECONDARY ux-textspans--BOLD']"


class Product:
    """A class that interacts with product page on the Ebay website"""

    ITM_ID = "itm"

    @classmethod
    def validate_product_name(cls, arg):
        return cls.ITM_ID == arg

    def __init__(self):
        self.product_link = input(
            "Input the Ebay product URL in format in the format https://www.ebay.com/itm/{ITM_AD} >> "
        )
        self.product_name = None
        self.product_photo_url = None
        self.seller_name = None
        self.product_price = None
        self.shipping_price = None

    def __get_data(self):
        """A method that receives data from HTML and converts it to beautifulsoup object"""

        itm = self.validate_product_name(self.product_link.split("/")[3])

        try:
            if not itm:
                print(
                    "The web-address was not entered or was entered incorrectly. "
                    "Try again in the format https://www.ebay.com/itm/{ITM_AD}"
                )
            else:
                page = requests.get(
                    url=self.product_link,
                    headers=HEADERS,
                ).content
                soup = BeautifulSoup(page, "lxml")
                return soup

        except requests.ConnectionError:
            print("Connection error")

        except requests.Timeout:
            print("Timeout error")

        except requests.RequestException:
            print("Request error")

    def __parse_data(self) -> dict:
        """A method that receives data in json format and converts it into a nested list"""

        if self.__get_data():
            soup = self.__get_data()

            self.product_name = soup.select_one(selector=PRODUCT_NAME).text

            self.product_link = soup.select_one(selector=PRODUCT_LINK).get(
                "href"
            )

            self.product_photo_url = soup.select_one(
                selector=PRODUCT_PHOTO_URL
            ).get("href")

            self.seller_name = soup.select_one(selector=SELLER_NAME)["title"]

            if (
                    soup.select_one(selector=PRODUCT_PRICE_IN_USD).text.split()[0]
                    != "US"
            ):
                self.product_price = float(
                    soup.select_one(
                        selector=PRODUCT_PRICE_APPROXIMATELY
                    ).text.replace("US $", "")
                )
            elif (
                    soup.select_one(selector=PRODUCT_PRICE_IN_USD).text.split()[0]
                    == "US"
            ):
                self.product_price = float(
                    soup.select_one(selector=PRODUCT_PRICE_IN_USD)
                    .text.replace("US $", "")
                    .replace("/ea", "")
                )
            else:
                self.product_price = soup.select_one(
                    selector=PRODUCT_PRICE_IN_USD
                ).text

            if soup.select_one(selector=SHIPPING_PRICE_IN_USD).text.split()[
                0
            ] == "Free" or not soup.select_one(
                selector=SHIPPING_PRICE_APPROXIMATELY
            ):
                self.shipping_price = 0
            elif (
                    soup.select_one(selector=SHIPPING_PRICE_IN_USD).text.split()[0]
                    == "US"
            ):
                self.shipping_price = float(
                    soup.select_one(
                        selector=SHIPPING_PRICE_IN_USD
                    ).text.replace("US $", "")
                )
            elif (
                    soup.select_one(
                        selector=SHIPPING_PRICE_APPROXIMATELY
                    ).text.split()[0]
                    == "(approx"
            ):
                self.shipping_price = float(
                    soup.select_one(selector=SHIPPING_PRICE_APPROXIMATELY)
                    .text.split()[2]
                    .replace("$", "")
                    .replace(")", "")
                )

            result_dict = {
                "PRODUCT NAME": self.product_name,
                "PRODUCT LINK": self.product_link,
                "PRODUCT PHOTO URL": self.product_photo_url,
                "SELLER NAME": self.seller_name,
                "PRODUCT PRICE": self.product_price,
                "SHIPPING PRICE": self.shipping_price,
            }

            return result_dict
