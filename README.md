# Stock Market Analysis Application

This project is a web-based Stock Market Analysis Application developed using the Flask framework in Python. It allows users to explore historical stock data, visualize stock trends, and gain insights into the performance of various companies. The application is built to help investors and stock market enthusiasts make informed decisions by providing interactive charts and detailed company profiles.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Company Information Display:** View basic company information, including the stock symbol, industry, and description.
- **Historical Stock Data Retrieval:** Retrieve stock price data for selected companies over different timeframes (e.g., 1 day, 1 week, 1 month).
- **Stock Performance Visualization:** Visualize stock price trends with interactive graphs such as line charts, candlestick charts, and bar charts.
- **Stock Symbol Search:** Easily search for companies by their stock ticker symbols.
- **Custom Date Range:** Filter historical stock data by date range for better analysis.
  
---

## Technologies Used

- **Frontend:**
  - HTML, CSS: Used for the layout and design of the web pages.
  
- **Backend:**
  - Python, Flask: Flask is used as the web framework to handle routing, requests, and backend logic.
  
- **Data Processing:**
  - Pandas: For data manipulation and analysis of historical stock data.
  
- **Data Visualization:**
  - Matplotlib: Used to generate graphical representations of stock performance, including line charts, candlestick charts, and bar charts.
  
- **External APIs:**
  - Financial APIs (e.g., Alpha Vantage, Yahoo Finance): Used to retrieve historical stock price data.

---

## Installation

Follow these steps to set up and run the Stock Market Analysis Application locally:

### 1. Clone the repository:

```bash
git clone https://github.com/Shardul-no/Stock-market-project.git
```

### 2. Navigate to the project directory:

```bash
cd Stock-market-project
```

### 3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

### 4. Activate the virtual environment:

- For **Windows**:

```bash
venv\Scripts\activate
```

- For **macOS/Linux**:

```bash
source venv/bin/activate
```

### 5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 6. Run the Flask application:

```bash
python app.py
```

After running the application, open your web browser and navigate to `http://127.0.0.1:5000/` to access the app.

---

## Usage

- **Home Page:** The landing page where users can search for companies by their stock symbols (tickers).
- **Company Info Page:** After selecting a company, users will be redirected to a page displaying basic company details and historical stock data.
- **Charts:** Historical stock data is presented through interactive charts, such as line graphs and candlestick charts, showing stock price trends over time.
- **Date Range Filter:** Users can filter the stock data based on custom date ranges (e.g., one day, one week, or one month).
  
---

## Data Sources

- **CompanyData.csv:** Contains information about companies, including stock symbols and brief descriptions.
- **Tickers.csv:** A list of stock ticker symbols used to fetch stock price data.
- **Stock Data API:** The application fetches historical stock data via APIs like Alpha Vantage or Yahoo Finance, allowing users to retrieve past stock prices.

---

## Project Structure

```
Stock-market-project/
│
├── app.py                     # Main Flask application file
├── requirements.txt           # List of dependencies
├── templates/                 # HTML templates for rendering pages
│   ├── home.html
│   ├── company_info.html
│   ├── charts.html
│   └── ...
├── static/                    # Static assets (CSS, images)
│   ├── style.css
│   └── ...
├── data/                      # Data files
│   ├── CompanyData.csv
│   └── Tickers.csv
└── README.md                  # Project documentation
```

---

## Contributing

Contributions are not welcome!