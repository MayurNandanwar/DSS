
#* Time Series ?: time series is s series of data point order in time.aim to observe the data how will continue in future. core assumption is thaat past data pattern will continue in future.but in realworld 
#* poswsibility of missing data because of some techical issue.or other params contribute into missing information

Note: we can not dorp missing data because order becomes eneven or we care about order also we will have issue with some model technique
we can not replace missing data with mean , meadian or mode because time series daata has trend and seasonality. ex. on every weekend sales increase compare to usual days 
if i replace missing val with mean or median then it will be distribution missmatch, also product sales on weekdays it is high compare to weekend 
# to replace missing values we have method like forward fill (ffill), also there is backwardfill method but we could not know future value so we can not replace nan with bfill,rolling method wher we set  window and minimum periods 
# ex. window=2 means previous 2 method and perform any operation ex. mean we choose, then missing value will be replace by avg value of pervious 2 value if any value is nan then here minimim period i have set 1 then miss value replace by perviois 1 value 
# and also we can replace missing value using previous year using [lambda x: x['year-month-day']-pd.offset.DateOffset(years=-1)]['temp'] if x['temp'].isna() else x['temp']]  
#! if you gave weekly data, you shoul atleastg have 2 years of data ideally 3 years data for training so 
#! that you have very clear pattern.

model = 'Additive' ,'Multiplicative'
'additive': combination of trend + cyclic + seasonality + residual
'multiplicative': trand * cyclic * seasonality * residual
#! Additive	When seasonality is constant over time (avg near to strainght line the additive)
#! Multiplicative	When seasonality increases/decreases over time (proportional to trend)(damping or exponential)

#!ACF (Autocorrelation Function)	Shows correlation between the series and its lags (including indirect correlations). Useful to detect seasonality.
#!PACF (Partial Autocorrelation Function) Shows correlation with only the direct lag (removes indirect effects). Helps identify the number of AR (AutoRegressive) terms.

#! Moving average: core concept is your data should be stationary means mean =0 and std =1. basically time series is a stationary and it has very slow varying mean.
# when your data has very fluctuation, non stationary mean then moving average might not be the best method to do forecasting.because moving average is like flat it does not provide you advantage on the latest data point. possible that 
#suddent movement happen in future so it does not detect.

#Weighted Moving Average: it provides weight to the data points according to your requirement ex. you want that i have to find moving avg for 10 data point so and lower weight to nearer data point and high weights
#to latest data point. ex you are finding probability of visiting customer. one customer came last 3 month ago and one customer came 1 week ago so based on latest data i want to find probability 
#of next time which customer will visit earlier so i will assign higher weight to latest data means high weight to 1 week early came customer.
# complexity is you have to assign weight manually 

#Exponentially Moving avg: it weights to current event higher.
# exponential smothing avg: it has factor value (alpha) is larger means it assign more weighted or more paying attension to latest data and smaller value means taking historical data or previous data into account.

#! To check data is stationary or not , also to check trend is stationary us KPSS method from state module. if p value in kpss <0.05 then data is not stationary
#! another method to test stationary data or not: use ADF method augmented dickey fuller test where if probability >0.05 then data is not stationary

#! simple exponential smoothing:
# it not just doing average but its like listioning more to what happen to our most recent periods or our most recent salse. it emphesise most recent salse.
# Equation: current level + alpha *(recent actual - current level)
# ex. current level = 100 cups sold, yesterday 120 cup sold and alpha is fine tune param = 0.2 then : 100+ 0.2*(120-100)
# if we have data then we are trying to get past a spikes like day or week when there was like huge increase or decrease
# disadvantage: not catch the trend or seasonal rushes means not cat high demand at specific period of time,often due to seasonal factors like weather, holidays, or harvest cycles
#! exponential smoothing is not really known for very insightful , it servers purpose like use past to predict future ,give more weight assign to recent information
#! initial level means first record target value at begining, smoothing level means how much percentage use past information to predict future
#!which scenario is simple exponential smoothing the most suitable forecasting method?
#ans : data with relatively constant mean and no systemetic trend and seasonality

