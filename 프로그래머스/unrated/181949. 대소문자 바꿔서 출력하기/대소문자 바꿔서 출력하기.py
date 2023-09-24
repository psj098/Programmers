str = input()

switch_str = ''.join([char.lower() if char.isupper() else char.upper() for char in str])

print(switch_str) 