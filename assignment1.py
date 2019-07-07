import csv
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Data visualization concepts assignment 1
# Plot 1: Create a vertical stacked bar chart and present the total number of births per area in canton of Zurich for
# each gender for 2015.

# Plot 2: Aggregate the number of births per gender and create a pie chart in order to present the
# total number of births for females and males in canton of Zurich for 2015.

# Plot 3: Create a line plot (similar to time series) and present the total (aggregated)
# number of births  from canton of Zurich per year for both females and males.

class Assignment1(object):
    def __init__(self, filename):
        # Initialize
        self.years = []
        self.areas = []
        self.areas_names = []
        self.filename = filename
        with open(self.filename, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if not row["StichtagDatJahr"] in self.years:
                    self.years.append(row["StichtagDatJahr"])
                if not row["QuarSort"] in self.areas:
                    self.areas.append(row["QuarSort"])
                    self.areas_names.append(row["QuarLang"])

        # Convert years and areas in tuple for later use
        self.years = tuple(reversed(self.years))  # Reverse years in order to have it sorted
        self.areas = tuple(self.areas)
        self.areas_names = tuple(self.areas_names)

    def get_total_births_per_gender_per_year(self, gender, year):
        total = 0
        with open(self.filename, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["StichtagDatJahr"] == year and row["SexKurz"] == gender:
                    total += int(row["AnzGebuWir"])
            return total

    def get_total_births_per_area_per_year(self, area, year):
        out = {"men": 0, "women": 0, "total": 0}
        with open(self.filename, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["StichtagDatJahr"] == year and row["QuarSort"] == area:
                    if row["SexKurz"] == "M":
                        out["men"] += int(row["AnzGebuWir"])
                        out["total"] += int(row["AnzGebuWir"])
                    else:
                        out["women"] += int(row["AnzGebuWir"])
                        out["total"] += int(row["AnzGebuWir"])
        return out

    def get_total_births_per_year(self, year):
        total = 0
        with open(self.filename, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row["StichtagDatJahr"] == year:
                    total += int(row["AnzGebuWir"])
            return total

# Print head info
print("============================================================================")
print(" _______       ___   .___________.    ___   ____    ____  __       _______.")
print("|       \     /   \  |           |   /   \  \   \  /   / |  |     /       |")
print("|  .--.  |   /  ^  \ `---|  |----`  /  ^  \  \   \/   /  |  |    |   (----`")
print("|  |  |  |  /  /_\  \    |  |      /  /_\  \  \      /   |  |     \   \    ")
print("|  '--'  | /  _____  \   |  |     /  _____  \  \    /    |  | .----)   |   ")
print("|_______/ /__/     \__\  |__|    /__/     \__\  \__/     |__| |_______/    ")

print("  ___           _                          __    ___")
print(" / _ | ___ ___ (_)__ ____  __ _  ___ ___  / /_  <  /")
print("/ __ |(_-<(_-</ / _ `/ _ \/  ' \/ -_) _ \/ __/  / / ")
print("/_/ |_/___/___/_/\_, /_//_/_/_/_/\__/_//_/\__/  /_/ ")
print("                /___/                               ")

print("Timucin Besken - 14-924-609")
print("============================================================================")

data = Assignment1("bevgeburtenjahrgeschlquartstz.csv")  # Create data object


def get_data_plot1(year):
    global data
    total_m = []
    total_w = []
    total_both = []
    for area in data.areas:
        t_total = data.get_total_births_per_area_per_year(area, year)
        n_m = t_total["men"]
        n_w = t_total["women"]
        n_total = t_total["total"]
        total_m.append(n_m)
        total_w.append(n_w)
        total_both.append(n_total)
    total_m = tuple(total_m)
    total_w = tuple(total_w)
    total_both = tuple(total_both)
    return {"men": total_m, "women": total_w, "total": total_both}


# Choose year to plot

valid = False

while(not valid):
    data_year = input("Please write the year you want to plot (1993-2015): ")
    # Check if integer
    try:
        u_i = int(data_year)
    except ValueError:
        print("This is not a valid input!")
    else:
        # Check if in 1993-2015
        if int(data_year) < 1993 or int(data_year) > 2015:
            print("You have to choose a year between 1993 and 2015")
        else:
            valid = True


# Set-up figure
fig = plt.figure(figsize=(30, 30))
fig.subplots_adjust(hspace=1, wspace=0, top=0.910, bottom=0.080, left=0.041, right=0.990)

########################################
#              PLOT 1                  #
########################################
print("Generating first plot...")
plt.subplot(221)
data_plot_1 = get_data_plot1(data_year) # Get data

# Setup working variables
men = data_plot_1["men"]
women = data_plot_1["women"]
total = data_plot_1["total"]
areas = data.areas
width = 0.7

# Plot labels and title
plt.ylabel('Number of births')
plt.xlabel('Areas')
plt.title('Number of males and females births per Area in Zurich in ' + data_year)

# Axes ticks
plt.xticks(range(len(areas)), data.areas_names, rotation='vertical')
plt.yticks(range(0, max(total), 50))

# Generate bars
p0 = plt.bar(range(len(areas)), men, width)
p1 = plt.bar(range(len(areas)), women, width, bottom=men, color='#d62728')

# Add legend
plt.legend((p0[0], p1[0]), ('Males', 'Females'))

# Create box for checkboxes
box_measures = plt.axes([0.43, 0.92, 0.05, 0.06]) # x position, y position, width, height
# Add checkboxes
check = CheckButtons(box_measures, ('Males', 'Females'), (True, True))


# Hide/Show men/women helper function
def select_gender(label):
    if label == 'Males':
        for (m_bar, w_bar) in zip(p0, p1):  # Loop through all bars
            m_bar.set_visible(not m_bar.get_visible())  # Change the bool to the opposite
            if m_bar.get_visible():  # If male bar is visible, then the women bar should be on top
                w_bar.set_y(m_bar.get_height())  # Set women bar starting y value = x height
            else:
                w_bar.set_y(0)  # If the men bar is not visible, then women start from 0
    elif label == 'Females':
        for b in p1:
            b.set_visible(not b.get_visible())  # Since this is on top of men, nothing else is necessary to do
    plt.draw()

check.on_clicked(select_gender)  # When click on checkbox, run the function

########################################
#              PLOT 2                  #
########################################
print("Generating second plot...")

# Set-up plot settings
plt.subplot(222)
plt.axis('equal')

# get and Set-up data
total_birth_man = data.get_total_births_per_gender_per_year("M", data_year)
total_birth_w = data.get_total_births_per_gender_per_year("W", data_year)
sizes = [total_birth_man, total_birth_w]
total = int(total_birth_man) + int(total_birth_w)

# Plot title and labels
plt.title('Number of males and females born in Zurich in ' + data_year)
labels = 'Males', 'Females'

# Generate pie chart
plt.pie(sizes, labels=labels, autopct=lambda p: "{:0.0f}".format(p*total/100), shadow=False, startangle=90)


########################################
#              PLOT 3                  #
########################################
print("Generating third plot...")

# Setup plot settings
plt.subplot(223)

#  get and Set-up data
years = data.years
n_births_total = []

# Loop through the years
for year in years:
    n_births_total.append(data.get_total_births_per_year(year))

#  Set-up chart and plot

# Labels and plot title
plt.xlabel('Year')
plt.ylabel('Number of births')
plt.title('Number of births per year in Zurich')

# Axes ticks
plt.xticks(range(len(years)), years, rotation='vertical')

# Generate line plot
plt.plot(range(len(years)), n_births_total)
plt.grid()  # Add grid

################################################################################

plt.show()  # Generate final figure
