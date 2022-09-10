from asyncore import read
import csv

with open("winner.csv") as f:
    read_content = csv.reader(f)
    winner_list = []
    for i in read_content:
        winner_list += i
    print("Winner List", winner_list)


# find the winner og Welch Nationional Event 
with open("winner.csv") as f:
    user_input = input("Enter the event name")
    read_winner_file = csv.reader(f)
    list_of_winner =[]
    for i in read_winner_file:
        list_of_winner += i
    print(user_input)
    index_of_user_input = list_of_winner.index(user_input)
    target_index = index_of_user_input + 1
    the_winner = list_of_winner[target_index]
    print(f'The winner was {the_winner}')
