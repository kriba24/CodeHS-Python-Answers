role = input("Are you an administrator, teacher, or student? ")
if role == "student":
    print("Students do not get keys!")
elif role != "administrator" and role != "teacher" and role != "student":
    print("You can only be an administrator, teacher, or student!")
else:
    print("Administrators and teachers get keys!")