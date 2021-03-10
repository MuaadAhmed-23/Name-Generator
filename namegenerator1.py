reading_firstname = open('firstname.txt', 'r')
reading_lastname = open('lastname.txt', 'r')

# convert firstname file to lists and then sets
for x in reading_firstname:
    global convert_list_firstname
    convert_list_firstname = list(x.split(' '))
    convert_set_firstname = set(convert_list_firstname)

# combine the first and last name sets together in a set
for line in reading_lastname:
    global convert_list_lastname
    convert_list_lastname = list(line.split(' '))
    convert_set_lastname = set(convert_list_lastname)
    global fullName
    fullName = convert_set_lastname.union(convert_list_firstname)
    fullname_list = list(fullName)
    print(fullname_list)

# combining both the first and last names and generate full names
for x in fullname_list:
    if fullname_list.index(x) == fullname_list.index(x):
        z = fullname_list.index(x)
        if z > len(fullname_list):
            break
        if z < len(fullname_list):
            q = z + 2
            d = fullname_list[z] + ' ' + fullname_list[q]
            print(d)
