def last_transactions(user_transactions: list, transaction: str, max_length: int = 3) -> list:
    """
    Adds a transaction to the list of user transactions 
    and returns the updated list.
    
    :param user_transactions: List of current transactions
    :param transaction: New transaction
    :param max_length: Maximum transactions to keep

    :return: Updated list of transactions
    """

    # Add new transaction
    user_transactions.append(transaction)

    # Remove oldest transaction if we exceed the maximum
    if len(user_transactions) > max_length:
        user_transactions.pop(0)

    return user_transactions

def test_first_transaction_is_dropped():
    expected_value = 3
    transactions: list[str] = []

    transactions = last_transactions(transactions, "deposit $100", 3)
    transactions = last_transactions(transactions, "deposit $200", 3)
    transactions = last_transactions(transactions, "deposit $300", 3)
    transactions = last_transactions(transactions, "deposit $400", 3)

    assert (
        len(transactions) == expected_value
    ), f"Expected {expected_value}, but got {len(transactions)} transactions"

    assert ( transactions[0] == "deposit $200"), f"Expected first transaction to be 'deposit $200', but got '{transactions[0]}'"

    # Return a success message
    return "Tests passed!"

print(test_first_transaction_is_dropped())