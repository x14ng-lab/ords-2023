import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd

def draw_charts(top_n, start_month, all_data, BNF_ref, filtered_dataset, section_count):
    '''
    Draws a pie chart and a bar chart side by side to show the demand proportion and
    frequency of the top n most in-demand drug categories in a selected time period.

    Inputs:
    - top_n (int): Number of top demanded drug categories to display.
    - start_month (str): The starting month of the data, used for filtering and 
        displaying the time range.
    - all_data (pd.DataFrame): The complete dataset of drug demand information.
    - BNF_ref (pd.DataFrame): The BNF reference.
    - filtered_dataset
    - section_count
    '''
    # Convert the user input start month to integer for later comparison
    start_month_int = int(start_month)

    # Count the occurrences of each BNF code in the filtered dataset
    bnf_code_counts = filtered_dataset['BNFCode'].value_counts()

    # Calculate the total count of all sections as denominator
    total_count = section_count.sum()

    # Select the top n BNF sections based on the input, other_count is the sum of the rest of drugs
    top_sections = section_count.head(top_n)
    other_count = total_count - top_sections.sum()

    # Prepare labels and sizes for the ple and bar charts
    labels = top_sections.index.tolist()
    sizes = top_sections.tolist()
    percentages = [(size / total_count) * 100 for size in sizes]

    # Set up the overall figure size as we want to group two chart in one graph
    plt.figure(figsize=(18, 8))

    # Createthe first chart: a pie chart
    plt.subplot(1, 2, 1) # Set the position for the pie chart

    # Define a color scheme for the group graph. Each color corresponds to a drug type, which is the same in both pie charts and bar charts
    colors = plt.cm.GnBu(np.linspace(1, 0, len(top_sections) + 1))  # +1 for 'Others' section

    # Customizing the pie chart appearance
    explode = [0.1] + [0] * (len(sizes) - 1) + [0.1]  # Include 'Others' section
    pie_patches, _ = plt.pie(sizes + [other_count], explode=explode, colors=colors, 
                             startangle=140, shadow=True)

    # Set the title for the pie chart, in order to have a better layout, we choose to use plt.text rather than plt.title.
    plt.text(-1.1, 1.4, 'Proportion of Drug Demand by Category', fontsize=16, ha='left', va='top')
    plt.axis('equal') #Make sure we have a pie chart

    # Create the second chart: a bar chart
    plt.subplot(1, 2, 2)  # Set the Position
    
    # Set the counts as the y values
    counts = top_sections.tolist()

    # Customizing the bar chart appearance
    bars = plt.bar(range(len(labels)), counts, color=colors[:-1])  # Exclude 'Others' Section
    plt.title(f'Top {top_n} Most In-Demand Drug Categories in {start_month}', fontsize=20)
    plt.ylabel('Frequency of drug sales', fontsize=12)

    # Remove x-axis labels for better appearance
    plt.xticks([])

    # Set up the legend with labels showing percentages and counts ('Others' shows only percentage)
    combined_labels = [f'{label} - {percentage:.1f}% - {count} times of demand' for label, percentage, count in zip(labels, percentages, counts)]
    combined_labels.append(f'Others - {100 - sum(percentages):.1f}%')  # Include only percentage for 'Others'
    plt.legend(pie_patches, combined_labels, loc='best', bbox_to_anchor=(1.15, 1))

    # Adjust layout for better appearance
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Display the charts
    plt.show()


def draw_least_demand_chart(least_demand_sections, least_m, start_month):
    '''
    Draws a horizontal bar chart displaying the least demanded medicine categories in a selected period.

    Inputs:
    least_demand_sections (Series/DataFrame): Contains the least demanded medicine categories and their frequencies.
    least_m (int): The number of least demanded medicine categories to display.
    start_month (str): The starting month of the data, used for displaying the time range in the chart title.
    '''
    # Plotting the horizontal bar chart for the least demanding drugs
    plt.figure(figsize=(12, 8))
    bars = plt.barh(least_demand_sections.index, least_demand_sections.values, color=plt.cm.spring(np.linspace(1, 0, least_m)))

    # Add data labels and customize style
    for bar in bars:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, 
                 f'{int(bar.get_width())}', 
                 va='center', ha='left', fontsize=10, color='black')

    # Set title and labels
    plt.title(f'Least Demanding {least_m} Medicine Categories from {start_month}')
    plt.xlabel('Frequency with which the Drug is Requested')
    plt.ylabel('Category of Drug')

    # Display the plot
    plt.show()


