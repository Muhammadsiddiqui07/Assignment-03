# # Questio :01
# info = input('Enter any String :')
# count = 0
# for i in range(len(info)):
#     if info[i] == 'a':
#         print('Found vowel ' , info[i])
#         count = count + 1
#     elif info[i] == 'e':
#         print('Found vowel ' , info[i])
#         count = count + 1
#     elif info[i] == 'i':
#         print('Found vowel ' , info[i])
#         count = count + 1
#     elif info[i] == 'o':
#         print('Found vowel ' , info[i])
#         count = count + 1
#     elif info[i] == 'u':
#         print('Found vowel ' , info[i])
#         count = count + 1
        
# print('Total number of vowle is ' , count)

# # Question :02
# info = input('Enter any String: ')
# upper = 0
# lower = 0
# num = 0
# space = 0

# for i in range(len(info)):
#     if info[i] in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
#         print('Upper case found:', info[i])
#         upper += 1
#     elif info[i] in 'qwertyuiopasdfghjklzxcvbnm':
#         print('Lower case found:', info[i])
#         lower += 1
#     elif info[i] in '1234567890':
#         print('Number is found:', info[i])
#         num += 1
#     elif info[i] == ' ':
#         print('White space found')
#         space += 1

# print('Total upper case is:', upper)
# print('Total lower case is:', lower)
# print('Total number is:', num)
# print('Total white space is:', space)

# # Question :03
# info = input('Enter any String: ')
# print('Original string:', info)

# if len(info) > 1:
#     start = info[0]
#     end = info[-1]
    
#     new_info = end + info[1:-1] + start
# else:
#     new_info = info

# print('New string:', new_info)


# # Question :04
# info = input('Enter any String: ')
# reverseStr = ""
# i = len(info) - 1  

# while i >= 0:
#     reverseStr += info[i]  
#     i -= 1

# print(reverseStr)


# # Question :05
# user_input = input("Enter a string: ")

# if len(user_input) > 1:
#     shifted_string = user_input[1:] + user_input[0]
# else:
#     shifted_string = user_input

# print("Shifted string:", shifted_string)


# # Question :06
# name = input("Enter your full name (first name, middle name, last name): ")
# initials = ""
# initials += name[0] + ". "
# for i in range(len(name)):
#     if name[i] == ' ':  
#         initials += name[i+1] + ". "
# print("Initials:", initials.rstrip())


# # Question :07
# string = input("Enter a string: ")

# string = string.replace(" ", "").lower()

# start = 0
# end = len(string) - 1
# is_palindrome = True

# while start < end:
#     if string[start] != string[end]:
#         is_palindrome = False
#         break
#     start += 1
#     end -= 1

# if is_palindrome:
#     print(f"'{string}' is a palindrome.")
# else:
#     print(f"'{string}' is not a palindrome.")


# # Question :08
# original_string = "SHIFT"
# length = len(original_string)
# for i in range(length):
#     shifted_string = original_string[i:] + original_string[:i]
#     print(shifted_string)


# # Question :09
# password = input("Enter a password: ")

# if len(password) < 8:
#     print("Password must be at least eight characters long.")
# else:
#     has_upper = False
#     has_lower = False
#     has_digit = False

#     for char in password:
#         if 'A' <= char <= 'Z':
#             has_upper = True
#         elif 'a' <= char <= 'z':
#             has_lower = True
#         elif '0' <= char <= '9':
#             has_digit = True
#         if has_upper and has_lower and has_digit:
#             break

#     if has_upper and has_lower and has_digit:
#         print("Password is valid.")
#     else:
#         if not has_upper:
#             print("Password must contain at least one uppercase letter.")
#         if not has_lower:
#             print("Password must contain at least one lowercase letter.")
#         if not has_digit:
#             print("Password must contain at least one numeric digit.")
