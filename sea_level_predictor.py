import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], color="blue", label="Data")

    # First line best fit
    # Linear regression
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    # Generate x values from first year to 2050
    years_extended = list(range(df["Year"].min(), 2051))
    # Calculate corresponding y values for line best fit
    sea_level_extended = [intercept + slope * year for year in years_extended]
    # Plot line best fit
    plt.plot(years_extended, sea_level_extended, color="red", label="Best Fit Line")

    # Second line best fit
    # Filter data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]
    # Linear regression filtered data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = (
        linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    )
    # Generate x values from 2000 to 2050
    years_recent_extended = list(range(2000, 2051))
    # Calculate corresponding y values for New line best fit
    sea_level_recent_extended = [
        intercept_recent + slope_recent * year for year in years_recent_extended
    ]
    # Plot new line best fit
    plt.plot(
        years_recent_extended,
        sea_level_recent_extended,
        color="green",
        label="Best Fit Line (2000 onwards)",
    )

    # Labels and title
    plt.title("CSIRO Adjusted Sea Level by Year")
    plt.xlabel("Year")
    plt.ylabel("CSIRO Adjusted Sea Level (inches)")
    plt.legend()

    plt.savefig("sea_level_plot.png")
    return plt.gca()
