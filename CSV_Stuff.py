import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# data_df = yf.download("aapl", start="2020-05-026", end="2020-05-27")
# data_df.to_csv('aapl1.csv')

# csv file we are working on
spy = pd.read_csv("C:\\Users\\jakel\\OneDrive\\Desktop\\UDacity\\spy.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])

def create_graph(file):
    file[['Close','Adj Close']].plot()
    plt.show()

def create_df():
    # define date range
    start_date ='5/27/2019'
    end_date ='5/27/2020'
    dates = pd.date_range(start_date,end_date)

    # create empty data frame
    df1 = pd.DataFrame(index = dates)

    # joins two data frames
    # spy is sp100 to make sure there was trading that day
    df1 = df1.join(spy,how='inner')

    df1 = df1.rename(columns={"Adj Close":"spy"})

    symbols = ["aapl","ABIO"]

    for symbol in symbols:
        df_temp = pd.read_csv("{}.csv".format(symbol),index_col="Date",parse_dates=True,usecols=["Date","Adj Close"],na_values="nan")

        df_temp = df_temp.rename(columns={"Adj Close":symbol})

        df1 = df1.join(df_temp)

    # drops all the nan na_values
    df1 = df1.dropna()

    return df1

def plot_data(df):
    ax = df.plot(title="Stock Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Prices")
    plt.show()

def normalize_data(df):
    return df/ df.iloc[0,:]

if __name__ == '__main__':
    plot_data(normalize_data(create_df()))
