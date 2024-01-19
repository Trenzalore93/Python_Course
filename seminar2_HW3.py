# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.

n = 16
two_in_power = 1
power = 0
while two_in_power <= n:
    two_in_power = 2**(power)
    power += 1
    if two_in_power <= n:
        print(two_in_power)

    
