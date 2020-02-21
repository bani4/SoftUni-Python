electrons_to_distribute=int(input())
electrons_on_shell=[]
distributed=False
shell=1
while not distributed:
    if electrons_to_distribute>=2*shell**2:
        electrons_to_distribute-=2*shell**2
        electrons_on_shell.append(2*shell**2)
    else:
        electrons_on_shell.append(electrons_to_distribute)
        distributed=True
    shell+=1
if electrons_on_shell[len(electrons_on_shell)-1]==0:
    electrons_on_shell.pop()
print(electrons_on_shell)