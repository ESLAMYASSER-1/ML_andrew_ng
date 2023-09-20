import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim

# Enter phone number with country code
phone_number = "+79102279996"

# Parse phone number
parsed_number = phonenumbers.parse(phone_number)

# Get geographic information
geographic_info = geocoder.description_for_number(parsed_number, "en")
print("Geographic information:", geographic_info)

# Get carrier information
carrier_info = carrier.name_for_number(parsed_number, "en")
print("Carrier information:", carrier_info)

# Get detailed location information
geolocator = Nominatim(user_agent="phone_number_location")
location = geolocator.geocode(geographic_info)
if location is not None:
    print("Detailed location information:")
    print("Address:", location.address)
    print("Latitude:", location.latitude)
    print("Longitude:", location.longitude)
else:
    print("Unable to get detailed location information for the phone number.")
