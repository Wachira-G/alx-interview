#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def calculate_winner(n):
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
