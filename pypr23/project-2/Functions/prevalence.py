import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import datetime as dt
import ipywidgets as widgets
from IPython.display import display
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import geopandas
#import mapclassify
from plotly.subplots import make_subplots
import plotly.express as px

def mc_sim_interactive(df):
  """
  Generating full-interactive monte-carlo simulation

  Args:
      df (pandas.DataFrame): data used to simulate
  """
  np.random.seed(0)
  #slider for selecting how many years want to simulate
  yr = widgets.IntSlider(value=50,max=150, min=10)
  #slider for selecting how many possibilities want to simulate
  tr = widgets.IntSlider(value=100,max=500, min=10, step=5)
  print("Number of Year to simulate")
  display(yr)
  print("Number of Trials")
  display(tr)

  out = widgets.Output()

  def on_value_change(change):
    """
    Function run during changing one of the sliders
    """
    with out:
      out.clear_output()
      pred_year = yr.value
      trials = tr.value

      #Calculating chnages
      changes = 1 + df.iloc[:,0].pct_change()

      #Calculating the necessary parmaeter for simulation
      mu, sigma = changes.mean(), changes.std()
      #Calculating the simulated results
      current = df.iloc[:,0].iloc[-1]
      sim_infected ={"Trail " + str(i) : np.append(current,current * np.random.normal(mu,sigma,pred_year).cumprod()) for i in range(1,trials+1)} #Simulate "pred_year" year data
      sim_infected = pd.DataFrame(sim_infected)
      sim_infected['Year'] = [y for y in range(df.index[-1],df.index[-1]+(pred_year+1))]
      sim_infected = sim_infected.set_index('Year')  

      #Play widget
      play = widgets.Play(value=0,min=0,max=np.shape(sim_infected)[1],step=5,interval=500,description="Press play",disabled=False)
      def f(w):
        plt.plot()
        plt.axhline(current, c='k') #add a black line to visualize current data point
        plt.plot(sim_infected.iloc[0:,:w])
        #Changing the x lable to be more reable by looking at number of year would like to simulate
        if pred_year < 10:
          plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 1 == 0]);
        elif pred_year < 50:
          plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 5 == 0]);
        elif (pred_year < 100):
          plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 10 == 0]);
        else:
          plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 20 == 0]);
        plt.title(f'Monte-Carlo Simulation for Next {pred_year} Years Infectious Population with {w} Possibilities');
        plt.xlabel("Year")
        plt.ylabel("Infectious Population")
        plt.show()
      widgets.interact(f, w=play)

  #Obsering sliders action
  yr.observe(on_value_change, 'value')
  tr.observe(on_value_change, 'value')
  display(out)
  
