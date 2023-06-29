import os
import requests


# Function to retrieve weather data for a location
def get_weather(api_key, location):
    # Construct the API URL with the provided location and API key
    url = f"https://api.weatherbit.io/v2.0/current?city={location}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response into data
        data = response.json()
        print(f"Weather in {location}:")
        print(f"Temperature: {data['data'][0]['temp']}°C")
        print(f"Description: {data['data'][0]['weather']['description']}")
    else:
        print("Error occurred while retrieving weather data.")


# Read the Weatherbit API key from an environment variable
api_key = os.environ.get("WEATHERBIT_API_KEY")

while True:
    # Prompt the user to enter a location
    location = input("Enter a location: ")
    # Call the get_weather function with the provided API key and location
    get_weather(api_key, location)

    while True:
        # Prompt the user to choose whether to ask for another city
        continue_prompt = input("Would you like to ask for another city? (y/n): ")
        if continue_prompt.lower() == "n":
            break
        elif continue_prompt.lower() == "y":
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    if continue_prompt.lower() == "n":
        break
