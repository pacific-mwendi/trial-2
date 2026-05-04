import nce as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tickers
msft = "MSFT"
sp500 = "^GSPC"
dji = "^DJI"

# Download 8 years of daily data
data = yf.download([msft, sp500, dji], start="2018-01-01")["Adj Close"]

# Compute daily returns
returns = data.pct_change().dropna()

# Separate series
msft_ret = returns[msft]
sp_ret = returns[sp500]
dji_ret = returns[dji]

# Regression (beta)
beta_sp, alpha_sp = np.polyfit(sp_ret, msft_ret, 1)
beta_dji, alpha_dji = np.polyfit(dji_ret, msft_ret, 1)

# Create regression lines
line_sp = beta_sp * sp_ret + alpha_sp
line_dji = beta_dji * dji_ret + alpha_dji

# Plot
plt.figure()

plt.scatter(sp_ret, msft_ret, label="MSFT vs S&P 500")
plt.plot(sp_ret, line_sp, label=f"S&P 500 Beta = {beta_sp:.2f}")

plt.scatter(dji_ret, msft_ret, label="MSFT vs DJI30")
plt.plot(dji_ret, line_dji, label=f"DJI30 Beta = {beta_dji:.2f}")

plt.xlabel("Market Returns")
plt.ylabel("Microsoft Returns")
plt.title("Microsoft Beta vs S&P 500 and DJI30 (Last 8 Years)")
plt.legend()

plt.show()