from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import csv

def main():
    # Set up Chrome options
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # Set to False to see the browser
    options.add_argument('--headless=new') if False else None
    
    try:
        # Initialize the Chrome driver
        service = Service()
        driver = webdriver.Chrome(options=options, service=service)
        
        # Create CSV file to store book data
        with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'Price', 'Availability', 'Rating', 'Category', 'Page']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            page = 1
            total_books = 0
            has_next_page = True
            
            while has_next_page and page <= 5:  # Limit to 5 pages for demonstration
                # Navigate to the current page
                url = f'https://books.toscrape.com/catalogue/page-{page}.html' if page > 1 else 'https://books.toscrape.com/'
                driver.get(url)
                print(f"\nScraping page {page}...")
                
                # Find all book containers
                book_containers = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
                print(f"Found {len(book_containers)} books on page {page}")
                
                # Extract data from each book
                for book in book_containers:
                    title = book.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
                    price = book.find_element(By.CSS_SELECTOR, '.price_color').text
                    availability = book.find_element(By.CSS_SELECTOR, '.availability').text.strip()
                    
                    # Get rating (stars)
                    rating_element = book.find_element(By.CSS_SELECTOR, 'p.star-rating')
                    rating_classes = rating_element.get_attribute('class').split()
                    rating = [cls for cls in rating_classes if cls != 'star-rating'][0]
                    
                    # Get category from sidebar
                    try:
                        category = driver.find_element(By.CSS_SELECTOR, '.side_categories ul li ul li.active a').text.strip()
                    except NoSuchElementException:
                        category = "Unknown"
                    
                    # Write to CSV
                    writer.writerow({
                        'Title': title,
                        'Price': price,
                        'Availability': availability,
                        'Rating': rating,
                        'Category': category,
                        'Page': page
                    })
                    
                    total_books += 1
                
                # Check if there's a next page
                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')
                    page += 1
                except NoSuchElementException:
                    has_next_page = False
                    print("No more pages available.")
            
            print(f"\nScraping completed. Total books scraped: {total_books}")
            print(f"Data saved to books.csv")
        
        # Close the browser
        driver.quit()
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()