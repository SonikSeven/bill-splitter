import random
number = int(input('Enter the number of friends joining (including you):\n'))
names = []

if number > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(number):
        names.append(input())
    total_bill = int(input('Enter the total bill value:\n'))
    if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower() == 'yes':
        lucky = random.choice(names)
        friends = dict.fromkeys(names, round(total_bill / (number - 1), 2))
        friends[lucky] = 0
        print(f'{lucky} is the lucky one!\n{friends}')
    else:
        friends = dict.fromkeys(names, round(total_bill / number, 2))
        print(f'No one is going to be lucky\n{friends}')
else:
    print('No one is joining for the party')
