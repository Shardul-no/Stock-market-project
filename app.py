from flask import Flask, render_template, request
import pandas as pd
import yfinance as yf

app = Flask(__name__)

# Load the data from the CSV file
data = pd.read_csv('CompanyData.csv')

# Convert 'Market Cap' to numeric, forcing errors to NaN
data['Market Cap'] = pd.to_numeric(data['Market Cap'], errors='coerce')

# Define market cap categories
def categorize_market_cap(market_cap):
    if pd.isna(market_cap):  # Check for NaN values
        return 'N/A'
    if market_cap > 100000000000:  # 1 trillion
        return 'Large-Cap'
    elif market_cap > 33221000000:  # 33,221 crore
        return 'Mid-Cap'
    else:
        return 'Small-Cap'

# Add a new column for market cap category
data['Market Cap Category'] = data['Market Cap'].apply(categorize_market_cap)

@app.route('/', methods=['GET', 'POST'])
def home():
    sectors = data['Sector'].unique()
    filtered_data = None

    if request.method == 'POST':
        selected_sector = request.form.get('sector')
        risk_apetite = request.form.get('risk_apetite')

        # Filter data based on selected sector
        filtered_data = data[data['Sector'] == selected_sector]

        # Further filter based on risk appetite
        if risk_apetite == 'High':
            filtered_data = filtered_data[filtered_data['Market Cap Category'] == 'Large-Cap']
        elif risk_apetite == 'Mid':
            filtered_data = filtered_data[filtered_data['Market Cap Category'] == 'Mid-Cap']
        elif risk_apetite == 'Low':
            filtered_data = filtered_data[filtered_data['Market Cap Category'] == 'Small-Cap']

        # Convert 'Annual Return (%)' to numeric to ensure sorting works
        filtered_data['Annual Return (%)'] = pd.to_numeric(filtered_data['Annual Return (%)'], errors='coerce')

        # Sort data by Annual Return (CAGR) in descending order
        filtered_data = filtered_data.sort_values(by='Annual Return (%)', ascending=False)

    return render_template('index.html', sectors=sectors, data=filtered_data)

def get_nifty_status():
    try:
        nifty = yf.Ticker("NIFTY.NS")
        hist = nifty.history(period="2d")
        
        if hist.empty or len(hist) < 2:
            return None, None  # Return only 2 values
        
        latest_close = hist['Close'].iloc[-1]
        prev_close = hist['Close'].iloc[-2]
        
        status = "up" if latest_close > prev_close else "down"
        icon = "🔼" if latest_close > prev_close else "🔽"
        
        return status, icon  # Return only 2 values instead of 3
    except Exception as e:
        print("Error fetching Nifty data:", e)
        return None, None

@app.route('/support')
def support():
    status, icon = get_nifty_status()
    return render_template('support.html', status=status, icon=icon)

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True) 