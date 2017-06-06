messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
print messy_list
# Your code goes below here
messy_list.pop(3)
print messy_list
messy_list.insert(0, 1)
print messy_list
# messy_list = [1, "a", 2, 3, False, [1, 2, 3]]
messy_list.remove("a")
del messy_list[3::]
print messy_list

def first_4(a):
    forinList = a[0:4]
    print forinList

first_4("12345678")

aList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def first_4(a):
    fFour = a[0:4]
    return fFour

first_4(aList)

def first_and_last_4(a):
    fFour = a[0:4]
    lFour = a[-4:]

    fFour.extend(lFour)
    return fFour

def odds(a):
    oddNums = a[1::2]
    return oddNums

first_and_last_4(aList)
odds(aList)

nums = [1, 2, 3, 4, 5]

def reverse_evens(a):
    evens = a[::2]
    rEvens = evens[::-1]

    return rEvens

def sillycase(a):
    half = len(a) / 2
    aLow = a[:int(half)].lower()
    aUp = a[int(half):].upper()
    a = aLow + aUp
    return a


sillycase("Banana")
