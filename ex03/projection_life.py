from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def main():

    # load csv with the function of previous exercise
    life_expectancy = load("life_expectancy_years.csv")
    if life_expectancy is None:
        return

    income_per_person = load("income_per_person_gdppercapita\
_ppp_inflation_adjusted.csv")
    if income_per_person is None:
        return

    # extract 1900's data
    life_expectancy = life_expectancy['1900']
    income_per_person = income_per_person['1900']

    # create new table with desired data
    both = pd.concat([life_expectancy, income_per_person], axis=1)

    # rotate the data table
    both = both.transpose()

    # change indexes for data clarity
    both.index = ['life_expectancy', 'average_revenue']

    # initialize the dot plot
    plt.figure()

    # add dots
    for column in both.columns:
        plt.plot((both[column]['average_revenue']),
                 (both[column]['life_expectancy']), 'bo')

    # customize the plot
    plt.xscale('log')
    x = [300, 1000, 10000]
    labels = ['300', '1k', '10k']
    plt.xticks(x, labels)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    # display the plot
    plt.show()


if __name__ == "__main__":
    main()
