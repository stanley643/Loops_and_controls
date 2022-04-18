planets=['Mercury', 'Venus','Earth', 'Mars', 'Jupiter','Saturn','Neptune']
for planet in planets:
    print(planets, end='')
print('')

s = 'Stanley is the nEw Programmer in tOwn who is gAIning alot of fAmE eVERYDAY'
for char in s:
    if char.isupper():
        print (char, end='')
print('')


for i in range(5):
    print("Doing important work. i = ", i)


    #while loop

i = 0
while i < 10:
    print(i, end=' ,')
    i +=1
print('')
    #List comprehensions
squares = [n**2 for n in range(10)]
print(squares)