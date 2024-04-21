# function definition
def capital_indexes(string):
    idx_list = []

    for i in range(len(string)):
        if string[i] == string[i].upper():
            # add upper case letters INDEXES to the idx list
            idx_list.append(i)
    return idx_list

final_list = capital_indexes("ASLKASLKASKL") # function call
print(final_list)