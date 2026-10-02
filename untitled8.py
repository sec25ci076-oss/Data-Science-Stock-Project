import pandas as pd
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock):
    # Sort dates chronologically
    stock_sorted = stock_data.sort_values(by="Date")
    rev_sorted = revenue_data.sort_values(by="Date")
    
    # Create 2 static subplots stacked vertically
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=False)
    fig.suptitle(f"{stock} Financial Dashboard", fontsize=16, fontweight='bold')
    
    # Chart 1: Historical Share Price
    ax1.plot(pd.to_datetime(stock_sorted['Date']), stock_sorted['Close'].astype(float), color='tab:blue', linewidth=2)
    ax1.set_title("Historical Share Price")
    ax1.set_ylabel("Price ($US)")
    ax1.grid(True, linestyle='--', alpha=0.5)
    
    # Chart 2: Historical Revenue
    ax2.plot(pd.to_datetime(rev_sorted['Date']), rev_sorted['Revenue'].astype(float), color='tab:orange', linewidth=2)
    ax2.set_title("Historical Revenue")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Revenue ($US Millions)")
    ax2.grid(True, linestyle='--', alpha=0.5)
    
    # Adjust spacing and display directly in notebook output
    plt.tight_layout()
    plt.show()
