from collections import deque, Counter, namedtuple

nums = [1, 2, 3, 4, 5]

dq = deque(nums)
dq.appendleft(0)
print(dq)

print(Counter("applemango"))

turn_rotation_tuple = namedtuple("TurnRotation", "angle, type")
coordinatesTuple = namedtuple("Coordinates", "x, y, z MoreInfo")
turn_rotation = turn_rotation_tuple(180, "clockwise")
coordinates = coordinatesTuple(10, 20, 30, turn_rotation)
print(coordinates)
print(coordinates.MoreInfo)