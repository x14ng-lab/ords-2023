# Week 7 workshop - API requests: Weather forecast

This week, we will use Python to request real-time information from an online service. One way to do this is to use an **API** (application programming interface) -- an interface which allows your program to access data in real time from other sources.

We will use the [Open-Meteo weather forecast API](https://open-meteo.com/en) to build our own weather forecast program.

## Task 1: Making an API request

To make our first API request, we will use a new package called `requests` ([documentation](https://requests.readthedocs.io/en/latest/)), which will handle the communication between your program and the weather API, to make the actual information request to the service. The package comes pre-installed with Anaconda.

The data provided by most APIs is in [JSON format](https://en.wikipedia.org/wiki/JSON), which actually looks a lot like a Python dictionary. An example request result is shown on the [front page](https://open-meteo.com/en) of the weather API -- you should recognise the `{key: value}` structure which characterises JSON and dictionaries.

### Using the URL builder

Browse the [API documentation](https://open-meteo.com/en/docs) for the weather API. You will see that there are many different variables to observe -- temperature, precipitation, wind speed, etc.

- Enter the coordinates for Edinburgh in the "Latitude" and "Longitude" boxes (lat 55.9, long -3.2).
- Then, choose 1 or 2 variables you'd like to display. Note that some of these give a reading every hour ("Hourly"), others give a reading per day ("Daily").
- Click the "Preview" button.

The graph should update on the webpage with your chosen variables, **as well as the URL just below**. Try choosing a different variable, and watch how the URL changes.

All we need to make an API request is this URL.

### Making the request from a Python script

Open `weather.py` in VSCode. The package `requests` should already be imported.

The [Quickstart guide](https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content) in the `requests` documentation gives an example of making a request for JSON data:

```python
import requests

r = requests.get('your-URL-here')
print(r.json())
```

where the `.json()` method of the `Request` object `r` returns a Python dictionary containing your requested data.

Copy and paste the URL from the website to make a request from your Python script.

### Plotting the results

Examine the structure of the dictionary, and try to plot your chosen variable(s) over time.

For example, if you selected variables with hourly readings, you should see them under the `'hourly'` label in the `r.json()` dictionary, as a nested dictionary.


## Task 2: Building a request programmatically

Instead of using the point-and-click browser interface, let's try to build a new request from scratch in Python.

The only thing to do is to build the URL with the parameters we want. On the webpage, the [API documentation](https://open-meteo.com/en/docs) (scroll down after the graph) provides a list of all the parameters you can request.

We could try to build the URL string directly ourselves, by chaining up `&parameter=variable1,variable2` for all the parameters and values we want. However, `requests.get()` provides [a `params` optional argument](https://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls) to pass these parameters as a dictionary. For example, to obtain the daily minimal and maximal temperatures in Edinburgh over the next 7 days (note that omitting the [time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) seems to return an error):

```python
# Create a dictionary for the parameters I need
params_dict = {'timezone': 'Europe/London',
               'latitude': 55.9,
               'longitude': -3.2,
               'daily': ['temperature_2m_max' ,'temperature_2m_min']}

# Make a request by passing these parameters
r = requests.get('https://api.open-meteo.com/v1/forecast', params=params_dict)
print(r.json())
```

The "base" URL `'https://api.open-meteo.com/v1/forecast'` is sometimes called the "API endpoint".

Build your own request to display a weather forecast with 2 or 3 variables of your choice.


## Task 3: Weather in other cities

`open-meteo.com` also provides a [Geocoding API](https://open-meteo.com/en/docs/geocoding-api), which can be used to obtain (amongst other things) latitude and longitude coordinates for 11 million different cities and towns in the world.

Study the API documentation, and find out how to obtain the latitude and longitude coordinates for **your hometown** using an API request (as in Task 2, not using the web interface!). Then, write a function `weather_forecast(city_name)`, which takes a string as a city/town name, and displays a short weather forecast for this city.

You can choose to plot certain variables like wind speed, temperature, cloud cover, etc. over time (as in Tasks 1 and 2), or you could write a text summary forecast, for instance something like

```
Tomorrow, the weather in [city] will be [sunny/cloudy/rainy/etc..].
The minimum temperature will be [min], and the maximum will be [max].
```


## Bonus tasks (if you have time)

These are a few ideas for what you could do next -- pick one you like and go ahead!

### Cleaning up timestamp data

The times of the readings will be given as strings. To clean up the time axis labels in your plot, two functions will be useful:

- [`parser.parse()`](https://dateutil.readthedocs.io/en/stable/parser.html#dateutil.parser.parse) from the `dateutil` package can automatically convert a string timestamp to a `datetime` object.
- [`Axes.xaxis_date()`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.xaxis_date.html#matplotlib.axes.Axes.xaxis_date) from `matplotlib` can automatically set up your x-axis ticks and labels to work well with `datetime` objects.


### Using weather codes

One of the variables you can request to the weather API is a "weather code". Scroll all the way down [on the documentation page](https://open-meteo.com/en/docs) to see what each code represents, and use this to write a user-friendly forecast.


### Explore other public APIs

[This page](https://github.com/public-apis/public-apis) offers a community-maintained list of many public APIs. Browse through them, pick one you find interesting, and write a program using it. Combine them together -- for instance, why not complement your daily weather forecast with a reminder of public holidays happening on that day, and a picture of a fluffy cat?

**Note** that although all of these are public, some will require you to request an API key for authentication. Usually this is done by giving your email address or creating a user account. The API documentation should give you the necessary instructions on how to request it and how to use it.

Note also that these APIs often limit the number of requests that one person can make over a period of time (usually 1 hour).
