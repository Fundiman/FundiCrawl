# **FundiCrawl**

**FundiCrawl** is a Python-based web crawler designed to scrape data from multiple URLs and save the collected information into well-organized text files. It fetches details such as the page title, meta description, links, headings, paragraphs, images, scripts, styles, tables, and raw HTML. Each URL is saved in its own file with the domain and the date as part of the filename, ensuring no data is mixed.

## **Features**

- **User Agent**: Customizable user agent (`Mozilla/5.0`).
- **Data Collected**: 
  - Title
  - Meta description
  - Links
  - Headings (H1-H6)
  - Paragraphs
  - Tables
  - Images
  - Scripts
  - Styles
  - Raw HTML
- **Output**: Saves data in separate `.txt` files named `<domain>-<date>-<full-url-path>.txt`.

## **Requirements**

- Python 3.12.9
- requests==2.31.0
- beautifulsoup4==4.12.3

## **Installation & Usage**

To install and run **FundiCrawl**, follow these steps:

1. Clone the repository or download the script.
    ```bash
    git clone https://github.com/Fundiman/FundiCrawl.git
    ```

2. Navigate to the directory containing the script:
    ```bash
    cd FundiCrawl
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script. When prompted, input the URLs you want to scrape, separated by commas.

    Example:
    ```bash
    python main.py
    ```

    Prompt:
    ```
    Enter the URLs to scrape (separated by commas): https://example.com, https://anotherexample.com
    ```

5. After scraping, the script will create separate `.txt` files for each URL you provided. The filename format will be:

    ```
    <domain>-<date>-<full-url-path>.txt
    ```

    For example, if you scrape `https://example.com`, the file would be named:
    ```
    example.com-2025-03-30-example-com.txt
    ```
    Also there's examples of data scrapped using this tool in DEMO/

6. The scraped data will include:
    - Title
    - Meta Description
    - Links (all hyperlinks on the page)
    - Headings (H1-H6)
    - Paragraphs
    - Tables (with rows and columns)
    - Images (links to images)
    - Scripts (all JavaScript code)
    - Styles (CSS)
    - Raw HTML of the page

## **Contributing**

Feel free to fork the repository, open issues, or create pull requests to enhance the crawler.

### **To Contribute:**
1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## **License**

This project is open-source and available under the MIT License.