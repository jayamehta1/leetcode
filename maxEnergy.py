"""3147. Taking Maximum Energy From the Mystic Dungeon
In a mystic dungeon, n magicians are standing in a line. Each magician has an attribute that gives you energy. Some magicians can give you negative energy, which means taking energy from you.
You have been cursed in such a way that after absorbing energy from magician i, you will be instantly transported to magician (i + k). This process will be repeated until you reach the magician where (i + k) does not exist.
In other words, you will choose a starting point and then teleport with k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.
You are given an array energy and an integer k. Return the maximum possible energy you can gain.
Note that when you are reach a magician, you must take energy from them, whether it is negative or positive energy.
"""


def maximumEnergy(energy, k):
    n = len(energy)
    dp = list(energy)
    for i in range((n - 1), -1, -1):
        if i + k < n:
            dp[i] = dp[i + k] + energy[i]
    return max(dp)


# Example usage:
print(maximumEnergy([2, 3, -5, 1, -4, -2, 6, -1], 3))  # Output: 8
print(maximumEnergy([-2, -3, -5, -1, -4, -2, -6, -1], 3))  # Output: -1
print(maximumEnergy([1, -2, 3, 4, -5, 6], 2))  # Output: 10
print(maximumEnergy([10, -5, -2, 4, 0, 3], 1))  # Output: 10
