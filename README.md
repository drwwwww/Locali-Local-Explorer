# Local Explorer 🌍

Local Explorer is a terminal-based Python tool that provides users with **real-time weather**, **local news**, and **upcoming events** for any city they enter. It's a quick way to explore a city before a trip or just stay informed about your hometown.

---

## Features

- **🌦 Weather Updates**: Get current temperature, humidity, and condition descriptions using [WeatherAPI](https://www.weatherapi.com/).
- **📰 Top Headlines**: Fetch the latest local news using [NewsAPI](https://newsapi.org/).
- **🎟 Events Search**: Discover upcoming events via the [Ticketmaster API](https://developer.ticketmaster.com/).
- **🎨 Terminal UI**: Colored output using `colorama` for a more readable and visually engaging CLI experience.

---

## Demo & Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/local-explorer.git
cd local-explorer

# Set up your environment
cp .env.example .env
# Then open .env and add:
# WEATHER_API_KEY=your_weather_api_key
# NEWS_API_KEY=your_news_api_key
# TICKETMASTER_API_KEY=your_ticketmaster_api_key

# Install required Python packages
pip install requests python-dotenv colorama

# Run the program
python local-explorer.py

Welcome to the Local Explorer tool - Type a city you would like to explore to get started.
Type City Here: Chicago

What information would you like to receive about Chicago?
Weather      News       Events       All
Answer Here: All

Thank you, we will now look for All info in Chicago

-----This is the current weather for Chicago-----
The current temperature is 72
And feels like 70
With a humidity of 55
And conditions described as: Sunny

-----This is the news for Chicago-----
- Mayor announces new green initiative -
Chicago mayor introduces ambitious plan for green energy...

...

-----These are events in Chicago-----
- Lollapalooza 2025 -
2025-08-01
...
