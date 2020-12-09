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
    df.reset_index(inplace = True)
    #df["month"] = df.index.month
    #df["year"] = df.index.year
    df_bar = pd.DataFrame()
   # 
    df_bar['year'] = [d.year for d in df.date]
    df_bar['month'] = [d.strftime('%b') for d in df.date]
    df_bar['value'] = df['value']
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.reset_index(level=['year','month'])
    print(df_bar.info())  
    print(df_bar.head())
    
  
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot

    fig, ax = plt.subplots(figsize=(10,10))
    ax = sns.barplot(x = 'year', y = 'value', hue = 'month', data = df_bar)
    ax.set(xlabel='Years', ylabel = 'Average Page Views')
    #ax.legend(months)
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

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    #fig.savefig('box_plot.png')
    #return fig
