# Week 1 workshop - Pair-programming and working with GitHub

In the workshops in this course, you will work on a programming task together with a partner, using a method called **pair programming**. This week's task is designed for you to try it out, and to become familiar with the workflow.

## What is pair programming?

Pair programming is a method where two people (usually) sit in front of the same computer. Each person has a specific role:

- The **driver** writes and runs the code, and is the only person allowed to do it. They explain what they do to the navigator.
- The **navigator** observes and helps the driver, spots errors in the code, gives suggestions and ideas... They are not allowed to write code.

The two programmers decide who should "drive" first, and that person takes the keyboard to start working. The other person, the navigator, watches the screen and helps the driver with the task -- without touching the mouse or keyboard.

Then, after a while, the driver passes the keyboard and mouse to the navigator, and they switch roles.

This can also work well with teams of 3, where the driver has 2 navigators. We will call this workflow "pair programming" regardless of whether we work in teams of 2 or 3.

## How does it work on a laptop?

Since you will each be working with your own laptops (or desktop computers) during the labs, there are a few ways to go about pair-programming -- here are examples:

- The driver always works from their own computer, the navigator(s) watch the screen. When changing roles, the new driver starts working from their own computer, and everyone moves to watch that.
- All students work from one computer and pass it around when they switch roles.
- etc.

The task this week contains detailed instructions about what to do and when, so you can have a better idea of how this works in practice. You can try different ways to pair-program and stick to what feels the most natural. There will be less and less scaffolding in future workshops -- it will feel more natural after you've done it a few times. During workshops, we will typically ask you to switch roles **every 15 minutes** or so, to make sure that both you and your partner(s) take both roles at least once.

## Working with git and GitHub

You will be working with git and GitHub throughout the course. If it seems a little intimidating just now, don't worry -- you'll become more and more comfortable with it as you practice. Here are a few useful things to know before getting started:

- **git** is a program that helps you manage programming projects. You can think of git as a sort of clerk or bookkeeper, which keeps track of all the changes you make to the files in your project.
- a **repository** is basically just a folder with some files inside, generally managed with git. It's where your programming project lives, it contains the files with all the code.
- a **repo** is just short for "repository".
- a **local repo** is a repository located on your computer's hard drive (not online), or in your codespace.
- Whenever you "accept an assignment" using the links on Learn, a repo is created for you online on GitHub.
- When you **clone** that repo onto your computer, or when you start a codespace, this downloads the files from the GitHub repo, and also creates a "link" (called a *remote*) from your local repo to the GitHub repo. The changes you make to these files are *only* in your codespace (or on your computer), until you *push* them (i.e. upload them) back to the GitHub repo. We will go through that process today.

## Terminal commands

*If you are not comfortable using a terminal, and/or if you are using Codespaces, you can skip this section, as well as anything in the rest of the instructions that starts with __Terminal commands__.*

If you are using a code editor which doesn't have a git interface/menu (for example Spyder), you can use a terminal to manage git instead. You will need to type commands in the terminal and press Enter to run them.

- On Windows, use the application "Git Bash". (It should come pre-installed with git.)
- On MacOS and Linux, use your Terminal application. (It should come pre-installed with your operating system.)

Here is a summary of the commands we'll use today, for reference. Replace the repo URL with the link you copy from GitHub.

| Command | Description |
|-|-|
| `git clone https://github.com/pypr23/w01-workshop-yourteamname.git` | Clones the GitHub repo in your home folder. |
| `cd w01-workshop-yourteamname` | Navigate to the newly created folder. |
| `git status` | Check if there are any unstaged changes. |
| `git add -A` | Stages all changes. |
| `git commit -m "My commit message"` | Commits the staged changes with the message `My commit message`. (Include the quotation marks!) |
| `git push origin main` | Pushes the committed changes to the GitHub repo. |
| `git pull origin main` | Pulls the new changes from the GitHub repo. |

### Authentication

