'''

Instructions
Problem Description:

You are given n, the total number of people, and capacity, the maximum number of people the lift can carry at a time. All people want to go from the ground floor to the top floor. Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.



Input:

Two integers, n and capacity, where n is the total number of people, and capacity is the maximum number of people the lift can carry in one round.



Output:

An integer representing the number of rounds the lift needs to cover to transport all people to the top floor.



Example:

Input: n = 10, capacity = 3
Output: 4

Input: n = 7, capacity = 4
Output: 2


'''
def calculate_lift_rounds(n, capacity):
    # Divide total people by the capacity to get full rounds
    full_rounds = n // capacity
    
    # If there are any remaining people, add one more round
    if n % capacity != 0:
        return full_rounds + 1
    else:
        return full_rounds
    
print(calculate_lift_rounds(10, 3))  # Output: 4
print(calculate_lift_rounds(7, 4))  # Output: 2