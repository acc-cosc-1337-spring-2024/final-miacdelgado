from question_d import create_multiplication_table, display_multiplication_table

# Creates menu
print('Multiplication Table Menu\n'
      '1-Display Multiplication Table\n'
      '2-Exit\n')

# Prompts the user for one of the menu item selects
menu_select = int(input('Select one of the above options: '))

while menu_select != 1 and menu_select != 2:
    menu_select = int(input('That choice is not valid, please choose a menu option: '))

while menu_select == 1 or menu_select == 2:
    if menu_select == 1:
        
        table = create_multiplication_table()
        display_multiplication_table(table)

        menu_cont = input('Would you like to choose another option from the menu ( y or n )? ')

        if menu_cont == 'n' or menu_cont == 'N':
            print('Goodbye')
            menu_select = 'exit'

        else:
            print('Multiplication Table Menu\n'
                  '1-Display Multiplication Table\n'
                  '2-Exit\n')
                
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 2:
                print("Goodbye")
                menu_select = 'exit'

    elif menu_select == 2:
        menu_exit = input("Are you sure you would like to exit the program: ")
        if menu_exit == 'Y' or menu_exit == 'y':
            print("Goodbye")
            menu_select = 'exit'
        else:
            print('Multiplication Table Menu\n'
                  '1-Display Multiplication Table\n'
                  '2-Exit\n')
            
            menu_select = int(input('Select one of the above options: '))

            while menu_select != 1 and menu_select != 2:
                menu_select = int(input('That choice is not valid, please choose a menu option: '))

            if menu_select == 2:
                print("Goodbye")