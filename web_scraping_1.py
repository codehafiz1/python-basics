import requests
from bs4 import BeautifulSoup
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("📚 Multi Page Book Scraper!")
print("="*40)

all_books = []
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

page = 1

while True:
    print(f"📄 Scraping page {page}...")
    
    # Build URL for each page
    if page == 1:
        url = "http://books.toscrape.com"
    else:
        url = base_url.format(page)
    
    response = requests.get(url)
    
    # Stop if page doesn't exist
    if response.status_code != 200:
        print("✅ No more pages!")
        break
        
    soup = BeautifulSoup(response.text, 'lxml')
    books = soup.find_all('article', class_='product_pod')
    
    # Stop if no books found
    if not books:
        print("✅ All pages scraped!")
        break
    
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text.strip()
        stock = book.find('p', class_='instock availability').text.strip()
        
        all_books.append({
            'title': title,
            'price': price,
            'stock': stock
        })
    
    page += 1

print(f"\n📚 Total books found: {len(all_books)}")
print("="*40)

# Save to file
os.makedirs("scraped_data", exist_ok=True)
with open("scraped_data/all_books.txt", 'w', encoding='utf-8') as f:
    f.write(f"📚 ALL BOOKS - Total: {len(all_books)}\n")
    f.write("="*40 + "\n")
    for book in all_books:
        f.write(f"📚 {book['title']}\n")
        f.write(f"💰 {book['price']}\n")
        f.write(f"📦 {book['stock']}\n")
        f.write("-"*40 + "\n")

print("✅ Saved to scraped_data/all_books.txt!")
print("🎉 Scraping Complete!")