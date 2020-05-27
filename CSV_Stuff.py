import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# csv file we are working on
aapl = pd.read_csv("C:\\Users\\jakel\\OneDrive\\Desktop\\UDacity\\aapl.csv")
spy = pd.read_csv("C:\\Users\\jakel\\OneDrive\\Desktop\\UDacity\\spy.csv",index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])


def create_graph(file):
    file[['Close','Adj Close']].plot()
    plt.show()

def create_df():
    # define date range
    start_date ='2/6/2020'
    end_date ='3/6/2020'
    dates = pd.date_range(start_date,end_date)

    # create empty data frame
    df1 = pd.DataFrame(index = dates)

    # joins two data frames
    # spy is sp100 to make sure there was trading that day
    df1 = df1.join(spy)

    # drops all the nan na_values
    df1 = df1.dropna()

    return df1

if __name__ == '__main__':
    print(create_df())
