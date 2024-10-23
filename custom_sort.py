list_of_nums = [20 ,10, 5, 15 ,7, 9, 100]

list_of_nums.sort()
print(list_of_nums)

def custom_sorting(data, key):
    # Sorts the list based on the specified key
    return sorted(data, key=lambda x: x[key])

# Example usage: Sorting a list of names and city
data = [
    {"name": "Alice",
      "age": 25, 
      "city": "Mombasa"
      },
    {"name": "Bob", 
     "age": 30, 
     "city": "Kampala"
     },
    {"name": "Charlie",
      "age": 22,
    "city": "Cape Town"
     },
    {"name": "Harrison",
      "age": 17,
    "city": "Nairobi"
     },
]

# Sort by age
sorted_data = custom_sorting(data, "age")
print(sorted_data)

# Sort by name
sorted_data = custom_sorting(data, "name")
print(sorted_data)