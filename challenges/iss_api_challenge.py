#!/usr/bin/env python3
""" This code tracks the ISS station at the time the script is run. 
    Keep in mind the ISS moves at about 4.76 miles per second. """

# Import the appropriate modules to execute this script.
from textwrap import dedent
from datetime import datetime
import requests
import reverse_geocoder as rg

def iss_locator():
    """Locates the ISS at the time the script is run"""

    # Pull data from the API website
    iss_location = requests.get("http://api.open-notify.org/iss-now.json", timeout=10).json()

    # Convent epoch time from the API to human readable time.
    current_time = datetime.fromtimestamp(iss_location['timestamp'])

    # Putting LAT/LON into variables
    lat = iss_location['iss_position']['latitude']
    log = iss_location['iss_position']['longitude']

    # Convert LAT/LON into a geographical location on the globe
    coordinates = (lat, log)
    result = rg.search(coordinates, verbose=False)
    city = result[0]['name']
    country = result[0]['cc']


    # Print location of the ISS station
    print(dedent(f"""
        Current Location of the ISS:
        Timestamp: {current_time}
        Lat: {lat}
        Lon: {log}
        City/Country: {city}, {country}\n"""
        ))

if __name__ == "__main__":
    iss_locator()
