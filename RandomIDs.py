import secrets  # The secrets module in Python is used to generate cryptographically secure
# random numbers and tokens for managing sensitive data like passwords,
# authentication keys, and security tokens.


class generate_4_digit_id:
    def __init__(self):
        self.id = secrets.randbelow(9000) + 1000

    def __str__(self):
        return str(self.id)


"""
This ensures the result has at most 4 digits starting from 0.
+ 1000
Shifts the range upward so the smallest possible number is 1000 and the largest is 9999.

    """