#! when to use exponential smoothing average EMA : main assumption is that data or timeseries is stationary and  also it has very slow varying mean.
#if data is non stationary, data will not have slow moving mean or non stationary mean, then any moving avg like EMA, SMA WEMA might not be the right method to analyse the data 

#!SMA : calculate the average of last n data points where n is number of period 
  # SMA = (t+(t-1)+(t-2)+...+(t-n))/n ,  pandas func = rolling function = df['column'].rolling(window=n).mean() # ex n=3 means current data point with previous 2 data point and average them 
#! WMA(weighted moving average) assign the weights to the data points, here weights is assign manually as given below we can assign high weight factor to recent value and low to past values or vise versa according to requirement  
  # WMA = df['column'].rolling(window=3).apply(wma(np.array([0.5,1,1.5]))).shift(1) here shift 1 means this is calculate for next row or 4th row
  # def wma(weights):
  #   def cal(x):
  #     return (x* weights).mean()
  #   return cal
  #WMA is better than SMA because it assign high weight on previous data points. 

#! ema(Exponential Moving average): (close-prevous EMA) * (2/(span+1))+previous EMA
# here span is window ex. span 3 then ema will be calcdulated nased on 3 previous period

#!choice of the smoothing parameter α (0 < α < 1) affect SES forecasts
# ans : high alpha places more weight on recent information , min_periods mean if do not have 3 period then min  peroids required to calc ema , ex 1 then take 1 prevois peroid for calculate ema.
#note no need to add weight here as in WMA, better 
# ex. in stock market to calculate SMA or WMA with self assighn weight , possible that calculate 200 days sam , but in 50 days market
# sudenly goes down where SAM just doing average and WMA here we assign self weighted where this 2 will not suggest 
# or show good pattern , where ema will show closser pattern.

#!Note; when  have fluctuation  that time Moving avg not better we can use other complex model like Arima, SARIMA , LSTM


#! ESA(Exponential Smoothing Average): in EMA weights are calculate by it self. but in exponential smoothing reuires additional params
# called Alpha(smoothing factor or coefficient) this param control the rate at which influence the observations at prior timestamp and it allows to decay those 
# values exponentialy. alpha range is 0 to 1, large value means paying attension to most recent periods or datapoints, smaller values means taking histry into account
# eq.  Yt+1 = [Yt+(1-alpha)Yt-1 + (1-alpha)^2 Yt-2 + (1-alpha)^3 Yt-3 + .....] as goes towards prevous records value of alpha is decaying
# pandas : df['column'].ewm(alpha=0.7,adjust=flase,min_period=3).mean().shift(1)

# when your data point is too fluctuate and want to smooth it out then can select the low alpha value more focus on history 

#! why double exponential smoothing ?
# single exponential smoothing helps to smooth out the data while double add the anothe layer which is trand, it helps to handle the trend in data. here not just averaging high and low in data but also 
# catching the trend goes up or down also capture our selse going up or down over time 
# Equation : smoothd_level = alpha * Recent actual + (1- alpha)(Previous level- previous trend)
#           smoothed_trend =  beta * (smoothd_level-Previous Level)+(1- bete)* Previous Trend
# here alpha and bete is fine tune params
#Note: here we looking at how much level has changes from one period to next period,
# alpha adjust how much we consider our recent seles versus our previous level and trend
# bete tune how much weight give to the change in trend
# disadvantage: it captures the tred but not capture the seasonality 
# function: holtwinter.exponentialsmoothing(seaonal =None because we use Double exponential for thripple it is enable we can use add or mul)
#!When is double exponential smoothing the right tool?
#ans: suits data that drift upward and downward without reapeating cycle(series show roughly liear trend but no seasonality)
#! he parameter β controls the smoothing of which component? ans :Trend

