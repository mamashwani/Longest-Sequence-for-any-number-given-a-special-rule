"""
Muhammad Mashwani
PeopleSoft ID: 1378052
Homework #5

"""


def next_number(n):
   if n%2==0:
       next_n=n//2
   else:
       next_n=3*n+1
   return next_n

max_len,save_n=0,0
max_seq=[]

for i in range(1,50):
   num=i
   sequence=[num]
   while num!=1:
       num=next_number(num)
       sequence.append(num)

   if max_len<len(sequence):
       max_len=len(sequence)
       max_seq=sequence
       save_n=i

print("The maximum length for starting values up to 2000000 would yield")
print()
print()
print("The longest sequence up to 2000000 is ",save_n," with a length of",max_len)
print(max_seq)
