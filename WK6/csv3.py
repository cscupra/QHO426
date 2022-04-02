
import csv
csv_rowlist = [["SN", "Movie", "Character"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]
with open('movie.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)
