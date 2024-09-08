<p align="center">
  <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" alt="Python Logo" width="400"/>
</p>

## ( PLEASE READ INSTRUCTION.docx FOR MORE HELP ! )

# Weather App 🌦️

A simple Weather App built using **Python** and **Tkinter** that fetches and displays the current weather data for a user-specified city using the [OpenWeatherMap API](https://openweathermap.org/).

## 🧩 Features

- Fetches weather data for any city around the world.
- Displays **temperature**, **humidity**, and **weather description**.
- Built using **Tkinter** for GUI and **requests** for API calls.
- Handles city not found and API errors gracefully.

## 🚀 How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/shadowking06/weather-app-tkinter.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd weather-app-tkinter
    ```

3. **Install the required libraries**:
    ```bash
    pip install requests
    ```

4. **Set up OpenWeatherMap API Key**:
    - Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and create an account to get your free API key.
    - Replace the placeholder `api_key` in the script with your own API key.

5. **Run the program**:
    ```bash
    python main.py
    ```

## 📂 Project Structure

```bash
weather-app-tkinter/
│
├── main.py             # The main Python file
├── README.md           # Project readme
└── requirements.txt    # Dependencies (if you want to add later)
```

## 📜 Code Overview

The app uses the following steps to fetch and display weather data:

1. Takes city input from the user.
2. Sends a GET request to the **OpenWeatherMap API** with the city name and API key.
3. Receives and parses the weather data in JSON format.
4. Displays temperature, humidity, and weather description in the GUI.

### API Request Example

```python
base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(base_url)
weather_data = response.json()
```

## 🛠️ Technologies Used

  Python - Programming Language
  Tkinter - GUI Framework
  OpenWeatherMap API - To fetch real-time weather data
  Requests - To send HTTP requests and fetch data


## 🛠️ Future Improvements

- Add a feature to display a 5-day weather forecast.
- Implement more data points like wind speed, visibility, etc.
- Enhance the UI with more interactive elements and themes.

## 🔗 Connect with Me

GitHub : [shadowking06](https://github.com/shadowking06)
LinkedIn : [Ujjwal Pandey](https://www.linkedin.com/in/ujjwal-pandey-324769166/)

