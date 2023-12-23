# Python Programming - Tutorial notebooks

Tutorial notebooks are Jupyter notebooks (`.ipynb` files). They are your **course notes** for this course, in the form of interactive notebooks with code examples and exercises.

Each folder contains your tutorial notebook for a given week. For example, the `w01` folder contains the notebook for Week 1. Note that you already have access to all the notebooks for the entire semester -- but for the sake of your learning and workload, one per week should be plenty!

You will work through a new notebook each week, in your own time. You should work through most of your weekly notebook **before your workshop** on Thurs/Fri.


## How do I get started?

### To start a codespace (cloud environment):

If you're not sure how to get started, we recommend that you work in GitHub Codespaces. This will allow you to do all your programming inside your browser. Simply speaking, a codespace is a virtual computer with Python and some useful libraries already installed and set up for you.

Here is how to start a new codespace:

- Click on the green "<> Code" button (top right).
- Click on the "Codespaces" tab.
- Click on the green "Create codespace on main" button.
- Wait a few minutes for everything to get set up.
- Once VSCode appears in your browser, click on the `w01` folder, then on `week01.ipynb` in the left bar to start your notebook.

### Set up your codespace for Jupyter notebooks:

- Run the first code cell in `week01.ipynb`.
- If you are prompted (at the top of the screen) to install the Python + Jupyter extensions, do so.
- Then, if you are prompted to select a kernel, choose the option which starts with `base`.

If you have issues running code in the notebook, we strongly recommend that you use Google Chrome or Chromium. Some notebook features may not work in other browsers.

### To find your previously created codespace:

When you come back to this repository later, you'll be able to rejoin your previous codespace (instead of creating it again). GitHub will give it a random goofy name, and it will show up instead of the "Create codespace on main" button -- just click on it.

Codespaces are kept for 30 days; if you don't come back to a codespace for 30 days, it will be deleted, and you will lose your work. In the Week 1 workshop, you will learn how to upload your changes back to GitHub, so that you don't lose them (even if your codespace is deleted).

### If you prefer working offline:

You need to clone this repository. This is how (assuming you've installed all the required software):

- Click on the green "<> Code" button (top right).
- Click on the "Local" tab.
- Copy the URL given to you.
- Launch VSCode.
- In VSCode, press `Ctrl + Shift + P` (`Cmd + Shift + P` on MacOS), search for "clone", and select "Git: Clone".
- Paste the URL in the text box and press Enter.
- Select a folder where you want to store the files.
- If required, authenticate with GitHub.
- Finally, the files should appear in VSCode. Click on the `w01` folder, then on `week01.ipynb` in the left bar to start your notebook.


## What are the other files?

You don't need to touch any of them, but if you're wondering:

- `README.md` is this very file.
- `.gitignore` is a simple list of everything we don't want git to track.
- `show_solutions.py` will be used inside your notebook, for you to reveal exercise solutions when they are released.
- `solutions` is a folder (empty for now) where the solutions to the notebook exercises will be released at the end of each week. When the solution files are added to this folder, the solution boxes should start working automatically inside your notebooks.
- `.devcontainer` contains configuration files to set up your codespace.
