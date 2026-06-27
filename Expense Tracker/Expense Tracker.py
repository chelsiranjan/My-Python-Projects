
import csv
import os
from datetime import datetime

file_name = 'expenses.csv'

categories = [
    'Food', 'Transport', 'Shopping', 'Entertainment',
    'Bills', 'Health', 'Education', 'Other',
    'Clothes', 'Ration', 'Kitchen']

while True:
    print('\nExpense Tracker')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Category Summary')
    print('4. Exit')

    choice = input('Enter choice: ')

    if choice == '1':

        # data --> DD-MM-YYYY
        while True:
            date = input('Enter date (DD-MM-YYYY): ')

            try:
                entered_date = datetime.strptime(date, '%d-%m-%Y')

                if entered_date > datetime.now():
                    print('Future date is not allowed!')
                else:
                    break

            except ValueError:
                print('Invalid date! Please enter a valid date.')


        print('\nCategories:')

        for i in range(len(categories)):
            print(i + 1, categories[i])


        while True:
            try:
                num = int(input('Choose category number: '))
                # if other than category number it will show error or say invalid

                if 1 <= num <= len(categories):
                    break
                else:
                    print('Invalid category number')

            except ValueError:
                print('Enter a valid number')
                
        category = categories[num - 1]


      
        while True:
            try:
                amount = float(input('Enter amount: ₹ '))

                if amount > 0:
                    break
                else:
                    print('Amount must be positive')

            except ValueError:
                print('Enter a valid amount')
                
        description = input('Enter description: ')


        with open(file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
            
        print('Expense Added')




    elif choice == '2':

        if not os.path.exists(file_name):
            print('No expenses found')
            continue

        total = 0

        print('\nDate         | Category       | Amount       | Description')

        with open(file_name, 'r') as file:
            reader = csv.reader(file)

            for row in reader:

                date, category, amount, description = row

                print(
                    f'{date:<12} | '
                    f'{category:<14} | '
                    f'₹{float(amount):<11.2f} | '
                    f'{description}')


                total += float(amount)
            
        print(f'\nTotal Expenses: ₹{total:.2f}')




    elif choice == '3':

        if not os.path.exists(file_name):
            print('No expenses found')
            continue

        summary = {}

        with open(file_name, 'r') as file:
            reader = csv.reader(file)

            for row in reader:

                date, category, amount, description = row


                if category in summary:
                    summary[category] += float(amount)

                else:
                    summary[category] = float(amount)
                    
        print('\nCategory Summary')


        for category, total in summary.items():
            print(f'{category:<15} ₹{total:.2f}')




    elif choice == '4':

        print('GoodBye')
        break

    else:

        print('Invalid Choice')

