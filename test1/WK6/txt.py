with open("test1/WK6/harry.txt") as h:
    with open("john.txt") as j:
      h_lines = h.readlines()
      j_lines = j.readlines()
for i in range (len(j_lines)):
    print(f"John: {j_lines[i]}")
  

    