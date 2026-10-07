password = input("enter your password:")

if len(password) <8:
  print("password is too short.")
elif len(password) >= 8:
  print("password length is acceptable.")
  
if not any(char.isupper() for char in password):
  print("password needs an uppercase letter.")

if not any(char.islower() for char in password):
  print("password needs a lowercase letter.")

if not any(char.isdigit() for char in password):
  print("password needs a number.")

if not any(not char.isalnum() for char in password):
  print("password needs a special character.")

print("password checking complete.")
score = 0

if len(password) >= 8:
  score += 1

if any(char.isupper() for char in password):
  score += 1

if any(char.islower() for char in password):
  score += 1

if any(char.isdigit() for char in password):
  score += 1

if any(not char.isalnum() for char in password):
  score += 1

if score <= 2:
  print("password strength: weak")
elif score <= 4:
  print("password strength: medium")
else:
  print("password strength: strong")
  