def mc_sim_semi_interactive(df):
  """
  Generating semi-interactive monte-carlo simulation because the parmeter for simulation need to input by runing the code again

  Args:
      df (pandas.DataFrame): data used to simulate
  """
  np.random.seed(0)
  sns.set()
  #Users Input
  while True:
    yr = input("Prediction Year")
    if yr.strip().isdigit():
      yr = int(yr)
      if yr > 1 and yr <= 100:
        break;
      else:
        print("Number of Prediction Year must be a integer between 2 and 100 (inclusive)!!!")
    else:
      print(f'{yr} is not a appropriate input!It must a integer be between 2 and 100 (inclusive)!!!')

  while True:       
    pre = input("Trials")
    if pre.strip().isdigit():
      pre = int(pre)
      if pre > 0 and pre <= 100:
        break;
      else:
        print("Number of possibilities/lines must be a integer between 1 and 500 (inclusive)!!!")
    else:
      print(f'{pre} is not a appropriate input!It must a integer be between 1 and 500 (inclusive)!!!')
      
  #Calculating optimal step for animation
  if pre > 1:
    CD = [i for i in range(1,pre) if pre%i == 0]
    step = CD[(len(CD)//2)]
  else:
    step = 1
    
  #Calculating chnages
  changes = 1 + df.iloc[:,0].pct_change()

  #Calculating the necessary parmaeter for simulation
  mu, sigma = changes.mean(), changes.std()
  #Calculating the simulated results
  current = df.iloc[:,0].iloc[-1]
  sim_infected ={"Trail " + str(i) : np.append(current,current * np.random.normal(mu,sigma,yr).cumprod()) for i in range(1,pre+1)} #Simulate "yr" year data
  sim_infected = pd.DataFrame(sim_infected)
  sim_infected['Year'] = [y for y in range(df.index[-1],df.index[-1]+(yr+1))]
  sim_infected = sim_infected.set_index('Year')  
  #Play widget 
  play = widgets.Play(value=0,min=0,max=np.shape(sim_infected)[1],step=step,interval=500,description="Press play",disabled=False)
  def f(w):
      plt.plot()
      plt.axhline(current, c='k') #add a black line to visualize current data point
      plt.plot(sim_infected.iloc[0:,:w])
      #Changing the x lable to be more reable by looking at number of year would like to simulate
      if yr < 10:
        plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+yr+1) if y % 1 == 0]);
      elif yr < 50:
        plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+yr+1) if y % 5 == 0]);
      elif (yr < 100):
        plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+yr+1) if y % 10 == 0]);
      else:
        plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+yr+1) if y % 20 == 0]);
      plt.title(f'Monte-Carlo Simulation for Next {yr} Years Infectious Population with {w} Possibilities');
      plt.xlabel("Year")
      plt.ylabel("Infectious Population")
      plt.show()
  return widgets.interact(f, w=play)

def mc_sim_non_interactive(df,pred_year=30,trials = 50):
  """
  Generating non-interactive monte-carlo simulation

  Args:
      df (pandas.DataFrame): data used to simulate
      pred_year (int): how many years would like to predict (e.g. 10 means 10 years from 2023) (Default is 30)
      trials (int) : how many possibilities would like to see (e.g. 50 means 50 lines/possibliities) (Default is 50)
  """
  #Calculating chnages
  changes = 1 + df.iloc[:,0].pct_change()

  #Calculating the necessary parmaeter for simulation
  mu, sigma = changes.mean(), changes.std()
  #Calculating the simulated results
  current = df.iloc[:,0].iloc[-1]
  sim_infected ={"Trail " + str(i) : np.append(current,current * np.random.normal(mu,sigma,pred_year).cumprod()) for i in range(1,trials+1)} #Simulate "pred_year" year data
  sim_infected = pd.DataFrame(sim_infected)
  sim_infected['Year'] = [y for y in range(df.index[-1],df.index[-1]+(pred_year+1))]
  sim_infected = sim_infected.set_index('Year')  
  
  #Visualization
  plt.plot(sim_infected);
  if pred_year < 10:
    plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 1 == 0]);
  elif pred_year < 50:
    plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 5 == 0]);
  elif (pred_year < 100):
    plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 10 == 0]);
  else:
    plt.xticks([y for y in range(df.index[-1]+1,df.index[-1]+pred_year+1) if y % 20 == 0]);  
  plt.title(f'Monte-Carlo Simulation for Next {pred_year} Years Infectious Population with {trials} Possibilities');
  plt.ylabel('Population');
  plt.xlabel('Year');
  plt.axhline(current, c='k') #add a black line to visualize current data point
  plt.show()


def sorting(df, num = 3):
  """
  Sorting the given pandas.DataFrame to return the common diseases (defacult 3)

  Args:
      df (pandas.DataFrame): dataframe would like to figure out the common diseases
      num (int, optional): how many top common disease whant to return (Defaults to 3.)

  Returns:
      List: list of top common diseases, ordered from most common to less common (left to right)
  """
  #Transfoming the given datafreame to be a dictionary so that it is easier to perform sorting
  ty = {}
  for col in df.index:
    ty[col] = df[col]
  top_three_rate = list(dict(sorted(ty.items(), key=lambda item: item[1], reverse=True)).keys())[0:num]
  return top_three_rate

