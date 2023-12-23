# Project 2 - Frequently asked questions

### What should the report look like?

You will write your report as a Jupyter notebook (use `project-2-report.ipynb`). You will probably have several sections, at least one around each of your key data visualisations. Each figure should have a brief introduction to explain what it represents, and a short paragraph after to explain/interpret the results and conclude.

Look at the **C3** criterion in the marking scheme for what constitutes good presentation.

### Where do I write the code?

You can write code in the notebook (in code cells), or you can also write modules and import them into your notebook if you prefer. Task 3 from Project 1 is a good example of how you could do this.

When you submit your notebook, all figures must be displayed without having to re-run the code cells. You can check this by checking if the figures are visible after you submit to Gradescope.

### I can't upload large data files to GitHub/to my codespace.

Recall from the [Week 8 lecture](https://github.com/pypr23/w08-lecture/blob/main/cats/cats.py) that Pandas can use the URL of a `.csv` file as input, to download the data directly without you having to save the file manually. The same is true for `pd.read_excel()`, as long as the URL points to a `.xlsx` file.

Once you have read the data into a dataframe, you can save a local copy into your current folder, for instance as a `.csv` file. The next time you want to use the data, you can just use `pd.read_csv()` with your local file as input.

For example, let's do this with the "GP practice demographics" data. The link to download the file (found by right-click > "Copy link") is `https://publichealthscotland.scot/media/22255/demographics_2023_q1.xlsx`. It ends with `.xlsx` so we can use `pd.read_excel()` like this:

```python
import pandas as pd

# Download the data directly into a dataframe (this might take a little while!)
gp_data = pd.read_excel('https://publichealthscotland.scot/media/22255/demographics_2023_q1.xlsx', sheet_name=[1, 2])

# I've asked for 2 sheets (Age-Gender and SIMD, indexed 1 and 2 as they're the second and third sheets),
# so this gives me a dictionary with two entries (one per sheet),
# where the key is either 1 or 2, and the value is the corresponding dataframe.

# Save the data locally into CSV files for next time
gp_data[1].to_csv('gp_data_age_gender.csv')
gp_data[2].to_csv('gp_data_simd.csv')
```

Then, the next time we want to use the SIMD data for example, instead of re-downloading it, we can instead do:

```python
import pandas as pd
gp_data_simd = pd.read_csv('gp_data_simd.csv')
print(gp_data_simd.info())
```

To minimise the size of the saved files, you can also already select the parts of the data that you know you'll be interested in before saving the CSV file. For example, getting only the age-gender data for 2023/24 Q1:

```python
selector = gp_data[1]['Quarter'] == '2023/24 (Q1) Apr - Jun'
gp_data_2324_Q1 = gp_data[1].loc[selector]
gp_data_2324_Q1.to_csv('data_2324_Q1.csv')
```

and then to use that later:

```python
gp_data_2324_Q1 = pd.read_csv('data_2324_Q1.csv')
```

Just be careful with the amount of data you are saving -- try not to save too many heavy data files in your codespace.

### Can I use Excel to work on the data (e.g. filter, order, or select sections of the data) before I read it using Python?

**No**. Everything you do with the data must be done using Python, and all the code you use for processing the data must be included in your submission. When marking your projects, a marker must be able to reproduce all of your results exactly as they are, by just running the code in your notebook, starting from the original data files. See section above for examples of how to get started.
