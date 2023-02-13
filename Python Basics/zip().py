a = [1,2,3,4]
b = [5,6,7,8,9,10]
c = "python"

z = zip(a,b,c)
# print(list(z))
t1, t2, t3 = zip(*z)
print(t1, t2, t3, sep="\n")