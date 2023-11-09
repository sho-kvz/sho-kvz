grt = input('Greeting:')
grt = grt.lower()
grt = grt.replace(" ", "")


if grt.startswith('hello'):
    print('$0')
elif grt.startswith('h') and not grt.startswith('hello'):
    print('$20')
else:
    print('$100')


# x = input('write: ')
# x1 = x.replace(" ", "")
# print(x1)




#------------------------------------------------------------------------------------------------------------------------Bard:
# # Prompt the user for a greeting.
# greeting = input("Greetings! How are you today? ")

# # Remove leading whitespace from the greeting.
# greeting = greeting.lstrip()


# # Convert the greeting to lowercase.
# greeting = greeting.lower()

# # Check if the greeting starts with "hello".
# if greeting.startswith("hello"):
#     # Output $0.
#     print("$0")
# # Check if the greeting starts with "h" but not "hello".
# elif greeting.startswith("h") and not greeting.startswith("hello"):
#     # Output $20.
#     print("$20")
# # Otherwise, output $100.
# else:
#     print("$100")
