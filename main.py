# Headers
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


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
