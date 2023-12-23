import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

activity = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-31/cats_uk.csv')
cat_info = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-01-31/cats_uk_reference.csv')

# Average age of male and female cats (using groupby)
print(cat_info.columns)
# print(cat_info.groupby('animal_sex').get_group('f'))
# print(cat_info.groupby('animal_sex')['age_years'].mean())
# print(cat_info.groupby('animal_sex')['age_years'].max())

# Hunting depending on age and sex
# sns.relplot(data=cat_info, x='age_years', y='prey_p_month', hue='animal_sex')
# plt.show()

# Distribution of ages
sns.displot(data=cat_info, x='age_years', binwidth=1, col='animal_sex')#multiple='dodge')
plt.show()
