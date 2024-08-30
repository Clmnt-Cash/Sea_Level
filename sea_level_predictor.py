import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df)

    # Create scatter plot
    fig, ax1 = plt.subplots(figsize=(10, 6))
    ax1.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data")
    # Adding title and labels

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

    # Create second line of best fit
    # Filter the data to include only years from 2000 onwards
    df_recent = df[df["Year"] >= 2000]
    # Perform linear regression on the filtered data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = (
        linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    )
    # Generate x values from 2000 to 2050
    years_recent_extended = list(range(2000, 2051))
    # Calculate the corresponding y values for the new line of best fit
    sea_level_recent_extended = [
        intercept_recent + slope_recent * year for year in years_recent_extended
    ]
    # Plot the new line of best fit (from 2000 onwards)
    ax1.plot(
        years_recent_extended,
        sea_level_recent_extended,
        color="green",
        label="Best Fit Line (2000 onwards)",
    )

    # Labels and title
    ax1.set_title("CSIRO Adjusted Sea Level by Year")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("CSIRO Adjusted Sea Level (inches)")
    ax1.legend()

    plt.savefig("sea_level_plot.png")
    return plt.gca()
