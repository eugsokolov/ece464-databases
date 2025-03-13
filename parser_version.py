import requests
from bs4 import BeautifulSoup
import csv

def main():
    try:
        # Create CSV file to store book data
        with open('books_parser.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'Price', 'Availability', 'Rating', 'Category', 'Page']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            page = 1
            total_books = 0
            has_next_page = True
            
            while has_next_page and page <= 5:  # Limit to 5 pages for demonstration
                # Navigate to the current page
                url = f'https://books.toscrape.com/catalogue/page-{page}.html' if page > 1 else 'https://books.toscrape.com/'
                response = requests.get(url)
                
                # Check if the request was successful
                if response.status_code == 200:
                    print(f"\nScraping page {page}...")
                    
                    # Parse the HTML content
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Find all book containers
                    book_containers = soup.select('article.product_pod')
                    print(f"Found {len(book_containers)} books on page {page}")
                    
                    # Get category from sidebar
                    try:
                        category = soup.select_one('.side_categories ul li ul li.active a').text.strip()
                    except AttributeError:
                        category = "Unknown"
                    
                    # Extract data from each book
                    for book in book_containers:
                        title = book.select_one('h3 a').get('title')
                        price = book.select_one('.price_color').text
                        availability = book.select_one('.availability').text.strip()
                        
                        # Get rating (stars)
                        rating_element = book.select_one('p.star-rating')
                        rating_classes = rating_element['class']
                        rating = [cls for cls in rating_classes if cls != 'star-rating'][0]
                        
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
                    next_button = soup.select_one('li.next a')
                    if next_button:
                        page += 1
                    else:
                        has_next_page = False
                        print("No more pages available.")
                else:
                    print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
                    has_next_page = False
            
            print(f"\nScraping completed. Total books scraped: {total_books}")
            print(f"Data saved to books_parser.csv")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 