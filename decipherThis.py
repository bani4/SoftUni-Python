def decipher_word(word):
    char_code=''
    count=0
    #отделяме числовата част и броим колко знака е
    for i in word:
        if i.isdigit():
            count+=1
            char_code+=i
    
    #прилепяме знака като начална буква
    deciphered_word=chr(int(char_code))
    
    #вземаме последната за втора
    deciphered_word+=word[len(word)-1]
    
    #прилепяме тези които не се променят до предпоследната вкл.
    for i in range(count+1,len(word)-1):
        deciphered_word+=word[i]
    
    #слагаме 1вия след цифрите знак за последен, само ако не съвпада да е последна и втора буква като при 'go'
    if count!=len(word)-1:
        deciphered_word+=word[count]
    return deciphered_word

message=input().split()
deciphered_message=''

for w in message:
    deciphered_message+=decipher_word(w)+' '

print(deciphered_message)