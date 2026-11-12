
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Calculate line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # Generate x values through 2050
    years = pd.Series(range(1880, 2051))

    # Plot first line of best fit
    ax.plot(
        years,
        slope * years + intercept,
        color='red',
        label='Best fit line (1880-2050)'
    )

    # Select data from year 2000 onward
    recent_df = df[df['Year'] >= 2000]

    # Calculate second line of best fit
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_df['Year'],
        recent_df['CSIRO Adjusted Sea Level']
    )

    # Generate x values for recent trend
    recent_years = pd.Series(range(2000, 2051))

    # Plot second line of best fit
    ax.plot(
        recent_years,
        slope_recent * recent_years + intercept_recent,
        color='green',
        label='Best fit line (2000-2050)'
    )

    # Set labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    ax.legend()

    # Save and return the plot
    fig.savefig('sea_level_plot.png')
    return fig
