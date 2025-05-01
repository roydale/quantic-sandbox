"""
A program that asks the user what city they're starting in and computes the sequence of 
cities to visit that results in all cities being visited once and only once at the lowest 
cost. The output should show the sequence, the cost of each leg, and the total cost.
"""

import os
import requests
from bs4 import BeautifulSoup

# Function to retrieve Wikipedia page content
def get_wikipedia_page(brand_name):
    # Construct the URL for the Wikipedia page
    url = f"https://en.wikipedia.org/wiki/{brand_name}"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to check if a section title contains specific words
def contains_keywords(section_title, keywords):
    section_title = section_title.lower()
    for keyword in keywords:
        if keyword in section_title:
            return True
    return False

# Main function
def main():
    current_directory = os.getcwd()
    folder_directory = f"{current_directory}\\scraper_files"
    coffees_file_path = f"{folder_directory}\\coffees.txt"
    strategies_file_path = f"{folder_directory}\\wiki_scraper_strategies.txt"
    
    # Define the keywords to look for in section titles
    keywords = ["advertising", "marketing"]

    # Create or open the strategies.txt file for writing
    with open(strategies_file_path, "w", encoding="utf-8") as strategies_file:
        # Open the coffees.txt file for reading
        with open(coffees_file_path, "r", encoding="utf-8") as coffees_file:
            # Iterate through each brand name in coffees.txt
            for brand_name in coffees_file:
                brand_name = brand_name.strip()  # Remove leading/trailing whitespace

                # Retrieve the Wikipedia page content
                page_content = get_wikipedia_page(brand_name)

                if page_content:
                    # Parse the HTML content using BeautifulSoup
                    soup = BeautifulSoup(page_content, "html.parser")

                    # Find all section titles (usually enclosed in <span> tags with class "mw-headline")
                    section_titles = soup.find_all("div", class_="mw-heading")

                    # Iterate through section titles and check for keywords
                    for title in section_titles:
                        section_title = title.text
                        if contains_keywords(section_title, keywords):
                            # Find the parent element of the title
                            section = title.find_parent()

                            # Extract all text within the section
                            section_text = section.get_text().strip()

                            # Write the brand name, section title, and section text to strategies.txt
                            strategies_file.write(f"Brand Name: {brand_name}\n")
                            strategies_file.write(f"Section Title: {section_title}\n")
                            strategies_file.write(f"Section Text:\n{section_text}\n\n")

if __name__ == "__main__":
    main()