#! why Tripple:
# it not just handle trend but also seasonality 
# holtwinter method use three equation look for level, trend and seasonality 
# three coefficient alpha controls level , bete controls trends and gama controls the seasonality
#Note : this technique is highly effective in forecasting with recurring patterns
# advantage: handle intricate patterns , enhance forecastying accuracy by accounting for both trend and seasonality

#! pros and cons of Holtwinter:
# pros: 
# if problem is simple and not complex then holt winter exponential is very good 
# simple in implementation
# adaptable to changes because it assign more weightage to recent information compate to past 

# cons:
# it has one seasonal component, we can see seasonality either weekly or yearly if you want at a time
# external factor or variable can not use to refine the forecast. it doesnt have that flexibility and it 100% rely on historical data 
# (ex. what about weather, season, festival, holiday, any harmful decease)

#* for code if you have daily data and then you want monthly and only first day record then use dayfirst=True inpd.read_csv or excel


# ARIMA (Auto Regressive Integrated Moving Average): this does not have seasonal component (Past influence the present)
# ex. if you want to predict that how much coffee you want to drink tommorrow then you have to look that how much you dring for past few days.

# for this use lags: lags are just previous data points in the timeseries. ex. lag2 means day before yesterdays value infulence today
#! ARIMA(2,d,q) = means current day prediction depends on last two days prediction
#! todays coffee = alpha + (coefficient for AR)* yesterdays_coffee + (coefficient for MA)* yesterdays error + (coefficient for AR)* day before yesterdays_coffee + (coefficient for MA)* day before yesterdays error 

# Sarima(Seasonal Auto Regressive Integrated Moving Average) : this has seasonal component but only 1 we can not add multiple seasonal component like daywise and weekday wise i want to see trend 

# Sarimax(Seasonal Auto Regressive Integrated Moving Average with External Factor):we can add seasonal factor that can affect the output like temperature season etc.(This external factors called exogenous regressor)

# AR(Auto Regressive): explore past to predict future.AR captures the past impact on now.AR is super powerful in such time series where trend and pattern are very important.we use lag values of time series to predict the future.
# I (Integrated): talk about stationarity (stationary time series: constant mean and varience and also covarience over time. constant pattern over time ) 
# stationary patter:  stable pattern over the time 
#  Non stationary : growing pattern over the time so mean will not constant it will also increase, varying amplitude(varience change over time) , varying cycle where mean not constant changes per cycle  


# integrated in arima helps to transform data to be stationary : Integrated means howmany time i need to do differencing to make our data stationary.
#! how to test for stationary: Augmented Dickey-fuller test-> its a way formally to check mean, covarience and varience are constant over time
#! differencing is very useful for understanding our data to check if we have pattern that we can use
#! max 2 time can take differencing, if p value is not <0.05 then  data is not stationary
#MA(Moving Average): mistake that model has done before. we use that as source of information to improve future prediction. so not lear from what happen but also learn from mistakes
#! ex. you have to predict that howmuch coffee you will drink tomorrow so you will look in past data this is autoregrassive 
#! you will predict based on pastdata, but what if you add that you would have to drink lot of coffee but you drink few called error means i needed 3 cups yesterday but had one only
#! so keep that in mind to predict todays.MA helps to refine the prediction based on resent mistakes or slipups.
#! this is MA. MA looks at the error you made in previous prediction
# Moving Average Equestion:
#*Yt = alpha + (coefficient for AR)*(Y)t-1 + (coefficient for MA)* Previous error  + Error for current time

#! SAERIMAX(5,1,2) = here 5 lags, 1 lag differencing for integrated and 2 lag error use for moving average for predict future
#! p ( order) = 5
#! This means the model will use the past 5 lagged values of the time series to predict the current value.
#! Example: y(t) is regressed on y(t−1), y(t−2), ..., y(t−5)

#! d (differencing order) = 1
#! This means the series will be differenced once to make it stationary.
#! New series: y'(t) = y(t) - y(t-1)

