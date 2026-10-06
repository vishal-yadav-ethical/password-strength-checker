password = input("enter your password:")

if len(password) <8:
  print("password is too short.")
elif len(password) >= 8:
  print("password length is acceptable.")
