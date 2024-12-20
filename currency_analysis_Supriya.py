#!/usr/bin/env python
# coding: utf-8

# In[1]:



get_ipython().system('pip install yfinance')


# ### Step 1:
# To scrape EUR/INR data, we'll use the yfinance Python library, which is easy to work with for historical data from Yahoo Finance

# In[2]:


import yfinance as yf
import pandas as pd

# Define the ticker symbol for EUR/INR
ticker = "EURINR=X"

# Define the date range
start_date = "2023-01-01"
end_date = "2024-09-30"

# Download data
data = yf.download(ticker, start=start_date, end=end_date)

# Display the first few rows
print(data.head())

# Save to a CSV file if needed
data.to_csv("EURINR_data.csv")


# ### Step 2: Calculate Technical Indicators
# Now that we have the data, let’s calculate the Moving Average, Bollinger Bands, and Commodity Channel Index (CCI).
# 
# Moving Average: We'll calculate the Simple Moving Average (SMA) for 1-day and 1-week periods.
# 
# Bollinger Bands: Bollinger Bands consist of an upper band, a lower band, and the moving average (20-day window is typical).
# 
# Commodity Channel Index (CCI): CCI is a momentum-based indicator that compares the current price to the average price over a specified period (typically 20 days).
# 
# #### Code for Technical Indicators

# In[4]:


# Import necessary libraries for calculations
import numpy as np

# Ensure that only the 'Close' column is used for rolling standard deviation
data['20D_MA'] = data['Close'].rolling(window=20).mean()
data['Rolling_STD'] = data['Close'].rolling(window=20).std()

# Calculate the Upper and Lower Bollinger Bands based on 20D_MA and Rolling_STD
data['Upper_Band'] = data['20D_MA'] + 2 * data['Rolling_STD']
data['Lower_Band'] = data['20D_MA'] - 2 * data['Rolling_STD']

# Drop the temporary 'Rolling_STD' column if you don't need it
data = data.drop(columns=['Rolling_STD'])

# Display the data with Bollinger Bands
print(data[['Close', '20D_MA', 'Upper_Band', 'Lower_Band']].tail())


# ### Step 3: Determine BUY/SELL/NEUTRAL Recommendations
# Based on the calculated indicators, here’s a simple rule for each:
# 
# Moving Average: If the 1-day MA is above the 1-week MA, it may indicate a short-term bullish trend (BUY); otherwise, SELL.
# Bollinger Bands: If the price is near or above the upper band, it might be overbought (SELL). If it’s near or below the lower band, it could be oversold (BUY).
# CCI: If CCI > 100, consider it as overbought (SELL); if CCI < -100, consider it as oversold (BUY); else, NEUTRAL.
# #### Code for Decision Making

# In[12]:


import pandas as pd

# Load your data (update the path)
data = pd.read_csv('EURINR_data.csv')

# Print the initial state of the DataFrame
print("Initial DataFrame shape:", data.shape)
print("Initial DataFrame head:")
print(data.head())

# Check for empty columns
for column in data.columns:
    print(f"{column}: {data[column].isnull().sum()} NaN values")

# Assuming you are performing calculations, make sure these columns exist
required_columns = ['Close', 'Upper_Band', 'Lower_Band']
print("Checking for required columns:")
for col in required_columns:
    if col not in data.columns:
        print(f"Column '{col}' is missing.")
    else:
        print(f"Column '{col}' found with {data[col].isnull().sum()} NaN values.")

# Drop NaN values if needed
data = data.dropna()

# Check if DataFrame is still empty after drop
print("DataFrame shape after dropping NaN:", data.shape)

# Proceed with your recommendations if data exists
if not data.empty:
    # Initialize recommendations
    print("Proceeding with recommendations...")
    # Your recommendation code goes here
else:
    print("DataFrame is empty after dropping NaN.")


# In[13]:


import pandas as pd

# Load your data, skipping the first two rows
data = pd.read_csv('EURINR_data.csv', header=2)

# Print the cleaned DataFrame
print("Cleaned DataFrame head:")
print(data.head())


# In[14]:


# Check for NaN values
print("NaN values in each column:")
print(data.isnull().sum())


# In[15]:


# Rename columns to ensure they match expected names
data.columns = ['Date', 'Adj_Close', 'Close', 'High', 'Low', 'Open', 'Volume']  # Update as needed

# Print to verify changes
print("DataFrame with renamed columns:")
print(data.head())


# In[16]:


