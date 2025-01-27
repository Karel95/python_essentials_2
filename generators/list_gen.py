# The brackets make a comprehension:
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

# The parentheses make a generator:
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

print(len(the_list))

print(len(the_generator)) # TypeError: object of type 'generator' has no len()
