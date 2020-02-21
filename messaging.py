numbers=[x for x in input().split()]
string=input()
output=''

indexes=[]
for element in numbers:
    sum=0
    for i in element:
        sum+=int(i)
    indexes.append(sum)

for index in indexes:
    while index>=len(string):
        index=index//len(string)
    output+=string[index]
    string2=string[:index]+string[index+1:]
    string=string2

print(output)


