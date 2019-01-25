
def checkpermutation(str1, str2):

    if isinstance(str1, str) and isinstance(str2, str):
        if len(str1) == len(str2):
            perms = dict()
            for char in str1:
                if char in perms:
                    perms[char] += 1
                else:
                    perms[char] = 1

            for char in str2:
                if char in perms:
                    perms[char] -= 1
                    if perms[char] < 0:
                        return False
                else:
                    return False

            return True


if __name__ == '__main__':
    print(checkpermutation("1232","2124"))
