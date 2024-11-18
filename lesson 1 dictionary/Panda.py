Panda={
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0
}
Question=input("Gimme number! NOM NOM NOM! Me number eating monster! NOM NOM NOM! Me tell you if Panda or not! NOM NOM! Gimme number!")
for i in Question:
    if i in Panda:
        Panda[i]=+1
if 0 in Panda.values():
    print("Me not eat panda, no panda, me sad!!!😭😭😭")
else:
    print("NOM NOM! Me eat panda!!!😋😋😋 Me happy!")
print("Panda=Pangram")