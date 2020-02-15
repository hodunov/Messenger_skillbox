print('Hello, world!')
print(2 ** 80)

print(1, type(1))
print('1abc', type('1abc'))
print(1 / 3, type(1 / 3))
print(True, type(True))
print(False, type(False))
print(None, type(None))

this_is_list = [1, 2, 3.5, 'lkasjdbclkjasb', [1, 2, 3]]
print(this_is_list, type(this_is_list))

s = 'Hello, world!'
print(s[0])
print(s[-1])
print(s[0:5])
print(s[:5])
print(s[5:-2])

print(this_is_list[-1][1:])

list_of_users_bad = [
    ['Jack', 'Black', 50],
    ['Саша', 'Пушкин', 100],
]

list_of_users = [
    {'name': 'Jack', 'surname': 'Black', 'age': 50},
    {'name': 'Саша', 'surname': 'Пушкин', 'age': 100},
]

print(list_of_users[1]['name'])
print(list_of_users[0])
print('abc' in list_of_users[0])
