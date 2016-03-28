# The returned string is the concatenation of each string
# in the passed-in list.
print(', '.join(['cats', 'rats', 'bats']))

print(' '.join(['My', 'name', 'is', 'Simon']))

# Return a list of the words in S, using sep as the delimiter string.
# If maxsplit is given, at most maxsplit splits are done.
# If sep is not specified or is None, any whitespace string is
# a separator and empty strings are removed from the result.

print('My name is      Simon'.split())
print('My,name,is,Simon'.split(','))
