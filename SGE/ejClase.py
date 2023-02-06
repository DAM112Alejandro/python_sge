x=[8,2,3,1,2,5,7]
personas=['pedro','sara','miguel']
print(list([x**3 for x in x]))
print(list([x**2 for x in x if x%2!=0]))
print(list([x**2 for x in x if x%2!=0 and x>0]))
print(list([x for x in personas if x.__len__()>=5]))
print(list([x for x in personas if x.__contains__("o")]))
print(list([x for x in personas if x.__contains__("e") and x.__len__()>=6]))
