from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language = 'ru')
        if results:
            lat = round(results[0]['geometry']['lat'],2)
            lon =  round(results[0]['geometry']['lng'],2)
            return f"Широта: {lat}, Долгота: {lon}"
        else:
            return "Город не найден"
    except Exception as a:
        return f"Возникла ошибка: {e}"


key = '1ebc372879da43cd85408246fedd9ed1'
city = "Эквадор"
coordinates = get_coordinates(city,key)
print(f"Координаты города {city}: {coordinates}")