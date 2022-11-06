print("What should our value be:")
val1 = int(input())

val, combo, pv, nv, dv, qv, hv = 0, 0, 1, 5, 10, 25, 50
for h in range(int((val1 / 50) + 1)):  # [1]
    hc = (hv * h)
    for q in range(int((val1 / 25) + 1)):
        qc = (qv * q)
        for d in range(int((val1 / 10) + 1)):
            dc = (dv * d)
            for n in range(int((val1 / 5) + 1)):
                nc = (nv * n)
                for p in range(int((val1 / 1) + 1)):
                    pc = (pv * p)
                    val = (pc + nc + dc + qc + hc)
                    if val == val1:  # [2]
                        combo += 1
                        print("p = {}, n = {}, d = {}, q = {}, h = {} | Number Combo = {}".format(p, n, d, q, h, combo))
print("Total number of combinations for {}:".format(val1))
print(combo)


'''
1: This tower is the brute forcing of the program; it just increments by one for every combination of coins.

2: If the value of the coins equals our wanted value, then we print those values and increment our combo.

3: The use of break isn't useless. Without it, the program will not stop counting the pennies until it hits 100.
Because of that, you preform a plethora of un-needed calculations, as the program should reset to 0 pennies every combo,
which exponentiates the time it takes to find greater and greater combinations.
(I used the time module to verify this claim. Yes, it's true, alas, it's barely noticeable)
''' 
