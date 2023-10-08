t = (1, 2, 4)
# () - tupla
# {} - slownik
# [] - list
print(t)


def f():
    return 1, 2, "sting"


print(f())

t1 = ("marcin", "marcel", "maja")
print(t1)
print(t1.count("marcin"))  # 1
print(t1.index("maja"))  # 2
print(t1[1])  # marcel

t2 = ("monika",)
t3 = ("ss",) + t1 + t2
print(t3)

list1 = list(t3)
print(list1)
list1.append("magda")
print(list1)
t4 = tuple(list1)
print(t4)



for index, imie in enumerate(t4):
    # l=[index, imie]
    # l[0]
    # l[1]
    #
    # d = {"inxex": index, "imie": imie}
    # d["inxex"]

    print(f"Interuje sie przez element {index} o wartości {imie}")


l = [1,2,3,4,5 ] #15
l = [] #0
l = [1,-1] #0
l =[]

sum = None
for i in l:
    if sum is None:
        sum = i
        continue
    sum += i
print(sum)