#! q (moving average order) = 2
#! The model includes the past 2 error terms (residuals) in the prediction.
#!It models the current value using the past errors: e(t−1), e(t−2)

#^ if we have log spike(big amplitude) in data and model can not explain then MAE and RMSE very big difference. RMSE usually much higher than MAE.

#* AIC(Akaike information Criterial) AND BIC(Bayseian Information Criterian)
#-> help us to choose our model
#-> score the model based on 1) how well model fits data and complexity of model means number of parameters used. means Fit the data well (low error, captures trends and patterns). 2 Use the minimum number of parameters necessary to do that.
#-> both value should be low
#! AIC is specifically all about balance ; it wants a model that fits well but doesnt overboard(It uses too many parameters .It may fit even the noise in your training data overfitting)) with too many parameters
#! BIC penalize model with more parameters. stronger feeling to model is complex.

#* SARIMA(p,d,q)(P,D,Q,m): why we use because it has seasonal component. because it needed in real world ex. ice creal sales peaking in summer
# P -> Seasonal autoregressive order (look past seasonal data ex. X no of lags to predict future)
# D -> Seasonal differencing order (stabilize the seasonal pattern)
# Q -> Seasonal Moving average order
# m -> number of period in each season(seasonal period or interval)
#ex. SARIMA(3,1,2)(2,0,2,7) MEANS 3 LAGS FROM AUTIREGRASIVE AND 2 LAGS FROM SEASONAL AUTO REGRESSEIVE(MEANS 7TH LAG AND 14TH LAG BECAUSE M=7)


#* SARIMAX(SARIMA+X(exogenous factor)): X means external factor : past sales and seasonal trends can be dealt by serima
#* but what about the temperature, holidays kind of params that affect the model. SARIMAX helps to 
#* encorporate these variable to interprete time series data.


# seasonal_decompose - To decompose a time series into its constituent parts to better understand the underlying patterns.
# components
#   Trend: The overall direction of the series (increasing, decreasing, or stable).
#   Seasonal: Repeating patterns at fixed intervals (e.g., daily, weekly, monthly).
#   Residual: The remaining variation after removing trend and seasonal components.



#! ACF: helps us to predict how much informatio we have in past 
# Autocorrelation measures the correlation between a time series and a lagged version of itself.
# Purpose: To identify patterns or repeating cycles in a time series dataset.

# Interpretation:
# Values range from -1 to 1.
# 1 indicates perfect positive correlation.
# -1 indicates perfect negative correlation.
# 0 indicates no correlation.
# ACF Plot:

# X-axis: Lag periods
# Y-axis: Correlation coefficient
# Key Features:
# At lag 0, autocorrelation is always 1 (a series is perfectly correlated with itself).
# Significant spikes at certain lags indicate repeating patterns.


#! PACF
# PACF measures the correlation between a time series and its lag, after removing the effects of all shorter lags.

# Purpose: To identify the direct relationship between an observation and its lag, without intermediate effects.

# Main Difference between ACF and PACF:
# ACF: Measures overall correlation at each lag, including indirect effects.
# PACF: Measures direct correlation at each lag, excluding indirect effects.
# in ARIMA or ARMA : AR(p): Past values directly influence current value. PACF isolates this direct influence → sharp cutoff indicates AR order.
#                  : MA(q): Past forecast errors influence current value. ACF shows this influence → sharp cutoff indicates MA order.


#prophet Mode : y(t) = g(t)+s(t)+h(t)+et  
# #g(t) is trend model non periodic changes in value of time series
  # growth: Specifies the form of the trend component.
  # 'linear' (default): For series with a constant growth rate.
  # 'logistic': For series that exhibit saturation or a carrying capacity. Requires specifying a cap column in the dataframe. means
                #the 'logistic' growth term, especially in time series forecasting models (like Prophet or other growth models), refers to a sigmoid-shaped curve that: Starts slow, Grows rapidly,and then slows down again as it approaches a maximum limit (carrying capacity).
