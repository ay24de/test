"""
This is vars.py file
"""

# vars - only links
O1 = "object"
O2 = O1
print(f"id(O1): {id(O1)}\nid(O2): {id(O2)}")
O2 = "new object"
print(f"id(O1): {id(O1)}\nid(O2) - new object!!!: {id(O2)}")
