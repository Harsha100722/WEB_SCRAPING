# 📰 News Headlines Web Scraper

This Python project scrapes the top news headlines from [The Hindu](https://www.thehindu.com/) website and saves them into a text file.

## 📌 Objective

To automate the collection of:
- The page `<title>`
- All `<h2>` and `<h3>` tag headlines  
from the homepage of *The Hindu* website.

## 🧰 Tools & Libraries Used

- **Python 3.x**
- `requests` – to fetch the web page
- `beautifulsoup4` – to parse and extract HTML content

## 📁 Output

The extracted headlines are saved in a file named:




The file includes:
- The page title
- All `<h2>` tag texts
- All `<h3>` tag texts

## 🚀 How to Run the Script

### 1. Install dependencies (if not already installed)
pip install requests beautifulsoup4

Run the script
python your_script_name.py


✅ Example Output (in news_scraping.txt)
<Title>Tag:

The Hindu: Breaking News, India News, Sports News and Live Updates

<H2>Tags:

India News
World
Business

<H3>Tags:

Top Stories
Editor's Picks
Trending


