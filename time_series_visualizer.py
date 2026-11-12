
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar


# Import data
df = pd.read_csv(
    'fcc-forum-pageviews.csv',
    parse_dates=['date'],
    index_col='date'
)


# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


# Draw line plot
def draw_line_plot():
    # Create a copy of the data
    df_line = df.copy()

    # Set up the figure
    fig, ax = plt.subplots(figsize=(15, 5))

    # Draw the line chart
    ax.plot(df_line.index, df_line['value'], color='red')

    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save and return image
    fig.savefig('line_plot.png')
    return fig


# Draw bar plot
def draw_bar_plot():
    # Create a copy of the data
    df_bar = df.copy()

    # Extract year and month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Calculate average page views per month for each year
    df_bar = df_bar.groupby(
        ['year', 'month']
    )['value'].mean().unstack()

    # Convert month numbers into month names
    df_bar.columns = [
        calendar.month_abbr[month]
        for month in df_bar.columns
    ]

    # Draw the bar chart
    fig = df_bar.plot(
        kind='bar',
        figsize=(10, 7)
    ).figure

    # Set labels and legend
    ax = fig.axes[0]
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save and return image
    fig.savefig('bar_plot.png')
    return fig


# Draw box plots
def draw_box_plot():
    # Create a copy of the data
    df_box = df.copy()

    # Reset index
    df_box.reset_index(inplace=True)

    # Extract year and month
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Set month order
    month_order = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]

    df_box['month'] = pd.Categorical(
        df_box['month'],
        categories=month_order,
        ordered=True
    )

    # Create two adjacent plots
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(
        x='year',
        y='value',
        data=df_box,
        ax=axes[0]
    )

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise box plot
    sns.boxplot(
        x='month',
        y='value',
        data=df_box,
        order=month_order,
        ax=axes[1]
    )

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save and return image
    fig.savefig('box_plot.png')
    return fig