def unify(input_df):
    '''
    Load a prescription data and unify its column headers with the BNF prescription reference.

    Inputs:
    - input_df (pd.DataFrame): The prescription data to be processed.

    Outputs:
    - output_df (pd.DataFrame): The prescription data after unification.
    '''
    # Check that the input arguments are valid
    if not isinstance(input_df, pd.DataFrame):
        raise TypeError("Please enter a dataframe of the prescription data.")
    
    # Unify the column headers
    column_header_renames = {
        'BNFItemCode': 'BNF Presentation Code',
        'BNFItemDescription': 'BNF Presentation',
        'HBT': 'HBCode'
    }
    output_df = input_df.rename(columns=column_header_renames, inplace=False)

    # Lower case all the strings in the 'BNF Presentation' column
    output_df['BNF Presentation'] = output_df['BNF Presentation'].str.lower()

    return output_df


def filter(prescribing_data, BNF_Section_Code = ''):
    '''
    Filter out the data of a specific kind of prescription from the prescription data.

    Inputs:
    - prescribing_data (pd.DataFrame): The prescription data to be precessed.
    - BNF_Section_code (str): The BNF Section Code to filter by, e.g., the 
        BNF Section Code for Hypertension and heart failure is '0205'.

    Outputs:
    - prescribing_data_disease (pd.DataFrame): A new dataframe that only contains 
        the data of the specified prescription.
    '''
    # Check that the input arguments are valid
    if not isinstance(prescribing_data, pd.DataFrame):
        raise TypeError("Please enter a dataframe of the prescription data.")
    if not isinstance(BNF_Section_Code, str):
        raise TypeError("Please enter the BNF Section Code in string format.")
    
    # Filter out the data of the specified prescription
    prescribing_data_disease = prescribing_data[prescribing_data['BNF Presentation Code'].str.startswith(BNF_Section_Code)]
    
    return prescribing_data_disease


def groupsum(prescribing_data, gdf, col_to_groupby, col_to_sum):
    '''
    Sum a specified column for each group defined by another column,
    and then merge this summary with a given GeoDataFrame on a common field.

    Inputs:
    - prescribing_data (pd.DataFrame): The prescription data to be precessed.
    - gdf (GeoDataFrame): The GeoDataFrame to merge the summary data with 
        (normally a shape file).
    - col_to_groupby (str): The header of the column to group by in the prescription data.
    - col_to_sum (str): The header of the column to sum within each group.

    Outputs:
    - merged_gdf (GeoDataFrame): The result of merging the summary data with the GeoDataFrame.
    '''
    # Check that the input arguments are valid
    if not isinstance(prescribing_data, pd.DataFrame):
        raise TypeError("Please enter a dataframe of the prescription data.")
    if not isinstance(gdf, gpd.GeoDataFrame):
        raise TypeError("Please enter a GeoDataFrame of the shape file data.")
    if not isinstance(col_to_groupby, str) or not isinstance(col_to_sum, str):
        raise TypeError("Please enter the header in string format.")
    if not all(col in prescribing_data.columns for col in [col_to_groupby, col_to_sum]):
        raise ValueError("Please make sure you type the column header correctly.")
    
    # Sum the specified column for each group
    prescribing_data_groupsum = prescribing_data.groupby(col_to_groupby)[col_to_sum].sum().reset_index()

    # Merge the summary data with the GeoDataFrame on the common field
    merged_gdf = gdf.merge(prescribing_data_groupsum, left_on=col_to_groupby, right_on=col_to_groupby, how='left')

    return merged_gdf


def flt_dict(prescribing_data, bnf_code_dict):
    '''
    Filter out the prescription DataFrames based on the BNF code dictionary 
    that should be previously defined and store them in a new dictionary.

    Inputs:
    - prescribing_data (pd.DataFrame): The prescription data to be processed.
    - bnf_code_dict (dict): The dictionary of BNF codes of the diseases which 
        we want to investigate.

    Outputs:
    - flt_dictionary (dict): The dictionary of the filtered prescription DataFrames.
    '''
    # Check that the input arguments are valid
    if not isinstance(prescribing_data, pd.DataFrame):
        raise TypeError("Please enter a dataframe of the prescription data.")
    if not isinstance(bnf_code_dict, dict):
        raise TypeError("Please enter a dictionary of the BNF codes of the diseases you want to investigate.")
    
    # Initialise a dictionary to store the filtered DataFrames
    flt_dictionary = {}

    # Iterate through the BNF code dictionary that previously defined
    for disease, bnf_code in bnf_code_dict.items():
        flt_dictionary[disease] = filter(prescribing_data, bnf_code)

    return flt_dictionary


