from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"


key = '1ebc372879da43cd85408246fedd9ed1'
city = "Moscow"
coordinates = get_coordinates(city,key)
print(f"Координфты города {city}: {coordinates}")