def bar_visual(type,df):
  """
  Generating bar chart for prevalence data

  Args:
      type (String): type of data whant to generate (Counting, Prevalence Rate or Changes)
      df (pandas.DataFrame): related data
  """
  sns.set()
  fig, axes = plt.subplots(1, 2, figsize=(18,10))
  #Initialize Value
  if type=="Patients Counting":
    df_plot1 = df.iloc[:,2:20].copy()
    df = df.iloc[:,1:20].mean().copy()
    df_plot1["Year"] = df_plot1.index
    df_plot1 = pd.melt(df_plot1, id_vars="Year", var_name="Diseases", value_name="Infectious Population")
    df_plot1["Diseases"]= df_plot1["Diseases"].str.replace("PatientCount_","")
    title_overall = "Number of People Diagnosed with Different Diseases from 2018 to 2023"
    plot2_ylabel = "Mean Population"
    sns.barplot(df_plot1, y="Diseases", x = "Infectious Population", orient = "h", hue="Year", ax=axes[0]).set(title=title_overall);
  elif type=="Change":
    df_plot1 = df.iloc[:,21:40].copy()
    df = df.iloc[:,20:39].mean().copy()
    df_plot1["Year"] = df_plot1.index
    df_plot1 = pd.melt(df_plot1, id_vars="Year", var_name="Diseases", value_name="Changes")
    df_plot1["Diseases"]= df_plot1["Diseases"].str.replace("Change_","")
    title_overall =  "Changes with Different Diseases from 2018 to 2023"
    plot2_ylabel = "Average Changes"
    sns.barplot(df_plot1, y="Diseases", x = "Changes", orient = "h", hue="Year", ax=axes[0]).set(title=title_overall);
  elif type=="Rate":
    df_plot1 = df.iloc[:,40:].copy()
    df = df.iloc[0:,39:].mean().copy()
    df_plot1["Year"] = df_plot1.index
    df_plot1 = pd.melt(df_plot1, id_vars="Year", var_name="Diseases", value_name="Rates")
    df_plot1["Diseases"]= df_plot1["Diseases"].str.replace("Rate_","")
    title_overall = "Prevalence Rate with Different Diseases from 2018 to 2023"
    plot2_ylabel = "Average Prevalence Rate"
    sns.barplot(df_plot1, y="Diseases", x = "Rates", orient = "h", hue="Year", ax=axes[0]).set(title=title_overall);

  #Plot2
  top_three_rate = sorting(df)
  top = df[top_three_rate].copy()
  #Making the display be more reable
  if type=="Count":
    top_three_rate = [i.replace("PatientCount_","") for i in top_three_rate]
  elif type=="Change":
    top_three_rate = [i.replace("Change_","") for i in top_three_rate]
  elif type=="Rate":
    top_three_rate = [i.replace("Rate_","") for i in top_three_rate]

  #Bar chart for showing three most common diseases on averge from 2018 to 2023
  sns.barplot(x=top_three_rate, y = top, orient = "v", ax=axes[1]).set(title=f"The Averagly 3 Common Diseases from 2018 to 2023 ({plot2_ylabel})", ylabel= plot2_ylabel, xlabel= "Diseases");
  plt.xticks(rotation=45)
  plt.suptitle(f'Bar Charts for {type}')
  plt.show()


