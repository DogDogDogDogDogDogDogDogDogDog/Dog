#Count the occurrence of each vowel in the sentence given as input by the user.
Vowels={
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0
}
thingthaticantbecreativeenoughttothinkofanamefor=input("Say a sentence and i will say what and how many vowels.")
for i in thingthaticantbecreativeenoughttothinkofanamefor:
    if i in Vowels:
        Vowels[i]=Vowels[i]+1
print(Vowels)