def gdf_dict(prescibing_data, prescribing_data_dict, gdf, col_to_groupby, col_to_sum):
    '''
    Obtain the processed GeoDataFrames based on the filtered prescription
    DataFrames dictionary by "groupsum" and store them in a new dictionary.

    Inputs:
    - prescribing_data (pd.DataFrame): The prescription data to be precessed.
    - prescribing_data_dict (dict): The dictionary of the filtered prescription DataFrames.
    - gdf (GeoDataFrame): The GeoDataFrame to merge the summary data with 
        (normally a shape file).
    - col_to_groupby (str): The header of the column to group by.
    - col_to_sum (str): The header of the column to sum within each group.

    Outputs:
    gdf_dictionary (dict): The dictionary of the processed GeoDataFrames.
    '''
    # Check that the input arguments are valid
    if not isinstance(prescribing_data_dict, dict):
        raise TypeError("Please enter a dictionary of the filtered prescription data.")
    
    # Initialise a dictionary to store the processed GeoDataFrames
    gdf_dictionary = {}

    # Iterate through the filtered prescription dfs dictionary
    for disease, prescribing_data in prescribing_data_dict.items():
        gdf_dictionary[disease] = groupsum(prescribing_data_dict[disease], gdf, col_to_groupby, col_to_sum)

    return gdf_dictionary


def plot_single_choropleth(gdf, column, cmap, title='', figsize=(6, 6)):
    '''
    Plot a choropleth map for a single GeoDataFrame.

    Inputs:
    - gdf (GeoDataFrame): The GeoDataFrame to be plotted.
    - column (str): The column whose values are used to assign colors.
    - cmap (str): Color for the maps.
    - title (str): The title of the plot.
    - figsize (tuple): The figure size for the plot, specified as (width, height). Default is (6, 6).

    Outputs:
    None: The function creates and shows the choropleth plot but does not return any value.
    '''
    # Check that the input arguments are valid
    if not isinstance(gdf, gpd.GeoDataFrame):
        raise TypeError("The provided data is not a GeoDataFrame.")
    if not isinstance(column, str):
        raise TypeError("Please enter the column header in string format.")
    if column not in gdf.columns:
        raise ValueError("Please make sure you type the column header correctly.")
    if not isinstance(cmap, str):
        raise TypeError("Please enter the color in string format.")

    # Calculate global min and max values for column value in the GeoDataFrame
    min_value = gdf[column].min()
    max_value = gdf[column].max()

    # Set up the plotting arguments
    plot_kwargs = {
        'column': column,
        'cmap': cmap,
        'legend': True,
        'vmin': min_value,
        'vmax': max_value,
        'legend_kwds': {"label": column},
        'missing_kwds': {
            'color': 'lightgrey',
            'edgecolor': 'red',
            'hatch': '///',
            'label': 'Missing values'
        }
    }

    fig, ax = plt.subplots(figsize=figsize)
    gdf.plot(ax=ax, **plot_kwargs)
    ax.set_title(title)
    plt.show()


def plot_multiple_choropleths(gdf_dict, column, cmap, figsize=(20, 8)):
    '''
    Plot choropleth maps for multiple GeoDataFrames provided in a dictionary.

    Inputs:
    - gdf_dict (dict): A dictionary of GeoDataFrames where keys are names 
        of the diseases and values are the corresponding GeoDataFrames.
    - column (str): The column whose values are used to assign colors.
    - cmap (str): Color for the maps.
    - figsize (tuple): The figure size for the subplot grid, specified 
        as (width, height). Default is (20, 8).

    Outputs:
    None: The function creates and shows the choropleth plots but does not return any value.
    '''
    # Check that the input arguments are valid
    if not isinstance(gdf_dict, dict) or not all(isinstance(gdf, gpd.GeoDataFrame) for gdf in gdf_dict.values()):
        raise TypeError("gdf_dict must be a dictionary with GeoDataFrame values.")
    if not isinstance(column, str):
        raise TypeError("Column name must be a string.")
    if not all(column in gdf.columns for gdf in gdf_dict.values()):
        raise ValueError("The specified column does not exist in one or more GeoDataFrames.")
    if not isinstance(cmap, str):
        raise TypeError("Color map name must be a string.")

    # Calculate global min and max values across all GeoDataFrames in the dictionary
    min_value = min(gdf[column].min() for gdf in gdf_dict.values())
    max_value = max(gdf[column].max() for gdf in gdf_dict.values())

    # Set up the plotting arguments
    plot_kwargs = {
        'column': column,
        'cmap': cmap,
        'legend': True,
        'vmin': min_value,
        'vmax': max_value,
        'legend_kwds': {"label": column},
        'missing_kwds': {
            'color': 'lightgrey',
            'edgecolor': 'red',
            'hatch': '///',
            'label': 'Missing values'
        }
    }

    # Determine the layout for subplots
    nrows = 1 if len(gdf_dict) <= 3 else 2  # Adjust rows for more than 3 plots
    ncols = min(len(gdf_dict), 3)  # Maximum 3 columns
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize)

    # Ensure axes is always iterable, even if there's only one subplot
    if not isinstance(axes, np.ndarray):
        axes = [axes]

    # Iterate and plot each GeoDataFrame
    for (disease, gdf), ax in zip(gdf_dict.items(), axes):
        gdf.plot(ax=ax, **plot_kwargs)
        ax.set_title(f'{disease} Prescriptions')

    # Hide any unused subplots
    for i in range(len(gdf_dict), len(axes)):
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()

