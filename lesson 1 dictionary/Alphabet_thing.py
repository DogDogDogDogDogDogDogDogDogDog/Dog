alphabet={

}
question=input("Name a sentance and I will tell you how many of each letters are in it!")
for i in question:
    if i.isalpha():
        if i in alphabet:
            alphabet[i]+=1
        else:
            alphabet[i]=1
print(alphabet)