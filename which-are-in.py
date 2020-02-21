string1=input().split(', ')
string2=input().split(', ')
which_are_in_list=[]
for element in string1:
    element_is_substring=False
    i=0
    while not element_is_substring and i<len(string2):
        element_to_check_from_str2 = string2[i]
        if element_to_check_from_str2.find(element)>-1:
            element_is_substring=True
            which_are_in_list.append(element)
        else:
            i+=1

print(which_are_in_list)
