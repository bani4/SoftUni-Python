data=input()
number_list=[]
non_numbers=[]
for i in data:
    if i.isdigit():
        number_list.append(int(i))
    else:
        non_numbers.append(i)
non_numbers=''.join(non_numbers)

take_list=[]
skip_list=[]
for i in range(0,len(number_list)-1,2):
    take_list.append(number_list[i])
    skip_list.append(number_list[i+1])

result=''
start_pos=0
for i in range(len(take_list)):
    #take
    result+=non_numbers[start_pos:start_pos+take_list[i]:]
    #skip
    start_pos+=take_list[i]+skip_list[i]

print(result)