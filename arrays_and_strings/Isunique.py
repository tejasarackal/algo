
def isunique(ustring):
    if isinstance(ustring, str):
        unique = dict()
        for c in ustring:  # enumerating through all characters
            if c in unique:
                return False
            else:
                unique[c] = True
        return True
    else:
        return False


def isuniquerestrictive(ustring):
    if isinstance(ustring, str):
        strlen = len(ustring)
        ustring = ''.join(sorted(ustring))
        for index in range(0, strlen - 2):
            if ustring[index] == ustring[index + 1]:
                return False

        return True


if __name__ == '__main__':
    print(isuniquerestrictive("1232"))
