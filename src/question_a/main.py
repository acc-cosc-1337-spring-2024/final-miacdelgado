import question_a

# Creates list of 5 numbers
list_numbers = []

for i in range(0, 5):
    set_numbers = int(input('Enter a number to add to the list: '))
    list_numbers.append(set_numbers)

# Figures out the lowest number in the list
lowest_num = question_a.lowest_number(list_numbers)

# Figures out the highest number in the list
highest_num = question_a.highest_number(list_numbers)

# Figures out the total value of the list
total_num = question_a.total(list_numbers)

# Figures out the average of the list
average_num = question_a.average(list_numbers)

# Prints out the user generated list
print('Here is your list: ', list_numbers)

# Prints the "fun facts" of the list
print('Now, here are some fun facts about your list.'
      '\nThe lowest number entered is: ', lowest_num,
      '\nThe highest number entered is: ', highest_num,
      '\nThe total for all the numbers entered is: ', total_num,
      '\nThe average of the numbers entered is: ', average_num,)