# Note: in facebook prophet, if missing value then its ok if you dont want to impute , but you may impute based on business data
# params: interval_width = 0.80, means the model will generate 80% prediction intervals.The prediction intervals define a range where the future values are expected to fall with 80% probability and 20 % chance that forecasting will not fall within 80% interval.If you set interval_width = 0.95, the interval would be wider (more uncertain),ex. maybe:95% interval: [75, 125] wider compare to 80% interval: [85, 115]
        # face book auto deside yearly weekly or daily seasonality no need to give , if you have to provide based on data then you can.
        ##Note: interval_width deside according to requirement, profit model takes tow variable one is datetime and 2nd is target variable, to add multi variable use model.add_regreesor('column name') for rach column 
#! how model can use multivariate time series:
# profit takes column name is ds is datetime and y as target fix column names. we can add multi columns with help of model.regressor(column name) we can add

  seasonality_prior_scale : strength 
  seasonalityHoliday_prior_scale : how much holiday should affect the seasonality curve  because holiday and seasonality connected with each.
  change_point_prior_scale : does if the trend change easily. we have bit of overfitting. if doesnt change then have underfitting
  This three are the main params to tune

#!Note: Prophet is very good at dealing with non- linearity. bydefault facebook create use confidence interval 80 % we can add manually as param interval_width =0.95 if you want to set 95%.
#! one more advantage is that it itself identify that which seasonality is there (yearly, monthly, daily, Quarterly)
#! it is additive model does not identify trend and data is not stationary

#! LSTM: for multivariate
#Pros: robust to outlire, great work with Non linearity, Simple to use.
#!Cons: No insight, Required tuning, Poor at dealing with trends

# training process of LSTM
# You start by training on days 1 to 80.

# You forecast sales for days 81 to 90 (forecast horizon = 10 days).

# Then you move forward by, say, 5 days (stride = 5).

# Now, train on days 1 to 85, forecast days 86 to 95.

# Move forward again, train on days 1 to 90, forecast days 91 to 100.


#! TFT(Temporal fusion transformer): Imagine you are running forecasting for retailer chain and you model cant keepup with the intricate
(having many small parts or details put together in a complicated way) seasonality and promotional impact on sales
Traditional method like ARIMA and even LSTM do fall short. they cant dynamically adjust for holiday, special event,
even sudden market change
--> TFT gives accurate and multi-horizone forcast by capturing complex pattern and multi influencing factor in data.
multi-horizone  means : TFT can predict multiple future points at once which is crucial for detailed planning.
The attension mechanism it dynemically prioritizes relevant features improving accuracy of Model
Interpretability : TFT provides the insights into which fratures impact your forecast the most making the result trustworthy and transperent
--> flexibility with inputs so it seamlessly handles variety of input types.
because of this things our forecasting will be more robust and well comprehensive
-> while arima and LSTM model predict the future for 1 hour , for 1 month at a time herfe need 2 model one for hourly prediction , 2nd for monthly prediction 
, TFT model design to predict multiple futurepoints simulteneously, TFT can forecast different time scale, it can predict yearly, monthly, weekly in one go or i single model.
This capability is particularly valuable for company like uber, which need to forecast ride demand for diff time of days, day of month,special events , months whatsoever
--> Dynamic feature prioritize : TFT uses advance attension mechanism to dynamically prioritize the most relavent features at each time.
this allows model to adapt to changes conditions in realtime.This capability ensures that model focus on most relevant factor that infulence the predictions.
Ex. Ubers forecasting model needs to adjust variety of dynamic factors like events. so think concerts, sports games where changes,peak travel times and all of this
significantly impact ride demand, attension mechanism assigns diff weights to these feature over the time, this highlights varing importance at diff points
--> ex. during special time of the day or in certain weather condition, model might prioritize the diff. features and this prioritization can directly observed and 
analyzed. This kind of transperacy is essential for business application. this helps to improve decision making.DeprecationWarning
you can explore and find opportunity just with timeseries forecasting
--> flexibility : TFT handles the wide variety of input types static features so day of week,city and non future features like 
schedule events and observe historical data like past ride demands. this flexibility allows the TFT to incorporate diverse data source seamlessly enhance its ability to capture complexity of 
realworld scenarios.

