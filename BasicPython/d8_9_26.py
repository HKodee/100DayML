# iterator
numbers =[10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# Generators

def counter(start, end):
    current = start
    
    while current<= end:
        yield current
        current += 1
        
c = counter(5, 10)

print(next(c))
print(next(c))
print(next(c))

for x in c:
    print(x)
    
# practice quetion 1
 
def even_numbers(start, end):
    current = start
    
    while current<=end:
        if current%2==0:
            yield current

e = even_numbers(15,47)
print(next(e))
for x in e:
    print(x)        
   
   
#practice question 2  
# def greater_than_50(numbers):
#     i=0
#     for i<len(numbers):
#         if