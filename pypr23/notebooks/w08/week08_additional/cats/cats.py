import pandas as pd

activity = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-31/cats_uk.csv')
cat_info = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-31/cats_uk_reference.csv')

# print(cat_info.info())
# print(cat_info.columns)
# print(cat_info['animal_id'])

# How many male/female cats?
selector = cat_info['animal_sex'] == 'm'
#  print(cat_info.loc[selector, 'animal_id'])

# Average age of the cats by sex (m/f)
# print(cat_info['age_years'].mean())
print(f'Male cats: {cat_info.loc[selector, "age_years"].mean():.1f}')
print(f'Female cats: {cat_info.loc[~selector, "age_years"].mean():.1f}')
# ~selector
# print(cat_info.info())

# print(selector)
# cat_info.loc[['animal_sex']]

# Plot the trajectory (using lat/long readings) of the oldest
# female cat
oldest_f_cats = cat_info.loc[~selector, ['tag_id', 'age_years']].sort_values(by='age_years', ascending=False)
cat_of_interest = oldest_f_cats.iloc[0]['tag_id']
print(cat_of_interest)
# print(cat_info['animal_id'].head())
# print(cat_info['tag_id'].head())
# input()

# Look up this cat and extract the rows in 'activity'
# and plot their geographical location

#  print(activity.head())

# Extract only the rows corresponding to cat_of_interest
traj = activity.loc[activity['tag_id'] == cat_of_interest, ['location_long', 'location_lat', 'timestamp']]

# Convert 'timestamp' column to actual time stamps we can work with
print(traj['timestamp'].info()) # this is 'object'
traj['timestamp'] = pd.to_datetime(traj['timestamp'])
print(traj['timestamp'].info()) # this is 'datetime64'
# input()

# Make a new column 'elapsed' which is the time intervals between each timestamp and the first one
traj['elapsed'] = traj['timestamp'] - traj.iloc[0]['timestamp']
# print(traj.info())
# input()

# Convert to total number of seconds
traj['elapsed'] = traj['elapsed'].dt.total_seconds()
# print(traj['elapsed'])
# input()
# Adapted from http://chris35wills.github.io/time_elapsed_pandas/
# accessed 13th Nov 2023

# Dynamic plot of the cat's positions
import matplotlib.pyplot as plt
plt.ion()
fig, ax = plt.subplots()

# Set axis limits to the min and max coordinates (to fix the size of the figure)
ax.set(xlim=[traj['location_long'].min(), traj['location_long'].max()], ylim=[traj['location_lat'].min(), traj['location_lat'].max()])

# Set the transparency of each dot to correspond to the time elapsed (so darker dots correspond to later times)
col = 0.1 + traj['elapsed']/traj['elapsed'].max() * 0.9
# print(col)
# input()

# Plot each point separately so they appear sequentially
for i in range(len(traj['location_long'])):
    ax.scatter(traj.iloc[i]['location_long'], traj.iloc[i]['location_lat'], alpha=col.iloc[i], color='k')
    plt.pause(0.1)

# Wait before closing the figure
input('Press Enter to end the program.')
