## steps to perform timeseries
#no need to shuffle data because its a time series 

step1 = 'first train on normal data'
strp2 = 'predict on abnormal data or anomaly data'


# global outlire : data point that are completely out side the normal distribution. it can be due to data issue or business process issue.
# sometime it can be genuine.
# contextual outlire : very common outlire in data


# seasonality vs cyclic 
--> seasonality means season wise trend changes ex. in festival trafic in road will be high. seeing same behaviour over the interval of time
--> cyclic means suddenly gold price on spike, event suddenly occure and demand increase so syclic meas not predicteble where as seasonality 
predictable that every november sales increases due to some reason. Cyclic completely depend on business cycle or economic cycle.



#! example of company sales data 
# Looking at the ACF plot you shared — aside from lag 0 (which is always 1.0), the other lags are all very small (mostly between −0.2 and +0.2) and stay within the blue confidence interval.

# That tells us:

# There is no meaningful autocorrelation in your series.

# The series behaves almost like white noise (past values don’t explain future values).

# Adding more lags (like AR terms in ARIMA or input windows in TFT) won’t help much, since there’s no signal in the past that predicts the future.

# 📌 Implications for Forecasting
# ARIMA/AR-based models: Not very useful here, since AR terms rely on autocorrelation.

# Naïve / Simple models: A last value forecast or moving average may perform just as well.

# Exponential Smoothing (ETS): Can still capture level (and trend if it exists), even without autocorrelation.

# Machine learning (like TFT): Will likely overfit unless you add external covariates (e.g., price, season, promotions).

Example::
# Your ACF/PACF values (−0.3 to +0.3)
# → Each individual lag has only weak correlation with the future.
# Your Ljung–Box p < 0.05
# → The combined pattern across multiple lags is unlikely to be random,
# → but since each one is small, the overall predictive signal is weak.

 #!🔑 What This Means for Forecasting
# Yes — the predictive power for the future is weak.(because acf/pacf=-0.3 to 0.3)

# Past values explain only a small portion of future variation.

# Models that rely heavily on autocorrelation (like ARIMA with big p/q) won’t give much extra accuracy.

# A simple baseline like “next month = this month” may perform nearly as well as complex models.

# If you want stronger forecasts, you’ll likely need external covariates (e.g., seasonality indicators, macro data, promotions, holidays, etc.).

# ✅ So in short:
# The Ljung–Box result tells you there is some structure,
# But the ACF/PACF magnitudes tell you the structure is too weak to be highly predictive.

#! correlation method is not suitable for time series because it does not under stand the order of time 
there are other method like grangercasuality statistical test


#! Methods used in time series 
# sample method is used when we have uneven data in time series so we can convert this data to hourly level or M , Q, Business day, Daily, weekly etc level 

#! to achive stationary data use diff (in non stationary)
df.diff() # differance one val with previous value 
df.diff(2) # differance one val with previous 2nd value 

# calculate percentage changes every month in sell
data[:].pct_change(1)

# model.plot_diagnose() used to do analysis of chart


