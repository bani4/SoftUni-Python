stores = []
store_items = []

command = input()
while command != 'END':
    command = command.split('->')

    if command[0] == 'Add':
        if command[1] not in stores:
            stores.append(command[1])
            store_items.append([command[1], command[2]])

        else:
            store_items[stores.index(command[1])][1] += ',' + command[2]
    else:  # remove
        if command[1] not in stores:
            pass
        else:
            which_store = []
            for i in store_items:
                if i[0] == command[1]:
                    which_store = i
            store_items.remove(which_store)
            stores.remove(command[1])

    command = input()
store_items.sort(reverse=True)
store_items.sort(key=lambda x: (-x[1].count(',')))

print('Stores list:')
for i in store_items:
    print(i[0])
    items = i[1].split(',')
    for j in items:
        print(f'<<{j}>>')
