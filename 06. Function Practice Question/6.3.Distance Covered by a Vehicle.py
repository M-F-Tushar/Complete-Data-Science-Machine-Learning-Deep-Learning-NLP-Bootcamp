'''
Instructions
Problem Description:

You are given the speed of a vehicle and the time it has traveled. Your task is to compute and return the distance traveled by the vehicle.

Formula:

To calculate the distance traveled by a vehicle:

Distance=Speed×Time



Input:

Two floating-point numbers, speed and time, representing the speed of the vehicle and the time it has been traveling.



Output:

A floating-point number representing the distance traveled.



Example:

Input: speed = 60, time = 2
Output: 120.0

Input: speed = 50.5, time = 1.5
Output: 75.75


'''
def vehicle_distance(speed, time):
    return speed * time

print(vehicle_distance(60, 2))  # Output: 120.0
print(vehicle_distance(50.5, 1.5))  # Output: 75.75