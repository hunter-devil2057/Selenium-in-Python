# add(), discard(), clear(), pop(), copy(), union(), update(), intersection(), isdisjoint(), issuperset(), max(), min(), len()
a = {1, 2, 3, 4}
b = {5, 6, 7, 8, 9, 75, 42, 86, 38}
c = {9, 7, 38, 42}
d = b.issuperset(a)
print('Is all the elements of Set a are elements of Set b ', d)

e = b.issuperset(c)
print('Is all the elements of Set c are elements of Set b ', e)