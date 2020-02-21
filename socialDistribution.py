population=list(map(lambda x:int(x),input().split(', ')))
min_wealth=int(input())

def rich_to_poor(lista,mw):
    i=0
    while lista[i]<mw:
        giving=mw-lista[i]
        lista[i]=mw
        lista[lista.index(max(lista))]-=giving
        i+=1

if len(population)*min_wealth>sum(population):
    print('No equal distribution possible')
else:
    rich_to_poor(population,min_wealth)
    print(population)