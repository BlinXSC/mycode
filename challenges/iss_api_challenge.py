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

    # Convert LAT/LON into a geographical location on the globe.
    coordinates = (
        iss_location['iss_position']['longitude'],
        iss_location['iss_position']['latitude']
        )
    result = rg.search(coordinates, verbose=False)

    # Print location of the ISS station
    print(dedent(f"""
        Current Location of the ISS:
        Timestamp: {current_time}
        Lon: {iss_location['iss_position']['longitude']}
        Lat: {iss_location['iss_position']['latitude']}
        City/Country: {result[0]['admin1']}, {result[0]['cc']}\n"""
        ))

if __name__ == "__main__":
    iss_locator()
