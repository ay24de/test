"""
This is string.py file
"""

#
S1 = "this is string"
S2 = "this is string"
print(f"{id(S1)} = {id(S2)}")
print(f"id(S1) == id(S2): {id(S1) == id(S2)}")

# isalpha
S1 = "123425grsgsegs"
S2 = "frwgfvwgwr"
print(f"S1.isalpha(): {S1.isalpha()}")
print(f"S2.isalpha(): {S2.isalpha()}")

#immutability
S1 = 'string one'
S2 = S1.upper()
print(f'S1: {S1}')
print(f'S2: {S2}')
S1 = S1.capitalize()
print(f'new S1!!!!!: {S1}')

