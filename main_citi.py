from opencage.geocoder import OpenCageGeocode
from tkinter import*


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


def show_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city,key)
    label.config(text=f"Координаты города {city}: {coordinates}")


key = '1ebc372879da43cd85408246fedd9ed1'


window=Tk()
window.title("Координаты городов")
window.geometry("200x100")

entry=Entry()
entry.pack()

button = Button (text"Поиск координат", command=show.coordinates)
button.pack()

label = Label(text="Введите город и нажмите нп кнопку")
label.pack()

window.mainloop()

