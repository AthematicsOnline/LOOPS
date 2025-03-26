'''
count = 0

while count < 20:  # Loop condition
    print("Count:", count)
    count += 1  # Increment the count
print("Loop finished")

# -------------------------------------------------------------------------------
Num = int(input('Number '))
Count = 1
while Num > 0:
    R = Num % 3
    print(R)
    Num //= 10
# --------------------------------------------------------------------------------
'''
Num = int(input('Number '))
Count = 1
while Count <= Num:
    if Num%Count == 0:
        print(Count, end=",")
    Count = Count +1

# ---------------------------------------------------------------------------------
Num = int(input('Number = '))
I = 2
while I < Num:
    if Num%I == 0:
        print(Num, 'is not a prime number ')
        break
    I += 1
else:
    print(Num, 'is a prime number ')

# ----------------------------------------------------------------------------------
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i = i+1
print('The End')
# -----------------------------------------------------------------------------------
i = 1
while 1 < 5:
    i += 1
    if i == 3:
        continue
    print(i)
print('The End')
'''