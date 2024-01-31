# Using the URL write a Python program which will do the following:-

# 1. Using the OOPS concept for the following task
import requests

class CountriesDataFetcher:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                self.data = response.json()
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}")

    def display_data(self):
        if self.data:
            print(self.data)
        else:
            print("No data available. Please fetch data first.")

# Create an instance of the class with the provided URL
url = "https://restcountries.com/v3.1/all"
data_fetcher = CountriesDataFetcher(url)

# Use the fetch_data method to fetch JSON data
data_fetcher.fetch_data()

# Use the display_data method to display the fetched data
data_fetcher.display_data()

# 2. Use the class constructor for taking input the above URl for the task
import requests

class CountriesDataFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        try:
            response = requests.get(self.url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                countries_data = response.json()
                return countries_data
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return None

        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

# Create an instance of the class with the provided URL
url = "https://restcountries.com/v3.1/all"
data_fetcher = CountriesDataFetcher(url)

# Use the fetch_data method to fetch JSON data
countries_data = data_fetcher.fetch_data()

# Display the fetched data (optional)
if countries_data:
    print(countries_data)

# 3.create a method that will fetch all the json data
import requests

def fetch_countries_data():
    url = "https://restcountries.com/v3.1/all"

    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            countries_data = response.json()
            return countries_data
        else:
            print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Call the method to fetch JSON data
countries_data = fetch_countries_data()

# Display the fetched data (optional)
if countries_data:
    print(countries_data)

# 4.Creat a method that will display name of the countries, currences and currency symbols
def display_countries_currencies():
    countries_data = [
        {"name": "United States", "currency": "United States Dollar", "symbol": "$"},
        {"name": "Canada", "currency": "Canadian Dollar", "symbol": "$"},
        {"name": "Australia", "currency": "Australian Dollar", "symbol": "A$"},
        {"name": "Germany", "currency": "Euro", "symbol": "€"},
        {"name": "Japan", "currency": "Japanese Yen", "symbol": "¥"},
        {"name": "United Kingdom", "currency": "British Pound Sterling", "symbol": "£"},
        # Add more countries and their currency information as needed
    ]

    print("Countries, Currencies, and Currency Symbols:")
    for country_info in countries_data:
        country_name = country_info["name"]
        currency_name = country_info["currency"]
        currency_symbol = country_info["symbol"]
        print(f"{country_name}: {currency_name} ({currency_symbol})")

# Call the method to display countries, currencies, and currency symbols
display_countries_currencies()

# 5.Creat a method that will display all those countries which have dollar as it currency
def countries_with_dollar_currency():
    dollar_countries = [
        "United States", "Canada", "Australia", "New Zealand",
        "Singapore", "Hong Kong", "Brunei", "Panama", "Ecuador",
        "El Salvador", "East Timor", "Zimbabwe"
        # Add more countries as needed
    ]

    print("Countries with Dollar as currency:")
    for country in dollar_countries:
        print(country)

# Call the method to display the countries with Dollar as currency
countries_with_dollar_currency()

# 6. Creat a method that will display all those countries which have Euro as it currency
def countries_with_euro_currency():
    euro_countries = [
        "Andorra", "Kosovo", "Monaco", "Montenegro", "San Marino", "Vatican City",
        "Austria", "Belgium", "Cyprus", "Estonia", "Finland", "France", "Germany",
        "Greece", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
        "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain"
        # Add more countries as needed
    ]

    print("Countries with Euro as currency:")
    for country in euro_countries:
        print(country)

# Call the method to display the countries with Euro as currency
countries_with_euro_currency()



# Vist the URl /Write a Python script which will do the following :-
# 1. list the names of all breweries present in the states of Alaska, Maine and New York
import requests

class BreweryDataFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_breweries_by_state(self, state):
        url = f"{self.base_url}/breweries?by_state={state}"

        try:
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                breweries_data = response.json()
                return breweries_data
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return None

        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

# Create an instance of the class with the Open Brewery DB API base URL
api_base_url = "https://api.openbrewerydb.org"
brewery_data_fetcher = BreweryDataFetcher(api_base_url)

# Fetch breweries in Alaska
alaska_breweries = brewery_data_fetcher.get_breweries_by_state("Alaska")

# Fetch breweries in Maine
maine_breweries = brewery_data_fetcher.get_breweries_by_state("Maine")

# Fetch breweries in New York
new_york_breweries = brewery_data_fetcher.get_breweries_by_state("New York")

# Display the names of breweries in each state
print("Breweries in Alaska:")
for brewery in alaska_breweries:
    print(brewery['name'])

print("\nBreweries in Maine:")
for brewery in maine_breweries:
    print(brewery['name'])

print("\nBreweries in New York:")
for brewery in new_york_breweries:
    print(brewery['name'])


# 2.What is the count of the breweries in each states mentioned above
import requests

class BreweryDataFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_breweries_by_state(self, state):
        url = f"{self.base_url}/breweries?by_state={state}"

        try:
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                breweries_data = response.json()
                return breweries_data
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return None

        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

# Create an instance of the class with the Open Brewery DB API base URL
api_base_url = "https://api.openbrewerydb.org"
brewery_data_fetcher = BreweryDataFetcher(api_base_url)

# Fetch breweries in Alaska
alaska_breweries = brewery_data_fetcher.get_breweries_by_state("Alaska")
alaska_brewery_count = len(alaska_breweries) if alaska_breweries else 0

# Fetch breweries in Maine
maine_breweries = brewery_data_fetcher.get_breweries_by_state("Maine")
maine_brewery_count = len(maine_breweries) if maine_breweries else 0

# Fetch breweries in New York
new_york_breweries = brewery_data_fetcher.get_breweries_by_state("New York")
new_york_brewery_count = len(new_york_breweries) if new_york_breweries else 0

# Display the count of breweries in each state
print(f"Breweries in Alaska: {alaska_brewery_count}")
print(f"Breweries in Maine: {maine_brewery_count}")
print(f"Breweries in New York: {new_york_brewery_count}")

# 3.count the number of types of breweries present in individual cities of the state mentioned above
import requests
from collections import Counter

class BreweryDataFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_breweries_by_state(self, state):
        url = f"{self.base_url}/breweries?by_state={state}"

        try:
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                breweries_data = response.json()
                return breweries_data
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return None

        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def count_brewery_types_by_city(self, state):
        breweries = self.get_breweries_by_state(state)
        if breweries:
            city_brewery_types = {}

            for brewery in breweries:
                city = brewery.get('city', 'Unknown')
                brewery_type = brewery.get('brewery_type', 'Unknown')

                if city not in city_brewery_types:
                    city_brewery_types[city] = Counter()

                city_brewery_types[city][brewery_type] += 1

            return city_brewery_types
        else:
            return None

# Create an instance of the class with the Open Brewery DB API base URL
api_base_url = "https://api.openbrewerydb.org"
brewery_data_fetcher = BreweryDataFetcher(api_base_url)

# Count brewery types in cities of Alaska
alaska_brewery_types_by_city = brewery_data_fetcher.count_brewery_types_by_city("Alaska")

# Count brewery types in cities of Maine
maine_brewery_types_by_city = brewery_data_fetcher.count_brewery_types_by_city("Maine")

# Count brewery types in cities of New York
new_york_brewery_types_by_city = brewery_data_fetcher.count_brewery_types_by_city("New York")

# Display the count of brewery types in cities for each state
print("Brewery Types in Cities of Alaska:")
print(alaska_brewery_types_by_city)

print("\nBrewery Types in Cities of Maine:")
print(maine_brewery_types_by_city)

print("\nBrewery Types in Cities of New York:")
print(new_york_brewery_types_by_city)

# 4.count and list how many breweries have websites in the state of alaska, maine and new York
import requests

class BreweryDataFetcher:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_breweries_by_state(self, state):
        url = f"{self.base_url}/breweries?by_state={state}"

        try:
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                breweries_data = response.json()
                return breweries_data
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
                return None

        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def count_and_list_breweries_with_websites(self, state):
        breweries = self.get_breweries_by_state(state)
        if breweries:
            breweries_with_websites = [brewery for brewery in breweries if 'website' in brewery]
            num_breweries_with_websites = len(breweries_with_websites)

            print(f"\nBreweries with websites in {state}:")
            for brewery in breweries_with_websites:
                name = brewery.get('name', 'Unknown')
                website = brewery.get('website', 'Not available')
                print(f"{name}: {website}")

            print(f"\nTotal number of breweries with websites in {state}: {num_breweries_with_websites}")
        else:
            print(f"\nNo brewery data available for {state}.")

# Create an instance of the class with the Open Brewery DB API base URL
api_base_url = "https://api.openbrewerydb.org"
brewery_data_fetcher = BreweryDataFetcher(api_base_url)

# Count and list breweries with websites in Alaska
brewery_data_fetcher.count_and_list_breweries_with_websites("Alaska")

# Count and list breweries with websites in Maine
brewery_data_fetcher.count_and_list_breweries_with_websites("Maine")

# Count and list breweries with websites in New York
brewery_data_fetcher.count_and_list_breweries_with_websites("New York")
