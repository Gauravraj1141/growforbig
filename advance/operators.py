a = 4
b = 2

# division
c = a / b  # 2.0
# modulus
c = a % b  # 0
# Exponentiation a**b means square
c = a ** b  # 16
# Floor division
c = a // b  # 2
c = a & b
c = a | b

# print(c)
# d += a
# d %= a
# d //= a
d = 50
print(bin(d))
d <<= 4
print(d)

# print(15|20)
# a = bin(15)
# b = bin(20)
# print(int(a[2:])|int(b[2:]))
#  print(bin(15)|bin(20))
# print(type(a))
# print(type(int(a[2:])))

print(not False)  # True
print(not True)  # False

# Bitwise Operator
# {'&':'AND','|':'OR','~':'not','^':'XOR','<<':'Left Shift','>>':'Right Shift'}

# & operator
a = 12  # 1100
print(bin(a))  # 0b1100

# it will convert both variable in boolean and then apply 'AND' operator if both true then true otherwise false
# means 1,0=0
b = 5  # 101
print(bin(b))  # 0b101

# 1100 & 0101  = 0100  because 8421  so 1 is on the 4's position

print(a & b)  # 4


# | OR Operator

a = 12  # in binary 1100
print(bin(a))  # 0b1100
b = 5  # in binary 101
print(bin(b))  # 0b101

# solve it  1100 | 0101  = 1101  because it is or operator here 1,0 = 1  so based on 1101 so 8421 = 13
print(a | b)  # 13

# ~ Not operator
a = 6
print(bin(a))  # 0b110
# for "NOT" we take 2s complement of this binary number 110 = 001 means 0 will be 1 and 1 will be 0
# so 001 ka 2's complement = 001 = 110+1 = 111 now it will be negative means -7 based on 421
b = ~ a
print(b)

# ^ XOR operator
a = 7  # 111
print(bin(a))  # 0b111
b = 9  # 1001
print(bin(b))  # 0b1001

#  0111 ^ 1001 = 1110  based on 8421 = 14 here 0,1 = 1 and 1,1 = 0
print(a ^ b)  # 14


# >> Right shift  operator
a = 10  # 1010
print(bin(a))  # 0b1010
# here 1010 will be 0101 = 0101 = 010 it 421 because inplace of right 1 came 0 then it is known as divisible by 5
b = a >> 2
print(b)  # 2

# << left shift operator
a = 12  # 1100
print(bin(a))  # 0b1100
b = a << 2
# 1100 = 11000 here we multiply by 2 so here is 2times then 12*2 = 24 then 24*2= 48 , that's all 11000 = 11000
print(b)  # 48
