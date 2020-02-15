import random
from day1.max_age_func import max_user_age

ages = [
    {'name': 'Jack ' + str(i), 'surname': f'Black {i}', 'age': random.randint(0, 100)}
    for i in range(20)
]

print(ages)
print(max_user_age(ages))
print(max_user_age([]))
