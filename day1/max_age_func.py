def max_age(ages):
    if not ages:
        return

    maximum = ages[0]
    for age in ages:
        if maximum < age:
            maximum = age
    return maximum


def max_user_age(users):
    if not users:
        return

    result = users[0]
    maximum = users[0]['age']
    for user in users:
        if maximum < user['age']:
            result = user
            maximum = user['age']
    return result
