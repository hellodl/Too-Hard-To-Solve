
# 4.3
def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])


# 4.4
def fact(n):
    if n <= 1:  # considering negative num, fact(0) and fact(1)
        return 1
    else:
        return n * fact(n-1)


# 4.5
def reString(str):
    if len(str) <= 1:
        return str[-1]
    else:
        return str[-1] + reString(str[0:-1])

def alnumFilter(s):
    f = filter(str.isalnum,s)
    strFilterd = ''
    for i in f:
        strFilterd += i

    return strFilterd

def isPal(str):
    str_t = alnumFilter(str).lower()
    str_reversed = reString(str_t).lower()
    return (str_t == str_reversed)


def main():
    print(listSum([1, 4, 6, 8, 2, 1]))
    print(fact(3))

    str0 = 'cnt'
    print(str0)
    print(reString(str0))

    crazestr = 'ab#@df13@$[]03'
    cFiltered = alnumFilter(crazestr)
    print(cFiltered)

    print("is 'kayak' Palindrome?",isPal('kayak'))
    print("is 'aibohphobia' Palindrome?", isPal('aibohphobia'))
    print("is 'Live not on evil' Palindrome?", isPal('Live not on evil'))
    print("is 'Reviled did I live, said I, as evil I did deliver' Palindrome?", isPal('Reviled did I live, said I, as evil I did deliver'))
    print("is 'Go hang a salami; I’m a lasagna hog' Palindrome?", isPal('Go hang a salami; I’m a lasagna hog'))
    print("is 'Able was I ere I saw Elba' Palindrome?", isPal('Able was I ere I saw Elba'))
    print("is 'Kanakanak' Palindrome?", isPal('Kanakanak'))
    print("is 'Wassamassaw' Palindrome?", isPal('Wassamassaw'))

if __name__ == '__main__':
    main()
