first=int(input())
second=int(input())
third=int(input())
if first == second and third == first and second == third:
    print(3)
elif first == second or third == first or second == third:
    print(2)
else: print(0)