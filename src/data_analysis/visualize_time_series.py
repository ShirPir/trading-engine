from data_acquisition import load_historical_data
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def plot_historical_data(tickers, columns=None, start_date=None, end_date=None):
  """
  Generates and plots timeseries data for one or more tickers in subplots.

  Args:
      tickers (str or list): Single ticker symbol or list of ticker symbols.
      columns (list, optional): List of desired columns (default: None - all columns).
      start_date (str, optional): Start date in YYYY-MM-DD format (default: None - beginning of data).
      end_date (str, optional): End date in YYYY-MM-DD format (default: None - end of data).
  """

  # Handle single ticker or list of tickers
  if isinstance(tickers, str):
    tickers = [tickers]

  # Create a figure and gridspec object for consistent subplot size
  fig = plt.figure(figsize=(12, 6*len(columns)))  # Adjust figsize as needed
  gs = gridspec.GridSpec(len(columns), 1, height_ratios=[1]*len(columns))

  # Loop through tickers and columns, plotting data in subplots
  axes = []
  for i in range(len(columns)):
    axes.append( fig.add_subplot(gs[i]) )

  for i, ticker in enumerate(tickers):
    data = load_historical_data(ticker, columns, start_date, end_date)
    for j, col in enumerate(columns):
      axes[j].plot(data.index, data[col], label=ticker)
      axes[j].set_title(f"{col}")
      axes[j].legend()

  # Set common labels for x-axis across all subplots (optional)
  if len(columns) == 1:
    plt.xlabel("Date")
  else:
    for ax in axes:
      ax.set_xlabel("Date")  # Set x-axis label for each subplot

  # Style the plot
  plt.style.use('seaborn-v0_8-whitegrid')  # Example style, adjust as desired
  plt.tight_layout()

  # Make the plot interactive
  #plt.interactive()
  plt.show()