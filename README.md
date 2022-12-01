# Visual Sports Studio
### Author: Joseph Armstrong (armstrongjoseph08@gmail.com)
This project aims to design a desktop application that can retrieve sports stats from multiple sport leagues, and then give the user a toolbox of features like graphing and data exporting for users with little to no programing abilities. In order to achieve this end goal, the intention is to use data and software from open-source sports data projects to provide the data to users and then use open-source graphical user interface (GUI) frameworks to give users a low-code application that they can then manipulate the data with and have a codebase that can be easily ported to multiple platforms. With a core framework and design framework, I hope that this app, codenamed "Visual Sports Studio", can help those who want to work with various sports stats but don't have an extensive technical background.

## How to run Visual Sports Studio
To run the application "as-is" (or from source), you need to have Python 3.10 or newer installed and set up on your computer. To check which version of python you have installed run the following command:

```
python --version
```
OR
```
python3 --version
```

If your terminal/console produces a result like/similar this:

```
C:\Users\username>python --version
Python 3.10.8

C:\Users\username>
```
...you should be good to go with running this app, after you install the prerequisite python packages. 

## How to build Visual Sports Studio as a standalone application

Curently the only automatic way of creating is by running the make_windows.bat file. Assuming you have Windows installed with Python 3.10, run make_windows.bat by double clicking it, and Visual Sports Studio should compile into a single-file application after a few minutes.
