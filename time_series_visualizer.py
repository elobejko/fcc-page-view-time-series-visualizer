import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col = 'date', parse_dates = True)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975) )]


def draw_line_plot():
    # Draw line plot

  fig, ax = plt.subplots(figsize = (12, 3)) 
  plt.plot(df, color = 'red')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  
  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    tmp = df.copy()
    tmp.reset_index(inplace = True)
    df_bar = pd.DataFrame()
    df_bar['year'] = [d.year for d in tmp.date]
    df_bar['month'] = [d.strftime('%B') for d in tmp.date]
    df_bar['value'] = tmp['value']
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.reset_index(level=['year','month'])
  
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(8,8))
    ax = sns.barplot(x = 'year', y = 'value', hue = 'month', hue_order = months, data = df_bar, palette = 'dark')
    ax.set(xlabel='Years', ylabel = 'Average Page Views')
    ax.legend(loc='upper left', title ='Months')
    fig = ax.get_figure()
     
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize = (14,5))
    sns.boxplot(ax = axes[0], x="year", y="value", data=df_box).set(xlabel="Year", ylabel="Page Views")
    sns.boxplot(ax = axes[1], x="month", y="value", data=df_box, order = months).set(xlabel="Month", ylabel="Page Views")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
