solutions = (((1,3), (2,3), (3,4)), ((1,2), (3,4)), ((1,2), (2,5), (3,1), (3,4)))

lenths = {}

for sol in solutions:
    lenths[len(sol)] = sol

print(lenths)

print(lenths[min(lenths.keys())])