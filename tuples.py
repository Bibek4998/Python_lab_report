# Write a program to demonstrate tuple operations.
tuples=('A','B','C','D','E','F')
print(f"Original Tuple: {tuples}")
a=list(tuples)
a.append('G')
tuples=tuple(a)
print(f"Updated tuple: {tuples}")
print("Unpacking Tuple: ")
(A,B,C,D,*E)=tuples
print(A)
print(B)
print(C)