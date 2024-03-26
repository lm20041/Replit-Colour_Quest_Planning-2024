import csv

with open("colour_list_hex_v1.py", newline='') as file:
  # Read all rows into a list
  all_colors = list(csv.reader(file, delimiter=','))

# remove the first row (header values)
all_colors.pop(0)

#get first 5 rows of colors
print(all_colors[:5])

print("Length: {}".format(len(all_colors)))