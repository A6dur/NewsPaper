📰 News Fetcher
A simple Python script to fetch the latest news headlines from a news API. This project is a great starting point for anyone looking to build a news aggregator, a personal news feed, or a command-line tool for staying up-to-date.

✨ Features
✅ Fetches top headlines from a specified country.

🔎 Supports searching for news by a specific keyword.

🔑 Configurable API key management for security.

💻 Simple and easy-to-understand codebase.

🛠️ Prerequisites
Before you begin, ensure you have the following installed on your system:

🐍 Python 3.6 or higher

📦 pip (Python package installer)

🚀 Installation
Follow these steps to get your project up and running:

Clone the repository:

git clone https://github.com/your-username/news-fetcher.git
cd news-fetcher

Create a virtual environment (recommended):

python -m venv venv

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

🔑 API Key Setup
Get an API Key:
Sign up for a free API key from a news API provider like NewsAPI.

Create a .env file:
In the root directory of your project, create a new file named .env. This file will store your sensitive information.

Add your API key:
Open the .env file and add your API key like this:

NEWS_API_KEY=YOUR_API_KEY_HERE

Remember to replace YOUR_API_KEY_HERE with the actual key you obtained.

🏃 Usage
You can run the script from your terminal.

🌍 To get the top headlines from a specific country (e.g., the US):

python main.py --country us

📝 To search for news with a specific keyword (e.g., "technology"):

python main.py --keyword technology

🤝 To combine both a country and a keyword search:

python main.py --country us --keyword business

📦 Dependencies
requests: Used to make HTTP requests to the news API.

python-dotenv: Used to load environment variables from the .env file.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
