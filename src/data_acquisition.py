#%%
import pandas as pd

#%%
def load_historical_data(ticker, columns=None, start_date=None, end_date=None):
  """
  Loads historical stock data from a text file.

  Args:
    ticker (str): Ticker symbol of the stock.
    columns (list, optional): List of desired columns (including 'Date'). Defaults to None (all columns).
    start_date (str, optional): Start date in YYYY-MM-DD format. Defaults to None (entire file).
    end_date (str, optional): End date in YYYY-MM-DD format. Defaults to None (entire file).

  Returns:
    pd.DataFrame: DataFrame containing historical stock data.
  """
  # Build the filename with format f"{ticker}.*"
  filename = f"../data/historical/Stocks/{ticker}.us.txt"

  # Read the data from the text file
  try:
    # Read the data from the text file
    data = pd.read_csv(filename, parse_dates=["Date"], index_col="Date")
  except FileNotFoundError:
    raise Exception(f"File not found: {filename}")

  # Select desired columns
  if columns:
    data = data[columns]

  # Filter data based on dates
  if start_date:
    data = data.loc[start_date:]
  if end_date:
    data = data.loc[:end_date]

  return data

# %%
df = load_historical_data("aapl", columns=["Open","High"], start_date="1999-01-01")
# %%
