''' If temperature is greater than 30, it's a hot day other wise if it's less than 10; its cold day; otherwise, it's
neither hot nor cold.'''

user_temperaute=int(input("Enter the temperautre:"))
if user_temperaute>30:
    print(f'Its hot')
elif user_temperaute<10:
    print(f'Its cold')
else:
    print(f'Its neither hot nor cold')