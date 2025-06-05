from colorama import init, Fore, Back, Style
import requests
import json
import os
from dotenv import load_dotenv
import time

init()

load_dotenv()

weather_key = os.getenv("WEATHER_API_KEY")
news_key = os.getenv("NEWS_API_KEY")
ticketmaster_key = os.getenv("TICKETMASTER_API_KEY")

def weather():
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": weather_key,
            "q": city
        }
        response = requests.get(url, params=params)
        data = response.json()

        temp = str(data['current']['temp_f'])
        feels = str(data['current']['feelslike_f'])
        humid = str(data['current']['humidity'])
        cond = data['current']['condition']['text']

        print()
        print(Fore.GREEN + Style.BRIGHT + "-----This is the current weather for " + city  + "-----"  + Style.RESET_ALL)
        print()
        print(Fore.GREEN + Style.BRIGHT + 
            "The current temperature is " + temp  + 
            "\nAnd feels like " + feels +
            "\nWith a humidity of " + humid +
            "\nAnd conditions described as: " + cond 
            + Style.RESET_ALL)
        
    except KeyError as e:
        print()
        print(Fore.RED + Style.BRIGHT + "Could not find weather information for " + '"' + city + '"'  + Style.RESET_ALL)

def news():
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
                "apiKey": news_key,
                "q": city,
                "pageSize": 5
            }
        response = requests.get(url, params=params)
        data = response.json()
        
        title1 = data['articles'][0]['title']
        desc1 = data['articles'][0]['description']

        title2 = data['articles'][1]['title']
        desc2 = data['articles'][1]['description']

        title3 = data['articles'][2]['title']
        desc3 = data['articles'][2]['description']

        print()
        print(Fore.YELLOW + Style.BRIGHT + "-----This is the news for " + city  + "-----"  + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + Style.BRIGHT + "-" + title1 + "-" + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + Style.DIM + desc1 + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + Style.BRIGHT + "-" + title2 + "-" + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + Style.DIM + desc2 + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + Style.BRIGHT + "-" + title3 + "-" + Style.RESET_ALL)
        print()
        print(Fore.YELLOW + Style.DIM + desc3 + Style.RESET_ALL)

    except IndexError as e:
        print()
        print(Fore.RED + Style.BRIGHT + "Could not find news information for " + '"' + city + '"'  + Style.RESET_ALL)


def events():
    try:
        url = "https://app.ticketmaster.com/discovery/v2/events"
        params = {
            "apikey": ticketmaster_key,
            "city": city
        }
        response = requests.get(url, params=params)
        data = response.json()

        ev1 = data['_embedded']['events'][0]['name']
        date1 = data['_embedded']['events'][0]['dates']['start']['localDate']

        ev2 = data['_embedded']['events'][1]['name']
        date2 = data['_embedded']['events'][1]['dates']['start']['localDate']

        ev3 = data['_embedded']['events'][2]['name']
        date3 = data['_embedded']['events'][2]['dates']['start']['localDate']

        ev4 = data['_embedded']['events'][3]['name']
        date4 = data['_embedded']['events'][3]['dates']['start']['localDate']

        ev5 = data['_embedded']['events'][4]['name']
        date5 = data['_embedded']['events'][4]['dates']['start']['localDate']

        print()
        print(Fore.RED + Style.BRIGHT + "-----These are events in " + city  + "-----"  + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.BRIGHT + "-" + ev1 + "-" + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.DIM + date1 + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.BRIGHT + "-" + ev2 + "-" + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.DIM + date2 + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.BRIGHT + "-" + ev3 + "-" + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.DIM + date3 + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.BRIGHT + "-" + ev4 + "-" + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.DIM + date4 + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.BRIGHT + "-" + ev5 + "-" + Style.RESET_ALL)
        print()
        print(Fore.RED + Style.DIM + date5 + Style.RESET_ALL)

    except KeyError as e:
        print(Fore.RED + Style.BRIGHT + "Could not find event information for " + '"' + city + '"'  + Style.RESET_ALL)


def main():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to my Local Explorer tool - Type a city you would like to explore to get started.")
    global city
    city = input(Fore.CYAN + Style.BRIGHT + "Type City Here: " + Style.RESET_ALL)
    
    print(Fore.CYAN + Style.BRIGHT + "\nWhat informaton would you like to receive about " + Fore.RESET + Fore.BLACK + city + "?\n" + Style.RESET_ALL)
    global infoType
    infoType = input(Fore.GREEN + Style.BRIGHT + "Weather" + Fore.RESET + Fore.YELLOW + "      News" + Fore.RESET + Fore.RED + "       Events" + Fore.RESET + Fore.MAGENTA + "       All\n\n" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + "Answer Here: " + Style.RESET_ALL)

    print(Fore.CYAN + Style.BRIGHT + "\nThank you, we will now look for " + Fore.RESET + Fore.BLACK + infoType + Fore.RESET + Fore.CYAN + " info in " + Fore.RESET + Fore.BLACK + city + Style.RESET_ALL)
    time.sleep(1.5)

    if infoType == "Weather" or infoType == "weather":
        weather()
    
    elif infoType == "News" or infoType == "news":
        news()

    elif infoType == "Events" or infoType == "events":
        events()

    elif infoType == "All" or infoType == "all":
        weather()
        news()
        events()
        print()

    else:
        print(Fore.RED + Style.BRIGHT + "\nInvalid Infotype\n"  + Style.RESET_ALL)
        time.sleep(0.5)
        main()

    return city, infoType


main()




