current_version = input().split('.')
int_curr_ver = int(''.join(current_version))
next_ver = '.'.join(list(str(int_curr_ver + 1)))
print(next_ver)