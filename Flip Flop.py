
my_tuple = (1, 2, 3, 3, 2, 1)
def is_palindrome(tup):
    return tup == tup[::-1]
if is_palindrome(my_tuple):
    print(f"The tuple {my_tuple} is a palindrome.")
else:
    print(f"The tuple {my_tuple} is not a palindrome.")
