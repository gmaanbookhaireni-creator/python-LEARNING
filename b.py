import random
i = random.randint(1, 10)
j = 0
count = 0
while i != j:
    print(f'{j} didnt match with {i}')
    j = random.randint(1, 10)
    count += 1
else:
    print(f'matched after {count} iterations')