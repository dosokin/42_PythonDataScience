from load_csv import load
import matplotlib.pyplot as plt


def main():

    plt.close("all")

    # use the function of previous exercise to load the csv
    csv = load("life_expectancy_years.csv")
    if csv is None:
        return

    # extract line related to France data
    france_data = csv[csv['country'] == 'France']

    # remove unwanted data
    france_data = france_data.drop(['country'], axis=1)

    # rotate the data
    france_data = france_data.transpose()

    # create the plot based on france_data values
    france_data.plot(legend=False)

    # customize legend of the plot
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    # display plot
    plt.show()


if __name__ == "__main__":
    main()
