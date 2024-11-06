from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():

    # load given csv
    csv = load("population_total.csv")
    if csv is None:
        return

    # extract desired data rows
    france_data = csv[csv['country'] == 'France']
    belgium_data = csv[csv['country'] == 'Belgium']

    # create a new data table with selected rows
    data = pd.concat([belgium_data, france_data])

    # cast data to float and crop desired years
    for i, column in enumerate(data.columns[1:]):
        data[column] = data[column].str.replace('M', '').astype(float)
        if int(data[column].name) > 2050:
            data = data.drop([data[column].name], axis=1)

    # rotate the data table
    data = data.drop(['country'], axis=1)
    data = data.transpose()

    # initialize the plot
    data.plot(legend=False, color=['blue', 'green'])

    # customize the plot
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(['Belgium', 'France'], loc='lower right')

    labels = ['20M', '40M', '60M']
    y = [20, 40, 60]
    plt.yticks(y, labels)

    # display plot
    plt.show()


if __name__ == "__main__":
    main()