For certain commands, git will ask you to type your GitHub username and password. Since August 2021, to interact with GitHub using terminal commands, you need to set up a Personal Access Token (PAT) in your GitHub account settings. Follow the [instructions here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to set it up, and ask a tutor if you need help.

---

## Instructions

First, decide who should be the "driver" first (you will switch roles later).

### Create your team repository on GitHub

If you made it here (following the instructions on Learn), then you probably have done this already -- congratulations! You and your partner(s) are now **contributors** to the *same* GitHub repository -- you can each change the code in the repo.

The team repository you created (by accepting the assignment and creating/joining your team) lives online for the moment, on GitHub.

### Let's start coding!

- **Driver:** first of all, **show your screen** to your teammate(s), so that they can see what you do. When you code something, explain what you are doing out loud.
- **Navigator(s)**: follow what is happening on the screen, and help the driver. Read these instructions to them, so they don't have to keep coming back here to read them all the time. (You could use your own computer to do this.)

#### Driver:

- If you haven't done this already, **start a new codespace** for this repository. This is the same process as you did for creating your `pypr-notebooks-...` repository to get the course notebooks. If you don't remember how to do this, you can ask your **navigator** for help.

##### Terminal commands

*If you are working offline and prefer using terminal commands:*

> - Launch a terminal, type `git clone https://github.com/pypr23/w01-workshop-yourteamname.git`, and press Enter.
> - If prompted, type your GitHub username and press Enter, then paste your GitHub PAT and press Enter. (See earlier instructions to set up your PAT.)
> - Type `cd w01-workshop-yourteamname` and press Enter to navigate to the new folder.

#### Driver:

*If you have encountered any issues so far, please call a tutor.*

- Once VSCode is loaded, open the file `hello.py`. This is a **Python script**, which you can recognise with the extension `.py`. This can only contain Python code.

- You will see that there is already some code in there. Let's try to run it: in VSCode, click on the triangle which looks like a "play" button at the top right of your screen. You should see the *output* of the code appear in a terminal window at the bottom of the screen.

*If this doesn't work, please call a tutor.*

#### Driver & navigator(s):

Discuss together to figure out how the `print()` command works here. Driver, you can try to remove the `f` in front of the quote `'`, and run the code again to see what happens; you can also try changing what's inside the `{}`. Navigator, you can consult the documentation [here](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) and explain it to your driver.

#### Driver:

- On lines 1 and 2, change the variables `name` and `age` to reflect your own name and age.

- On line 3, create a new variable called `birthday`, a *string* which indicates when is your birthday (the day and month) -- for example, `'30th January'`.

- Then, after the `print()` command, add another line to print a sentence which says when is your birthday. Run all the code again, and check that it worked. If it doesn't work, ask your navigator to help you find the error.

Now, you are going to log your changes using git, and update the GitHub repo with your new code. This is what you need to do:

- Press Ctrl+s (Windows, Linux) or Cmd+s (MacOS) to save the file.

- You should now see a little blue circle with a number on the 3rd icon in the grey bar on the left of your screen (this is the "Source Control" tab). This means that git has detected that there have been changes made in the folder, but that you haven't yet informed git of these changes. Click on this icon.

- You should see the file `hello.py` under "Changes". Hover your mouse near "Changes", and click on the `+`. Your changes are now "Staged changes". This informs git that there have been some changes to the files in the repo.

- Finally:
    - **Type a message** in the text box where it says "Message", to describe what changes you've made. For example, your message could be "Added my birthday to hello.py".
    - **Then**, click the green "Commit" button.
Now, your changes are **committed** to your *local* repo. This just means that you've told git to save the changes, and to make a checkpoint in your project. **Whenever you commit**, you should first write a **short message** to describe what changes you've made.

*If at this point you see an error saying "Make sure you configure your 'user.email' and 'user.name' in git", [skip to the section below](#error-with-git-configuration-make-sure-you-configure-your-useremail-and-username-in-git), and come back here after.*

#### Navigator:

From your own computer, go to the repo on GitHub, refresh the page, and check the file `hello.py` -- you should see that it hasn't changed yet.

#### Driver:

The final step is for you to **push** these files from your codespace to GitHub (i.e. upload them). Click the green "Sync Changes" button (confirm if you get an extra message), and wait a few seconds for this to finish.

#### Navigator:

Refresh the page again, and check `hello.py` -- you should now see the changes.

#### Driver:

To summarise, this is what you have just done, in git terms:

1. First, you told git that you've changed some files. This is called **staging** your changes.
2. Then, you told git to **commit** these changes, i.e. to save them in your local repo (in your codespace or on your computer).
3. Finally, you told git to **push** the changes online to the GitHub repo, so that your collaborator(s) can also see them.

##### Terminal commands

*If you use the terminal, this is how you do all of the above:*

> - Make sure you have saved the file.
> - In your terminal, make sure you are still in the folder `w01-workshop-yourteamname`. If not (e.g. if you have opened a new terminal), navigate to it using `cd`.
> - You can check that there are new changes by using `git status` and pressing Enter. This should list the files that have been changed.
> - To stage all changes, type `git add -A` and press Enter.
> - To commit your changes, type `git commit -m "your commit message"` and press Enter.
> - To push your changes, type `git push origin main` and press Enter.

##### Error with git configuration: "Make sure you configure your 'user.email' and 'user.name' in git"

> If at this point you see an error with a message similar to the above, then git wants you to do a little bit of configuration before it lets you commit for the very first time. This is because each commit needs to be easily identifiable as coming from a specific person. This is explained in more detail [here in the git documentation](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) (in the section "Your Identity"), if you are interested. Here are the steps to solve this:

> - On Windows, launch the application "Git Bash". On MacOS and Linux, open the Terminal.
> - Type the following command and press Enter:
> `git config --global user.email "youremailaddress"`
> - Type the following command and press Enter:
> `git config --global user.name "Your Name"`
> 
> Use the email address you used to register your GitHub account. For example, for me, the 2 commands would be:
>
> `git config --global user.email "charlotte.desvages@ed.ac.uk"`
> `git config --global user.name "Charlotte Desvages"`
>
> After this, you can close the terminal and try to commit again -- it should now work.


### Time to switch roles!

Navigator, you are now the **driver**, and vice versa.

- **(New) driver**: show your screen to the others in your group. Explain what you do out loud for your navigator(s) to follow more easily.
- **(New) navigator**: you are now in charge of reading the instructions for your driver, observing what they do, and helping them when necessary.

**Note** for the new driver: if you decide to pass one laptop around to pair-program, or to take turns typing on one computer, you should still do the following from your *own* computer at least once. In future sessions, do this at the end of the session to ensure that all group members have access to the code you produced together.

#### Driver:

Go back to the GitHub repo, which is now updated with the latest changes.

- If you have not created your own codespace yet, go back to the first "Driver:" section, and follow the same instructions to create your codespace.
- If you had already created your own codespace at the start of the workshop, then go to VSCode in your browser, open the Source Control tab (third icon down on the left), click the `...` icon next to "Source Control", and click "Pull", which will download the latest changes from GitHub and update your local repo with these changes.

> **Terminal commands:** to pull the changes, in the terminal, make sure you are in the folder `w01-workshop-yourteamname`; if not, navigate to it using `cd`. Then, type `git pull origin main` and press Enter.

Go back to the "Explorer" tab (top icon on the left of VSCode) -- you should now see the files, including the changes that the previous driver just made. If you've had any issues with this, please call a tutor.

- Open `hello.py` and run the code yourself to check that it still works. (It should!)

- Change the values of `name`, `age`, and `birthday` to your own name, age, and birthday.

- Delete the line that prints when your birthday is.

- Write a new line to print a sentence which says that you will be one year older on your birthday. For instance, with the example values that were in the code at the beginning of the workshop, that could be something like:

> On the 27th October, I will be 37 years old.

The date and age should correspond to your own, and you are not allowed to type them or copy/paste them explicitly into the `print()` command. Run the code and check that it works.

#### Navigator:

Help your driver figure out how to do this. You can also look at the documentation [here](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals). If the code doesn't work the first time, help the driver to find the error.

#### Driver:

Save the file, stage your changes, commit them, and push them to GitHub. You can ask your navigator to read you the instructions again from the previous section.

#### Navigator:

After the changes have been pushed, refresh the GitHub repo to check that this has worked -- you should see the new code there. Then, go back to your codespace, and in the "Source Control" tab, click `...` and then "Pull". Check that you now also have the changes in your local `hello.py` file.

## Victory!

Well done -- you now know how to pair-program, how to use git to manage your changes, and how to work collaboratively on a shared GitHub repository.

**Note:** you can now go back to your `pypr-notebooks-...` repository, launch your codespace, and *stage, commit, and push* any changes you've made, so that they're safely uploaded to your GitHub repo. Remember that codespaces are deleted automatically after 30 days; if you don't do this, you will lose your work.

If you still have time before the end of the workshop, then please continue working like this together. You can change roles again now (don't forget to change who shares their screen), and continue adding and changing things to the code, if you want to get more practice with git. **Don't forget to stage and commit your changes regularly**, even if you are not switching roles immediately! Also, **don't forget to switch roles** at least a couple more times. If you are a team of 3, make sure you switch roles at least one more time so that everyone tries to be the driver.

Here are some suggestions:

- Instead of changing the values of `name`, `age`, and `birthday`, change the variable names to e.g. `name_1`, `age_1`, and `birthday_1`, and add 3 new variables `name_2`, `age_2`, and `birthday_2`, so that both your names, ages, and birthdays are kept in memory. Add another command to print that information for both of you.

- Using **comparison operators** (you can't type 'True' or 'False' yourself), try to print the following:

> Is <person 1> younger than <person 2>? <True/False>

where <person 1> and <person 2> are your respective names, and <True/False> is either `True` or `False` (the Boolean value) depending on your ages. Again, no typing names or ages in the `print()` command!

- Create more variables to print information about yourselves to get to know each other a little better: where you are from, what courses you are taking this semester... It's a bit like having a conversation using exclusively `print()` commands.

- You can also create a new Python script: in the "Explorer" tab, right-click on the name of the folder (`w01-workshop-...`), select "New File", and give it a name -- don't forget the `.py` extension. Write some code in it, run it; stage, commit, and push your changes for that new file to appear in the GitHub repo. You could create a new script like this to work together on one of the notebook problems, for example.

- If you've been using VSCode to manage git but you are curious about the terminal commands, try them out! They should also work in the terminal in VSCode in your codespace.

## Useful tips

- If you can't decide who should be the driver first, pick the person who lives closest to the North Pole.
- Throughout a pair programming session, the driver and the navigator should **communicate** as much as possible. For example, when typing code, the driver can explain what they want to do, talk through their thought process, ask the navigator for help; the navigator can provide feedback on the code, ask the driver to do something differently, spot mistakes and suggest corrections, consult the documentation (or other notes)...
- Today, you have used a shared GitHub repository to collaborate on a task. You also have a GitHub repository for your notebooks, which only belongs to you -- you should still push your local changes to GitHub, otherwise they will be lost when your codespace is deleted (30 days after you last use it). It's also a very good way to keep an **online backup** of your work -- in fact, this is how you will submit your assignments later on. (Your repositories are private by default.)