def dist_visual(diseases,male,female, row_plot =3):
  """
  Generating a distribution plot for investigeting the relation between generder and prevalence rate

  Args:
      diseases (String): interested diseases
      male (pandas.DataFrame): male data
      female (pandas.DataFrame): female data
      row_plot (int, optional):how many plot want to show per row (Defaults to 3)
  """
  
  start = 0
  #Male Data
  prevalence_data_male = male.copy()
  #Female Data
  prevalence_data_female = female.copy()
  #Caculating there show be hopw many row
  plot_num_list = [row_plot for i in range(len(diseases)// row_plot)]
  if sum(plot_num_list) < len(diseases):
    plot_num_list.append(len(diseases)-sum(plot_num_list))
  #Plotting
  for plot_num in plot_num_list:
    fig, axes = plt.subplots(1,row_plot,figsize=(20,8))
    ax_index = 0
    for i in range(start,start+row_plot):
      if i < len(diseases):
        #Data cleaning for male data
        prevalence_data_age_male = prevalence_data_male[prevalence_data_male['Age']!="All"].copy()
        prevalence_data_age_male = prevalence_data_age_male.groupby(['Age']).mean(numeric_only = True)
        prevalence_data_age_count_male = prevalence_data_age_male.iloc[:,40:].copy()
        prevalence_data_age_count_male['Age'] = prevalence_data_age_count_male.index
        df_plot_male = pd.melt(prevalence_data_age_count_male, id_vars="Age", var_name="Diseases", value_name="Prevalence Rates")
        df_plot_male["Diseases"]= df_plot_male["Diseases"].str.replace("Rate_","")
        df_plot_male["Gender"] = "Male"

        #Data cleaning for female data
        prevalence_data_age_female = prevalence_data_female[prevalence_data_female['Age']!="All"].copy()
        prevalence_data_age_female = prevalence_data_age_female.groupby(['Age']).mean(numeric_only = True)
        prevalence_data_age_count_female = prevalence_data_age_female.iloc[:,40:].copy()
        prevalence_data_age_count_female['Age'] = prevalence_data_age_count_female.index
        df_plot_female = pd.melt(prevalence_data_age_count_female, id_vars="Age", var_name="Diseases", value_name="Prevalence Rates")
        df_plot_female["Diseases"]= df_plot_female["Diseases"].str.replace("Rate_","")
        df_plot_female["Gender"] = "Female"

        #Merging male and female data
        df_plot = df_plot_male.merge(df_plot_female, how='outer')
        #Plotting the distribution graph
        plot = sns.barplot(df_plot[df_plot["Diseases"]==diseases[i]], y = "Prevalence Rates", x= 'Age', ax=axes[ax_index], hue='Gender', palette=['blue','red']).set(title=f"Distribution of Prevalence Rates of {diseases[i]}");
        axes[ax_index].tick_params(axis='x', rotation=45)
      else:
        #remove the redundant plot
        axes[ax_index].axis('off')
      ax_index += 1
    start += plot_num

def map_visual(df, shape_df, diseases, row_plot =3):
  """
  Generating a map plot for investigeting the relation between Board divison and prevalence rate

  Args:
      df (pandas.DataFrame): related dataframe
      diseases (String): interested disease
      row_plot (int, optional): how many plot want to show per row (Defaults to 3)
  """
  start = 0
  #Caculating there show be hopw many row
  plot_num_list = [row_plot for i in range(len(diseases)// row_plot)]
  if sum(plot_num_list) < len(diseases):
    plot_num_list.append(len(diseases)-sum(plot_num_list))
  #Plotting
  for plot_num in plot_num_list:
    fig, axes = plt.subplots(1,row_plot,figsize=(20,8))
    #Counting the subplot index
    ax_index = 0

    for i in range(start,start+row_plot):
      if i < len(diseases):
        df_plot = df[df['Diseases']==diseases[i]].copy()
        geo_df_prevalence = shape_df.join(df_plot)
        geo_df_prevalence.plot('Prevalence Rates', legend=True, cmap='YlOrRd', legend_kwds={"label":"Prevalence Rate"}, ax=axes[ax_index], missing_kwds={'color': 'white', 'edgecolor': 'red','hatch': '///','label': 'Missing values'}).set(title=f"Location Distribution \n({diseases[i]})")
      else:
        #remove the redundant plot
        axes[ax_index].axis('off')
      ax_index += 1
    start += plot_num