# Drop NaN values
data = data.dropna()

# Check if DataFrame is still empty after drop
print("DataFrame shape after dropping NaN:", data.shape)


# In[17]:


# Example logic for recommendations
# Ensure that the required columns exist
if 'Close' in data.columns and 'Upper_Band' in data.columns and 'Lower_Band' in data.columns:
    data['MA_Recommendation'] = np.where(data['1D_MA'] > data['1W_MA'], 'BUY', 'SELL')
    
    # Add Bollinger Band recommendations
    data['Bollinger_Recommendation'] = np.where(data['Close'] > data['Upper_Band'], 'SELL', 
                                                np.where(data['Close'] < data['Lower_Band'], 'BUY', 'NEUTRAL'))

    # Print recommendations
    print("Recommendations:")
    print(data[['Date', 'MA_Recommendation', 'Bollinger_Recommendation']].head())
else:
    print("One or more required columns are missing.")


# In[18]:


# Print the current columns in the DataFrame
print("Current DataFrame columns:")
print(data.columns.tolist())


# In[19]:


# Calculate moving averages and Bollinger Bands
window = 20  # Typical period for Bollinger Bands

# Calculate the moving average and standard deviation
data['20_MA'] = data['Close'].rolling(window=window).mean()
data['20_STD'] = data['Close'].rolling(window=window).std()

# Calculate Upper and Lower Bands
data['Upper_Band'] = data['20_MA'] + (data['20_STD'] * 2)
data['Lower_Band'] = data['20_MA'] - (data['20_STD'] * 2)

# Check the DataFrame to see if the new columns were added
print("DataFrame with Bollinger Bands:")
print(data[['Date', 'Close', 'Upper_Band', 'Lower_Band']].tail())


# In[20]:


# Now check again for required columns
required_columns = ['Close', 'Upper_Band', 'Lower_Band', '1D_MA', '1W_MA']
missing_columns = [col for col in required_columns if col not in data.columns]

if not missing_columns:
    # Add recommendations
    data['MA_Recommendation'] = np.where(data['1D_MA'] > data['1W_MA'], 'BUY', 'SELL')
    data['Bollinger_Recommendation'] = np.where(data['Close'] > data['Upper_Band'], 'SELL', 
                                                np.where(data['Close'] < data['Lower_Band'], 'BUY', 'NEUTRAL'))

    # Print the recommendations
    print("Recommendations:")
    print(data[['Date', 'MA_Recommendation', 'Bollinger_Recommendation']].tail())
else:
    print("Missing columns:", missing_columns)


# In[21]:


# Assuming 'Close' is available and is already in the correct data type

# Calculate the 1D Moving Average (which is just the last close)
data['1D_MA'] = data['Close'].shift(1)  # Shift by one to get the previous day's close

# Calculate the 1W Moving Average (average of the last 5 closes)
data['1W_MA'] = data['Close'].rolling(window=5).mean()

# Check the DataFrame to see if the new columns were added
print("DataFrame with moving averages:")
print(data[['Date', 'Close', '1D_MA', '1W_MA']].tail(10))


# In[22]:


# Check again for required columns
required_columns = ['Close', 'Upper_Band', 'Lower_Band', '1D_MA', '1W_MA']
missing_columns = [col for col in required_columns if col not in data.columns]

if not missing_columns:
    # Add recommendations
    data['MA_Recommendation'] = np.where(data['1D_MA'] > data['1W_MA'], 'BUY', 'SELL')
    data['Bollinger_Recommendation'] = np.where(data['Close'] > data['Upper_Band'], 'SELL', 
                                                np.where(data['Close'] < data['Lower_Band'], 'BUY', 'NEUTRAL'))

    # Print the recommendations
    print("Recommendations:")
    print(data[['Date', 'MA_Recommendation', 'Bollinger_Recommendation']].tail(10))
else:
    print("Missing columns:", missing_columns)


# In[23]:


import matplotlib.pyplot as plt

# Plot Close Price with Moving Average
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['1D_MA'], label='1-Day MA')
plt.plot(data['1W_MA'], label='1-Week MA')
plt.legend()
plt.title('EUR/INR with Moving Averages')
plt.show()

# Plot Close Price with Bollinger Bands
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['Upper_Band'], label='Upper Bollinger Band', linestyle='--')
plt.plot(data['Lower_Band'], label='Lower Bollinger Band', linestyle='--')
plt.legend()
plt.title('EUR/INR with Bollinger Bands')
plt.show()


# In[ ]:




