import csv

with open("pottercompetition.csv") as csv_file:
    reader_of_csv = csv.reader(csv_file)
    potter_competitions = []
    for each_line in reader_of_csv:
        potter_competitions += each_line
    # displays the list 
    print('data', potter_competitions)
    # targetting a lsit fourth element 
    print("A fourth element of list is:", potter_competitions[4])
    # methos for finding index number of element of list 
    print("Index of Xeror 198 is :", potter_competitions.index("Xerox 198"))

    

    