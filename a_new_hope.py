number_of_far = int(input())

if number_of_far == 1:
    print(f'A long time ago in a galaxy far away...')
else:
    far = 'far, ' * (number_of_far - 1)
    print(f'A long time ago in a galaxy {far}far away...')
