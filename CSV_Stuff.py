import pandas as pd
import matplotlib.pyplot as plt

# csv file we are working on
df = pd.read_csv("C:\\Users\\jakel\\OneDrive\\Desktop\\UDacity\\aapl.csv")

def create_graph(file):
    print(file['Adj Close'])
    file[['Close','Adj Close']].plot()
    plt.show()

if __name__ == '__main__':
    create_graph(df)
