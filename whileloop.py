# Importing re module
import re

# Given String
s = "I'm  human being."

# Performing Sub() operation
res_1 = re.sub('a', 'x', s)
res_2 = re.sub('[a,I]','x',s)

# Print Results
print(res_1)


print(res_2)


# The original string remains unchanged
print(s)