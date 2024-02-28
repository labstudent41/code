grammar = {
    'S': ['aA', 'aAb'],
    'A': ['b', 'ba']
}

# grammar = {
#     'S': ['A', 'AB'],
#     'A': ['aB'],
#     'B': ['b']
# }

def generate_regex(non_terminal):
    regex = ""
    for production in grammar[non_terminal]:
        production_regex = ""
        for symbol in production:
            if symbol.isupper():
                production_regex += generate_regex(symbol)
            else:
                production_regex += symbol
        regex += "" + production_regex + "|"
    return regex[:-1]

print("Expression : ", generate_regex('S'))
