import sys

def search (inp):
    for n in dect:
        num=str(dect[n]["NUMBER"])


        if inp == num:
            find = dect[n]["NAME"]

            return find
        elif len(inp)<10 or len(inp)>10:
            msg="This is invalid number"
            return msg

        elif inp.isdigit() :
            continue
        else:
            msg = "This is invalid number"
            return msg


    not_fi = "Sorry, the number is not found "

    return not_fi

cont1={
    "NAME": "Amal",
    "NUMBER":1111111111

}
cont2={
    "NAME": "Mohammed",
    "NUMBER":2222222222
}
cont3 = {
    "NAME": "Khadijah",
    "NUMBER":3333333333

}
cont4 = {
    "NAME": "Abdullah",
    "NUMBER":4444444444

}
cont5 = {
    "NAME": "Rawan",
    "NUMBER":5555555555

}
cont6 = {
    "NAME": "Faisal",
    "NUMBER":6666666666

}
cont7 = {
    "NAME": "Layla",
    "NUMBER":7777777777

}
dect={
    "contact1":cont1,
    "contact2": cont2,
    "contact3": cont3,
    "contact4": cont4,
    "contact5": cont5,
    "contact6": cont6,
    "contact7": cont7
}
print(dect)

inp=input("enter the PHONE Number :")
ans=search(inp)
print(ans)










