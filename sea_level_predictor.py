import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df)

    # Create scatter plot
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data")
    # Adding title and labels
    ax1.set_title("CSIRO Adjusted Sea Level by Year")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("CSIRO Adjusted Sea Level (inches)")

    # Create first line of best fit
    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    # Generate x values from the first year in the data to 2050
    years_extended = list(range(df["Year"].min(), 2051))
    # Calculate the corresponding y values for the line of best fit
    sea_level_extended = [intercept + slope * year for year in years_extended]
    # Plot the line of best fit
    ax1.plot(years_extended, sea_level_extended, color="red", label="Best Fit Line")
    # Add legend
    ax1.legend()
    plt.show()

    # Create second line of best fit

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    # plt.savefig("sea_level_plot.png")
    # return plt.gca()
