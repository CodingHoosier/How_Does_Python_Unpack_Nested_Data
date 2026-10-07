# https://www.youtube.com/watch?v=VZ4j1yFr68o
# How Does Python Unpack Nested Data?
# Create a nested data structure
#  (a tuple containing a string 
#   and another tuple)
# Create a nested data structure
record = ("Alice", (1995, 5, 14))
# Unpack!
name, (year, month, day) = record
print(name) # Alice
print(year) # 1995
print(month) # 5
# Now we'll cause a ValueError 
#  by trying to unpack 
#  the wrong number of elements.
data = [1,2,3,4]
try:
    a, b, c = data
except ValueError as e:
    print(f"ValueError: {e}")
else:
    # We'll never get here
    #  because of the ValueError
    print(f"a: {a}, b: {b}, c: {c}")    
# Does it work with 
#  a list of tuples? Yes!
info = [("Bob", 30), 
        ("Carol", 25), 
        ("Ted", 35), 
        ("Alice",19)]    
# Time to unpack!
bob, carol, ted, alice = info
print(f"Bob's age: {bob[1]}")   
