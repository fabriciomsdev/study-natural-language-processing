import re

# Removing my surname

nome = "Fabricio Magalhaes Sena"
result = re.sub(" [A-Z][\w]*", "", nome)

print(result)

"""
  Explanation:
    query: " [A-Z][a-z]*"
    Term 1: '" ' -> Indicate we need to get the anything with space on start.
    Term 2: '[A-Z]' -> After term 1 we should have a uppercase letter (only one)
    Term 3: '[\w]*' -> After term 2 the string should have any letter in lowercase or uppercase
"""
