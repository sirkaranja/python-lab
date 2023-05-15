
def palindrome():
    my_str = "RADAR"

    #case sensitivity
    my_str= my_str.lower()
    
    #reverse
    rev_str= reversed(my_str)

    #comparison for my_str and rev_str

    if list(my_str) == list(rev_str):
        print("The string is a palindrome")
    else:
        print("Not a palindrome")

palindrome()


