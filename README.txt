
Data Visualization Concepts - Assignment 1
 _______       ___   .___________.    ___   ____    ____  __       _______.
|       \     /   \  |           |   /   \  \   \  /   / |  |     /       |
|  .--.  |   /  ^  \ `---|  |----`  /  ^  \  \   \/   /  |  |    |   (----`
|  |  |  |  /  /_\  \    |  |      /  /_\  \  \      /   |  |     \   \    
|  '--'  | /  _____  \   |  |     /  _____  \  \    /    |  | .----)   |  
|_______/ /__/     \__\  |__|    /__/     \__\  \__/     |__| |_______/    

  ___           _                          __    ___
 / _ | ___ ___ (_)__ ____  __ _  ___ ___  / /_  <  /
/ __ |(_-<(_-</ / _ `/ _ \/  ' \/ -_) _ \/ __/  / / 
/_/ |_/___/___/_/\_, /_//_/_/_/_/\__/_//_/\__/  /_/
                /___/                              

Student name: Timucin Besken
Matriculation Number: 14-924-609

How to use:
Simply run from the terminal: python assignment1.py
You will be asked to provide the year to be plotted (valid values: 1993-2015) and then press Enter.


IDE used: JetBrains PyCharm Community Edition 2017.2.1

Python Distro: Anaconda 5.0.1 Python 3.6 version
Libraries: matplotlib v2.1.0
Python modules used: CSV
Interpreter: Python 3.6.3


Description:
I create a class whith some methods to retrieve the data from the csv file, 
that is get total births per year, get total births per area per year, and get total births per gender per year.

After that my code can be separated in 3 parts, one for each plot.

In the first I get the data with a function from the class with the method get_total_births_per_area_per_year() 
by looping through all areas of Zurich and then I arranged them in order to return a dictionary which is easier to work with.

For the checkbox I imported CheckButtons from matplotlib.widgets.
To hide/show males and females bars I simply hide/show the single bars, with the exception of the bars for females,
since they need to be bringed up or down depending from the visibility of the males bar.

For the plot 2 I get the data by calling the respective method get_total_births_per_gender_per_year(), 
once for males and once for females and then I give everything to the plot function while formatting the numbers 
in order to show the number of births instead of the percentage.

For the third plot I loop through the years to get the data by calling get_total_births_per_year(year), 
while looping I append each value to a list which I then give as argument to the plot() method.

The figure is then simply made by 2 rows 2 columns and then I plotted each chart in sequential slots.
