from itertools import takewhile


#
# a = [1, 1, 0]
# class ParkingSystem:
#
#     def __init__(self, big: int, medium: int, small: int):
#          self.big = big
#          self.medium = medium
#          self.small = small
#
#     def addCar(self, carType: int) -> bool:
#         if carType == 1 and a[0] > 0:
#             return True
#         elif carType == 2 and a[1] > 0:
#             return True
#         elif carType == 3 and a[2] > 0:
#             return True
#         else:
#             return False
# print(ParkingSystem(1, 1, 0).addCar(1))
# print(ParkingSystem(1, 1, 0).addCar(2))
# print(ParkingSystem(1, 1, 0).addCar(3))
# print(ParkingSystem(1, 1, 0).addCar(1))

# t = [4, 2, 3, 5, 6, 7, 2, 3]
# print(list(takewhile(lambda x: x != 7, t)))

# l = ['']
# class OrderedStream:
#     def __init__(self, n: int):
#         self.n = n
#
#
#     def insert(self, idKey: int, value: str) -> list[str]:
#         global l
#         l = l*self.n
#         ptr = len(list(takewhile(lambda x: x != '', l)))
#         l[idKey - 1] = value
#         if not l[ptr]:
#             return []
#         else:
#             return list(takewhile(lambda x: x != '', l[ptr:]))
#
#
# print(OrderedStream(5).insert(3, "ccccc"))
# print(OrderedStream(5).insert(1, "aaaaa"))
# print(OrderedStream(5).insert(2, "bbbbbb"))
# print(OrderedStream(5).insert(5, "eeeee"))
# print(OrderedStream(5).insert(4, "ddddd"))


# DESIGN solved!!!!!!!!!!!!
#
#     def __init__(self, big: int, medium: int, small: int):
#          self.big = big
#          self.medium = medium
#          self.small = small
#          self.a = {
#             1:self.big,
#             2:self.medium,
#             3:self.small,
#          }
#
#     def addCar(self, carType: int) -> bool:
#         if carType == 1 and self.a[1] > 0:
#             self.a[1] = self.a[1] - 1
#             return True
#         elif carType == 2 and self.a[2] > 0:
#             self.a[2] = self.a[2] - 1
#             return True
#         elif carType == 3 and self.a[3] > 0:
#             self.a[3] = self.a[3] - 1
#             return True
#         else:
#             return False

# print(ParkingSystem(0,0,2).addCar(1))
# print(ParkingSystem(0,0,2).addCar(2))
# print(ParkingSystem(0,0,2).addCar(3))
# git config user.name Jaska-ITishnik
# git config user.email jasurbekbekmirzayev2004@gmail.com

class OrderedStream:
    def __init__(self, n: int):
        self.n = n
        self.l = [''] * n

    def insert(self, idKey: int, value: str) -> list[str]:
        ptr = len(list(takewhile(lambda x: x != '', self.l)))
        self.l[idKey - 1] = value
        if not self.l[ptr]:
            return []
        else:
            return list(takewhile(lambda x: x != '', self.l[ptr:]))

print(OrderedStream(5).insert(3, "ccccc"))
print(OrderedStream(5).insert(1, "aaaaa"))
print(OrderedStream(5).insert(2, "bbbbbb"))
print(OrderedStream(5).insert(5, "eeeee"))
print(OrderedStream(5).insert(4, "ddddd"))



"""
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Jaska-ITishnik/algorithm.git
git push -u origin main
"""