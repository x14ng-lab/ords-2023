# Project 2: Public health in Scotland

The Scottish government publishes a range of data related to public health across the country. In this project, you will use data related to GP practices to investigate relevant questions related to Scottish public health.

(["GP" means "general practitioner"](https://www.nhsinform.scot/gp) -- in the UK, the GP practice is where you go when you need to "go to the doctor", when your medical problem is not an emergency.)

You will get started on the project during the **Week 8 workshop**.

---

## Goal and structure

The goal of this project is for you to present a **coherent and well-coded investigation** into some aspects of the dataset. You should do this in the Jupyter notebook called **`project-2-report.ipynb`**, which will contain your code, as well as any results and visualisations. You should also use Markdown cells to structure the notebook, describe your investigations, and present/explain your results.

You should aim for approximately **2-4 main data visualisations** overall, each showing a key result of your investigation. These could potentially consist of multiple plots or smaller visualisations; you may also wish to display intermediate plots or results to demonstrate the processing of your data.

This project is an **open-ended** task, so you should come up with your **own ideas** to analyse the dataset and extract useful information or interesting facts. Some ideas of questions you might address in your analysis will be given in the section "Some ideas to get you started"; they are a guide to some things you could think about, and should hopefully give you an idea about the scope of what's required for each main result/section, but...

#### you don't need to answer them all, and you are strongly encouraged to answer questions that are not listed.

When you are presenting your investigation of each question, be sure to make a coherent discussion for each task (using Markdown, maths as appropriate and code cells) -- it does not need to be long, but it should be clear enough to explain the problem and interpret your results.

In particular, since you are working as a group, some work will be needed to combine all of the code and writing that you each contribute into the submitted notebook -- this is something that you should plan to do, and the quality of **presentation** will be marked. Note, in particular, that this is a **group project, and not a collection of small individual projects** -- your report should be coherent, and evidence that you have collaborated effectively.

---

## Data

The key datasets provided for this project are:

- The ["GP demographics data"](https://publichealthscotland.scot/publications/general-practice-demographics-data-visualisation/general-practice-demographics-data-visualisation-up-to-1-july-2023/) file is the main dataset you will work with. It is an `.xlsx` file containing a demographic breakdown of how many patients were registered in each GP practice across the country, in each quarter since 2018, separated by age group, sex, and deprivation [using the Scottish Index of Multiple Deprivation](https://www.gov.scot/collections/scottish-index-of-multiple-deprivation-2020/).
- The [disease prevalence](https://publichealthscotland.scot/publications/general-practice-disease-prevalence-data-visualisation/general-practice-disease-prevalence-visualisation-27-june-2023/) datasets are all `.xlsx` files, containing yearly information on how many patients had different diseases, separated by age group. The "Practice - " files show this information for each GP practice, so this will be easiest to cross-reference with the GP demographics data, particularly if you want to focus on a particular city/region/neighbourhood/other subset of GP practices.
- The ["Prescriptions In The Community"](https://www.opendata.nhs.scot/dataset/prescriptions-in-the-community) datasets (to use together with the [BNF item code reference](https://applications.nhsbsa.nhs.uk/infosystems/data/showDataSelector.do?reportId=126), showing the reference codes for different types of medication -- login as Guest to download) are monthly datasets showing all medication prescriptions made by every GP practice in a given month. These are large datasets (approx. 100MB each) -- **please don't download more than 1 or 2 into your codespace at once.**
    - If you'd like to look at all types of prescription, pick one month and use that dataset only.
    - If you'd like to look at particular types of prescription (for instance, heart medication), and how this changes over time, here's a suggestion for how to proceed:
        - Download one data file.
        - Extract only the information you need from that data file, using the BNF item codes and/or a particular subset of GP practices.
        - Save the smaller dataframe to a CSV file.
        - Delete (manually) the original data file from your codespace, and use your smaller file for the rest of your analysis.
        - Repeat for every month for which you need data.

You are also free to download and use more related data from other sources to complement your investigation if you wish. For example:

- [GP practice contact details](https://publichealthscotland.scot/publications/general-practice-list-size-and-demographics-information/) includes postcodes of the different GP practices; you can use this together with this [postcode reference list](https://www.nrscotland.gov.uk/statistics-and-data/geography/our-products/scottish-postcode-directory/2023-2) which, in particular, gives latitudes and longitudes for the centre of each postcode. This will be useful if you plan to present data on a map.
- [Number of GPs by local authority (Table 3)](https://publichealthscotland.scot/publications/general-practice-gp-workforce-and-practice-list-sizes/general-practice-gp-workforce-and-practice-list-sizes-2012-2022/) gives information about the number of GPs, over the years 2012-2022, worked in different local areas. There is no breakdown by GP practice, unfortunately, but you can use this data if you are looking at a specific city or region, for instance.
- [Practice population by urban and rural areas (Table 8)](https://publichealthscotland.scot/publications/general-practice-gp-workforce-and-practice-list-sizes/general-practice-gp-workforce-and-practice-list-sizes-2012-2022/) gives information on how many patients registered in each GP practice live in an urban or a rural area (to different degrees of what is defined as "urban" or "rural").
- [Public Health Scotland](https://www.opendata.nhs.scot/organization) publishes plenty of other health datasets.
- The [opendata.scot portal](https://opendata.scot/datasets/?category=health-and-social-care) contains a lot of datasets published by different public bodies in Scotland (the government, city councils, etc.).

In any case, make sure the data is licensed in a way which allows you to use it!

### Reading XLSX files with pandas

We've seen the `pd.read_csv()` function to read CSV files into dataframes. Pandas also has a [`pd.read_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel) function to read data from Excel spreadsheets into dataframes. Consult the documentation to find out how to use it. For example, some of the data in `.xlsx` files is structured over multiple sheets in the same document, which `pd.read_excel()` can deal with.

---

## Some ideas to get you started

Generally speaking, it's probably a good idea to **limit the scope of your report**, in space and in time. Here are a few examples of what you could consider:

- You could focus your investigation on a particular NHS board (these correspond to broad regions of Scotland), or a single city, or even a small number of practices.
- You could focus on a particular sub-group of patients -- for example a given age group or gender.
- You could choose some variables in the data sets, and investigate how these change over time -- e.g. looking at long-term changes over the months/years, or seasonal changes.
- You could focus on a particular type of health issue, looking at the prescriptions or prevalence datasets, for example.

Please note that **this is not a Statistics or data science course**, but a Python programming course. For example, you can produce an excellent report "only" with carefully selecting and aggregating relevant data and producing some (non-trivial) visualisations of different aspects, perhaps with some basic statistics/aggregation. The important thing in your report is that you can use your Python skills to good effect to show interesting things about the data.

Here are some example questions your report could address. Again, **you should not cover all of them** (aim for 2-4 main results!), and you are certainly encouraged to come up with your own questions too. The important thing is that your report is **coherent and well-presented**, that your **code** works as intended, and that you explore some of the aspects of this dataset in reasonable depth, presenting results in a way which help you answer relevant questions or queries. If you investigate 1 or 2 of these with sufficient depth, this should be plenty enough for a good report.

- You could use GP practice registration data to map population age across Scotland, or within a local area. For example, can you identify regions/cities/neighbourhoods with a lot of families with young children, elderly people, or students?
- Using GP workforce data, can you say something about accessibility of GP services/doctor-to-patient ratios, e.g. in different areas or over the years?
- Can you highlight any significant/interesting differences between GP practices with a higher or lower proportion of different SIMD deciles?
- Investigate the prevalence of a particular disease, and how this has evolved over the years.
- Can you find evidence of certain diseases having a seasonal pattern?
- Do different diseases predominantly affect people of different age groups?
- Can you highlight any significant/interesting differences between urban and rural areas?


---

### Working on your project

During the Week 8 workshop, or as soon as possible after this, you should discuss with your group and come up with a **plan**.

- **Pair-program** as much as possible! You will likely be much more productive if you have another person to bounce ideas off of about what to investigate or how to present results, and help each other solve problems. You can do this in pairs, you can mix up pairs, you can even do "group programming" sessions with one driver and 2-3 navigators if that's helpful.
- Schedule quick **code reviews** for each other, to help each other stay on track and write better code.
- Use your shared GitHub repo to **collaborate**.
    - Every time you start working on the project, start by **pulling** the latest version from GitHub into your codespace.
    - Then, as you work, **commit** your changes regularly. When you are done for the day (or even before that), **push** your work to the GitHub repo to share it with your team.
- To **submit** your project, the process will be the same as for Project 1: first, **push** your final version (ready for submission) **to your GitHub repo**, then submit your repo to Gradescope. Gradescope will be set up so that one person can submit the report on behalf of their group.

---

### Packages

The same packages as usual are available in your codespaces -- these are:

```
python
numpy
scipy
matplotlib
pandas
seaborn
jupyter
ipykernel
ipywidgets
pip
```

Beyond these, you can also use other packages or libraries that you find useful. If there are any other packages you want to use:

- Find out the name of the package in the installation instructions.
- Add the name of the package as a new line to the file `requirements.txt`.
- In the terminal at the bottom of your codespace, run the command `pip install -r requirements.txt`.

This should install any new packages you've added to `requirements.txt` to your codespace permanently. (If you create a new, separate codespace however, you'll need to run the command again.)

Here are a couple of packages you might find useful:

- If you choose to visualise anything on a map, packages like [folium](https://python-visualization.github.io/folium/) or [geopandas](https://geopandas.org/) might be useful.
- If you fancy making interactive visualisations, with things like toggle buttons or sliders, you could look into [IPython widgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html). (This is how the "Solution" buttons are made in your tutorial notebooks, for example -- note that this is already installed in your codespaces.)
- Beyond matplotlib and seaborn, other popular plotting/visualisation libraries include [bokeh](https://docs.bokeh.org/en/latest/docs/gallery.html) and [plotly](https://plotly.com/python/).
- For those of you with an interest/experience in machine learning who would like to use this in your project, [Scikit-learn](https://scikit-learn.org/stable/) has plenty of useful functions for supervised and unsupervised learning.

For example, if you wanted to use folium and Scikit-learn, you would add the following to `requirements.txt`, then run the terminal command:

```
folium
scikit-learn
```

---

### Marking scheme

Your project will be marked on 4 criteria:

- Technical proficiency (16 marks)
- Amount of work done and depth of investigation (12 marks)
- Presentation and cohesion of the report (8 marks)
- Code comments, docstrings, code style, and readability (4 marks)

The detailed marking scheme will be available in your repositories under `project-2-markingscheme.md`.

### Peer moderation of group contributions

When submitting your group project, we will also ask each student to complete a short peer moderation form. You will be asked to rate each of your group members' contributions to the project, as well as your own contributions, on 3 different aspects:

- Engagement and communication: attendance and contribution to meetings, reliability, communication between meetings, and contributions to positive and supportive group dynamics.
- Effective collaboration and good will: overall efforts to contribute to the project as a team member, and to seek and provide feedback to/from other team members. Keep in mind that different students have different strengths.
- Quality of contribution: overall technical quality of the contribution of an individual to the project.

The results will inform the marking, together with the information gathered by your tutors over the next few weeks during the workshops. Each report will first be marked on its own merits, for the whole group; but if significant evidence of unequal contributions to the project is found, then grades may be adjusted for individual group members.


### Providing references

Most of the content of your submission must be **authored by your group**. That being said, you may use any code from the course material (e.g. workshop tasks, tutorial sheets, videos), without citing it.

You may also use **small pieces of code** (a few lines max at a time) that you found elsewhere -- e.g. examples from the documentation, a textbook, forums, blogs, etc... You may use this code *verbatim* (i.e. almost exactly as you found it), or adapt it to write your own solution.

A programming assignment is just like any other academic assignment -- and therefore, **you must provide a citation for any such code**, whether you use it *verbatim* or adapt it. To do so, include a code comment at the start of your script or notebook cell, indicating:
- the line numbers where the code was used or adapted,
- the URL of the source (or, if it's from a book, a full reference to the book),
- the date you accessed the source,
- the author of the code (if the information is available). This is also the case if the "author" is a generative AI (e.g. GPT).

You can use this template -- delete one of the URL or book reference lines as appropriate:

```python
# Lines X-Y: Author Name
# URL: http://...
# Book Title, year published, page number.
# Accessed on 10 Nov 2023.
```

You must also provide **detailed code comments** for any such code, in your own words, to demonstrate that you fully understand how it works -- you will lose marks if you use external code without explaining it, even if it's cited correctly.

Of course, any **non-code sources** that you used for any of your work should also be cited appropriately. You can have a "**References**" section at the end of the notebook, in a Markdown cell, to give your list of references for such sources.

With all that, we trust that you'll be able to use your best judgement, and to cite your sources appropriately -- if anything is not clear, please do ask. Note that **all submissions** will be automatically checked (and manually reviewed) for plagiarism and collusion (between groups), and [the University's academic misconduct policy](https://www.ed.ac.uk/academic-services/staff/discipline/academic-misconduct) applies.
