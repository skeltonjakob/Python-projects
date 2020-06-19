#for i in range(3):
#    for j in range(3):
#        product = i * j
#        print(str(i) + " * " + str(j) + " = " + str(product))
for i in range(1, 11):
    factors = []
    for j in range(1,i + 1):
        if i % j == 0:
            factors.append(j)
print("The factors of " + str(i) + " are: " + str(factors))


for i in range(1,11):
    for 
