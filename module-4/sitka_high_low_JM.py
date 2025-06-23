"""
Jessie Miers
CSD325
6/22/2025
The original sikta_high.py was modified to extract the lows data from the 'sitka_weather_2018_simple.csv' file,
as well as the original date and high temps. Function was made to allow users’ inputs to control what data was 
processed through the plot(graph function) based on the user inputs from the main function's inputs.
The main function includes a menu and prompt to have the user input highs, lows, and exit, along with alternatives listed out.
and provides a loop back when the user closes the pop-up, allowing them to input a different option. 


"""
import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.

    # Changed to also pull low temperatures from the file.
    dates, highs,lows = [], [],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

#This function, added to the original code, it is used to plot the information for the user's request, without the need for code duplication for high and low. 
def graph(dates, temperatures, title, color=''):
    # Plot the high or low temperatures based on user request.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, temperatures, c=color)


    # Format plot.
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
#This function was added to provide a looping menu for the user to access high or low information and exit the program. 
#This function also contains error checking on input and allows for alternatives to highs, lows, and exit. 
def main():
    print("Welcome to Sitka Weather Application.")
    print("You can view daily high or low temperatures from 2018. ")
    
    while True:
        choice = input("Please enter Highs(high), Lows(low), or Exit(quit) to continue or exit.\n").lower()
        if choice == "highs" or choice == "high":
            graph(dates, highs, "Daily Highs Temperatures - 2018", color='red')
        elif choice == "lows" or choice == "low":
            graph(dates, lows, "Daily Lows Temperatures - 2018", color='blue')
        elif choice == "exit" or choice == 'quit':
            print("Thank you for using Sitka Weather Application, Goodbye.\n")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again. \n")

if __name__ == "__main__":
    main()