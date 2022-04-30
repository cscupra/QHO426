import csv

def gather_data(n = 1):
  with open("eve_data.csv", "w") as file:
    csv_writer = csv.writer(file)
    for i in range(n)
      h = float(input("Enter Height: "))
      w = float(input("Enter Weight: "))
      csv_writer.writerow([h, w])
def retrieve_data():
    with open("eve_data.csv") as file:
      csv_reader = csv.reader(file)
    for row in csv_reader:
          heights.append(row[0])
          weights.append(row[1])   
return heights, weights
print(retrieve_data())
