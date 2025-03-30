#!/usr/bin/bash
import requests
from bs4 import BeautifulSoup
import datetime

class FundiCrawl:
    def __init__(self, user_agent):
        self.headers = {'User-Agent': user_agent}

    def fetch_url(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return None

    def parse_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data = {
            'title': soup.title.string if soup.title else "No Title",
            'meta_description': self.get_meta_description(soup),
            'links': self.get_links(soup),
            'headings': self.get_headings(soup),
            'paragraphs': self.get_paragraphs(soup),
            'tables': self.get_tables(soup),
            'images': self.get_images(soup),
            'scripts': self.get_scripts(soup),
            'styles': self.get_styles(soup),
            'raw_html': html
        }
        return data

    def get_meta_description(self, soup):
        meta_desc = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
        return meta_desc['content'] if meta_desc else "No description available"

    def get_links(self, soup):
        return [link['href'] for link in soup.find_all('a', href=True)]

    def get_headings(self, soup):
        headings = {}
        for level in range(1, 7):
            headings[f'h{level}'] = [heading.get_text() for heading in soup.find_all(f'h{level}')]
        return headings

    def get_paragraphs(self, soup):
        return [para.get_text() for para in soup.find_all('p')]

    def get_tables(self, soup):
        tables = []
        for table in soup.find_all('table'):
            table_data = []
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all(['td', 'th'])
                cols = [col.get_text() for col in cols]
                table_data.append(cols)
            tables.append(table_data)
        return tables

    def get_images(self, soup):
        return [img['src'] for img in soup.find_all('img', src=True)]

    def get_scripts(self, soup):
        return [script.get_text() for script in soup.find_all('script')]

    def get_styles(self, soup):
        return [style.get_text() for style in soup.find_all('style')]

    def scrape(self, urls):
        results = {}
        for url in urls:
            html = self.fetch_url(url)
            if html:
                data = self.parse_html(html)
                results[url] = data
        return results

    def save_data_to_file(self, url, data):
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        domain = url.split('//')[-1].split('/')[0]
        filename = f"{domain}-{today_date}-{url.split('//')[-1].replace('/', '-')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"\nData for {url}:\n")
            f.write(f"Title: {data['title']}\n")
            f.write(f"Meta Description: {data['meta_description']}\n")
            f.write(f"Links:\n")
            f.write("\n".join(data['links']) + "\n")
            f.write(f"Headings:\n")
            for level, headings in data['headings'].items():
                f.write(f"{level}: {', '.join(headings)}\n")
            f.write(f"Paragraphs:\n")
            f.write("\n".join(data['paragraphs']) + "\n")
            f.write(f"Tables:\n")
            for table in data['tables']:
                for row in table:
                    f.write("\t" + "\t".join(row) + "\n")
            f.write(f"Images:\n")
            f.write("\n".join(data['images']) + "\n")
            f.write(f"Scripts:\n")
            f.write("\n".join(data['scripts']) + "\n")
            f.write(f"Styles:\n")
            f.write("\n".join(data['styles']) + "\n")
            f.write(f"Raw HTML:\n")
            f.write(data['raw_html'] + "\n")
        print(f"Data saved to {filename}")

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 (FundiCrawl/1.0 +https://www.github.com/Fundiman/FundiCrawl)'

crawler = FundiCrawl(user_agent)

urls_input = input("Enter the URLs to scrape (separated by commas): ")
urls_to_scrape = [url.strip() for url in urls_input.split(',')]

scraped_data = crawler.scrape(urls_to_scrape)

for url, data in scraped_data.items():
    crawler.save_data_to_file(url, data)
