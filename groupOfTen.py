numbers = list(map(lambda x: int(x), input().split(', ')))
i = 1
while len(numbers) > 0:
    group_to_remove = list(filter(lambda x: (i-1)*10<= x <= i*10, numbers))
    print(f'Group of {i}0\'s: {group_to_remove}')
    i += 1
    numbers=[i for i in numbers if i not in group_to_remove]
