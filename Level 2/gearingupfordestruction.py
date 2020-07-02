# Gearing Up for Destruction
# ==========================

# As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's
# axial orientation gears. It should be pretty simple - just add gears to create the appropriate rotation ratio.
# But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it,
# the pegs that will support the gears are fixed in place.

# The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams.
# You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs).
# The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up.
# Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear,
# no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

# Given a list of distinct positive integers named pegs representing the location of each peg along the support beam,
# write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing
# the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above,
# such that radius = a/b. The ratio a/b should be greater than or equal to 1.
# Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible,
# the function solution(pegs) should return the list [-1, -1].

# For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12,
# the second gear could have a radius of 14, and the last one a radius of 6.
# Thus, the last gear would rotate twice as fast as the first one.
# In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

# The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers,
# all between 1 and 10000 inclusive.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution({4, 17, 50})
# Output:
#     -1,-1

# Input:
# Solution.solution({4, 30, 50})
# Output:
#     12,1

# -- Python cases --
# Input:
# solution.solution([4, 30, 50])
# Output:
#     12,1

# Input:
# solution.solution([4, 17, 50])
# Output:
#     -1,-1

from fractions import Fraction


def solution(pegs):
    n = len(pegs)
    separation = []
    for i in range(1, n):
        separation.append(pegs[i] - pegs[i-1])

    x = 0.0

    for i in range(len(separation)):
        if i % 2 == 0:
            x += separation[i]
        else:
            x -= separation[i]

    if n % 2 == 0:
        g0 = (2 * x) / 3.0
    else:
        g0 = 2 * x
    if g0 < 2:
        return [-1, -1]

    gearSizes = [g0]
    for i in range(n-1):
        newGearSize = separation[i] - gearSizes[-1]
        if newGearSize < 1:
            return [-1, -1]
        else:
            gearSizes.append(newGearSize)

    if g0 == int(g0):
        return [int(g0), 1]
    else:
        return [int(round(3 * g0)), 3]


print(solution([4, 17, 50]))
print(solution([4, 30, 50]))
print(solution([1, 5]))