import csv
from tkinter import N

# this will overwrite existing data in the file as we specify "w"
with open("csv_filr.csv", "w", newline="") as f:
    data_handler = csv.writer(f, delimiter="|")
    data_handler.writerow(["Year","Events","Winners"])
    data_handler.writerow(["1999","Best Kept Lawn","None"])
    data_handler.writerow(["1978","Gobstyones","Welch National"])

# this will append data to the file 
with open("csv_filr.csv","a",newline="") as f:
    handle_csv_file = csv.writer(f, delimiter=":")
    handle_csv_file.writerow(["1998","Birthday Celebration", "Hira Zahid"])
    handle_csv_file.writerow(["2022","Graduation Ceremony","Jinnah University For Women"])