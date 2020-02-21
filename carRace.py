numbers = [int(x) for x in input().split()]
left_racer = 0
right_racer = 0
for i in range(len(numbers) // 2):
    if numbers[i] != 0:
        left_racer += numbers[i]
    else:
        left_racer = left_racer * 8 / 10
    if numbers[len(numbers) - i - 1] != 0:
        right_racer += numbers[len(numbers) - i - 1]
    else:
        right_racer = right_racer * 8 / 10

if left_racer < right_racer:
    print(f'The winner is left with total time: {left_racer:.1f}')
else:
    print(f'The winner is right with total time: {right_racer:.1f}')
