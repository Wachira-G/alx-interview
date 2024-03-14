#!/usr/bin/python3

"""Prime game module."""

def isWinner(x, nums):
    """Main function for getting a winner."""
    def is_prime(num):
        """Checks if a number is a prime number."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        """Gets prime numbers upto to a certain number n."""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def calculate_winner(n):
        """Calculates the winner of the game"""
        primes = get_primes_up_to_n(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = [calculate_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