static features: holiday, city etc, dynamic feature changes over time: weather condition, local event like concert and past historical data 
helps model to learn and predict the


TFT Architecture:

y(q,t,T) = fq(T,(yi,t-k:t),(Zi,t-k:t),(Xi,t:t+T),Si)
in fq, q is quantile
(yi,t-k:t): historical target Value  for  ith timeseries from time t-k to t, this represents the past observations of target variable
(Zi,t-k:t): unknown input also known as past covariates for i-th timeseries from the time t-k to t time. this inputs that are known only up to current timestamp and include variables like pas weather condition,past sales etc that we know what has happened but we dont know what will happen in Future 
(Xi,t:t+T): known input also known as future covariates for i-th timeseries from time t to t+T time. these are input known in advance and include variable like holiday,dat of week, scheduled events
Si = static covariates does not change over time


fq  the function used to compute quantile forcast
T   The forecast horizone, represent how far into the future we are predicting


y(q,t,T) : predicted value of i-th timeseries at time t for quantile q and forcast horizone T


Layes of architecture: Encoder and decoder layer is there 

Encoder layer : (Zi,t-k:t) unknown input  pass to the LSTM layer processing happens sequentially and als this input directly pass to the 
add and normalization layer where out of LSTM and input goes to LSTM Layer will added to stabilize the model and perform normalization for computationally
effective
GRN layer : gated recurrent Network , from add & Norm layer result of encoder pass to the GRN layer this layer ensure that only 
most relavent information pass through layer improves model focus and accuracy. so GRN design to enhance the network learning capability
by managing flow of information through gating mechanism.
--> Component of GRN:
1) Gating mechanism : filter and leting only important information pass through and blocking out unnecessary data.
2)residual connection: does same work as happen in Add&Norm layer. add input  to its output layer and helping to keep essential information to intact
3)Normalization : normalize the output to stabilize the training process.

Masked Multi-head attension layer: focus on different part of information and understand relationship between and capture patterns


Dense layer :  applies final transformation  to the processed data, integratting all learned patterns and dependency to generate the final predictions.
this layer is crucial for generating final predictions.
Quantile forcast provides the models prediction for different quantiles, offering range of possibile future values to understand uncertainty and variability in prediction. 
it helps to make more informed decisions based on prediction range of values

static information provides to all the important layer of TFT model like LSTM , GRN layer , provides consistant information
needs to be accessible at various stage of processing 

TFD decoder responsible synthesizing((to make or combine diff thing ) the information from past inputs, non future input and static covariates 
to produce predictions.it does by advance component like attension mechanism to ensure that more relavant information is emphesized and Model
learn best way possible.
decoder combines these inputs to generate final predictions,while considering the dependencies and patterns.

covariates information supports future and past covariates: 
  -->https://unit8co.github.io/darts/#:~:text=Darts%20is%20a%20Python%20library,%2C%20similar%20to%20scikit%2Dlearn.

TFD : 
pros: Highly accurate forecasting 
handling multi timeseries covariates
interpretability : so attension mechanism helps to clarify which feature influence the forcasting.
robustness to missing data:it handles irregukar time series
it takes past and future covariates

cons:
computationally intensive or computational complexity require GPU
long training time: for realtime forcasting it may not be the best
take time to prepare the data 
prone to overfitting : risk of overfitting
if have tiny dataset deep learning may not be the best option


 NBeates
 --> it alloes past covariates(static) , not allow future covariates(static).
Pros:
no need to do feature engineering
handle complex patterns 
flexibility with covariates (past covariates)
scalability : small , large dataset, long forecast nbeates will excel at all of them.
simpler and robust 

cons:
no support for future covariates
its deep learning model computationally intensive
overfitting because of there are number of params so need to do param tuning

