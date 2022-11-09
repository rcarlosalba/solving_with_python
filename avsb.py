a_three = int(input())
a_two = int(input())
a_one = int(input())
b_three = int(input())
b_two = int(input())
b_one = int(input())

a_total = (3 * a_three) + (2 * a_two) + a_one
b_total = (3 * b_three) + (2 * b_two) + b_one

if a_total < b_total:
    print('B')
elif a_total > b_total:
    print('A')
else:
    print('T')
