import requests
import os

def check_website(address):
    # Make sure the address starts with http:// or https://
    if not address.startswith(('http://', 'https://')):
        address = 'http://' + address

    try:
        response = requests.get(address, timeout=5)
        if response.status_code == 200:
            return "up"
        else:
            return "down"
    except requests.RequestException:
        return "down"

def main():
    try:
        # Get a list of all files in the current directory
        current_directory = os.getcwd()
        folder_directory = current_directory + "\\sites_files"
        
        with open(f"{folder_directory}\\addresses.txt", 'r') as file:
            addresses = file.readlines()

        for address in addresses:
            address = address.strip()
            if address:  # skip empty lines
                status = check_website(address)
                print(f"{address} {status}")
    except FileNotFoundError:
        print("The file 'addresses.txt' was not found.")

if __name__ == "__main__":
    main()
