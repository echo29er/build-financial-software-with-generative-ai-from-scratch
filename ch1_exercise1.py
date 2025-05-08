def formatted_balance(current_balance: float) -> str:
    """
    Function purpose
        Returns the current balance in a formatted string. 

    Parameters: 
        current_balance(float): the current balance to be formatted
    
    Returns: 
        Str
    """

    return f"£{float(current_balance):,.2f}"

def message_to_user(balance_in: float) -> str:
    return f"Your balance is {formatted_balance(balance_in)}."


# Ask the user to enter the current balance
user_input = input("Enter your current balanace: ")

# Call the function to print the balanace
print(message_to_user(float(user_input)))