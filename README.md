<h1 align="center">🛒 eBay Parser 🛒</h1>
<h3 align="center">Service for collecting some data on a product page on eBay</h3>

## 📝 Description

The project is based on a class that collects data from a link to an Ebay product page.
List of returned data:

* the product's name
* link to the product
* link to photo
* seller name
* price
* shipping price

Return data format:

* JSON file
* console output

### ✅ Implemented checks

* Correctness of the entered data
* Connection error
* Timeout error
* The Request error

## 🛢️Technology stack

* Backend: Python 3.12.4, requests 2.32.3, beautifulsoup4 4.12.3, lxml 5.2.2
* Virtual Environment: venv
* Dependency Management: pip
* Collaboration and Version Control: Git, GitHub

## 🔀 Example response

<img alt="preview" src="picture/preview.png" width="800"/>

## 🚀 Install using GitHub

1. Install Python
1. Clone the repo
   ```commandline
   https://github.com/OleksiiKiva/ebay-parser.git   
   ```
1. Open the project folder in your IDE
1. Open the project terminal folder. Create & activate venv
   ```commandline
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on Linux/MacOS)
   ```
1. Install all requirements
   ```commandline
   pip install -r requirements.txt
   ```
1. Run `main.py`
   ```commandline
   python main.py (on Windows)
   python3 main.py (on Linux/MacOS)
   ```

## 📧 Contacts

Please send bug reports and suggestions by email:
[oleksii.kiva@gmail.com](mailto:oleksii.kiva@gmail.com)
