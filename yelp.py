import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("YELP_API_KEY")

# Yelp API Endpoint
YELP_ENDPOINT = 'https://api.yelp.com/v3/'

# Function to fetch data from Yelp API
def get_locations(term, location, categories, sort = 'best_match'):
    search_buisness = 'businesses/search'
    search_events = 'events'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }

    params = {
        'term': term,
        'location': location,
        'categories' : categories,
        'sort_by' : sort,
        'limit'   : '10'
    }
    params_events = {
        'location': location,
    }

    try:
        response = requests.get(YELP_ENDPOINT + search_buisness, headers=headers, params=params)
        response.raise_for_status()  # Check for any request errors
        response_events = requests.get(YELP_ENDPOINT + search_events, headers=headers, params=params_events)
        response_events.raise_for_status()

        print("********events*********")
        print(response_events.json())


        data = response.json()
        results = data['businesses']
        locations = []
        if results:
            for business in results[:5]:
                busines= {}
                busines['Name'] = business['name']
                busines['Rating'] = business['rating']
                busines['Adress'] = business['location']['address1']
                busines ['Link'] = [business['url']]

                info = ""
                info += f"Name: {business['name']}\n"
                print(f"Name: {business['name']}")
                info += f"Rating: {business['rating']}\n"
                print(f"Rating: {business['rating']}")
                info += f"Address: {business['location']['address1']}\n"
                print(f"Address: {business['location']['address1']}")
                info += f"Website: {business['url']}\n"
                print(f"Website: {business['url']}")
                info += "-----------\n\n"
                print("-----------\n\n")
                locations.append(busines)

            return locations
        else:
            print("No results found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Yelp API: {e}")
        return None
    


# Example usage
if __name__ == '__main__':
    search_term = 'restaurants'  # Replace with your desired search term
    location = 'New York'       # Replace with your desired location

    results = fetch_data_from_yelp_api(search_term, location)
    if results:
        for business in results[:5]:
            print(f"Name: {business['name']}")
            print(f"Rating: {business['rating']}")
            print(f"Address: {business['location']['address1']}")
            print(f"Website: {business['url']}")

            print("-----------")
    else:
        print("No results found.")