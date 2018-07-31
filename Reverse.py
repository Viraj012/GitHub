rom={'I': 1,'V' : 5,'X' : 10}
n=input("Enter a roman number")
k=
for i in range(len-1,0):
    if(rom[n[i]]>rom[n[i-1]]):
        k=k-rom[i-1]
    elif(rom[i]==rom[i-1] or rom[i]<rom[i-1]):
        k=k+rom[i-1]
print("\nEquivalent Decimal Number is %d ",k);
