''' If name is less than 3 characters long- name must be at least 3 characters othersie if its more than 50
characters- name must be maximum of 50 characters
otherwise - name looks good!'''

user_character=input("Enter a name:")
length_user_character=len(user_character)
if (length_user_character<=3):
    print("Name must be atleast 3 characters")
elif (length_user_character>=50):
    print("Name must be maximum of 50 characters")
else:
    print("Name looks good!")