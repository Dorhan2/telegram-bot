
with open("C:/Users/Андрей/PycharmProjects/untitled/gg.txt",'r') as file:
 s=file.read()
 i=0
 x=5
 y=4
 z=3
 q = 0
 sum2=0
s='+'.join(s[i:i+1]for i in range(0,len(s),1))
kol = s.count('') - 1
kol1 = s.count('+')
kol2=1
sum = eval(s) / (kol - kol1)
print(sum)
sum = eval(s) / (kol - kol1)
if sum<3.5 and x>sum:
    i=0
    while sum<3.509:
     i=i+1
     sum =(sum*(kol - kol1) + (x)) / (kol - kol1 + kol2)
print("надо получить",i,"<5>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum<3.5 and y>sum:
    i=0
    while sum<3.509:
     i=i+1
     sum =(sum*(kol - kol1) + (y)) / (kol - kol1 + kol2)
print("надо получить",i,"<4>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum<5  and x>sum:
    i=0
    while sum<4.509:
     i=i+1
     sum =(sum*(kol - kol1) + (x)) / (kol - kol1 + kol2)
print("надо получить",i,"<5>","для",round(sum,2))
sum = eval(s) / (kol - kol1)



if sum<2.5  and x>sum:
    i=0
    while sum<2.509:
     i=i+1
     sum =(sum*(kol - kol1) + (x)) / (kol - kol1 + kol2)
print("надо получить",i,"<5>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum<2.5  and y>sum:
    i=0
    while sum<2.509:
     i=i+1
     sum =(sum*(kol - kol1) + (y)) / (kol - kol1 + kol2)
print("надо получить",i,"<4>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum<2.5  and z>sum:
    i=0
    while sum<2.509:
     i=i+1
     sum =(sum*(kol - kol1) + (z)) / (kol - kol1 + kol2)
print("надо получить",i,"<3>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum< 3.5:
    i=0
    while sum<3.509:
        i=i+1
        sum = (sum * (kol - kol1) + (x)) / (kol - kol1 + kol2)
        while sum<3.509 and y>sum:
            q=q+1
            sum = (sum * (kol - kol1) + (y)) / (kol - kol1 + kol2)
            break
print("надо получить",i,'<5>',"и",q,"<4>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum< 2.5:
    i=0
    q=0
    while sum<2.509:
        i=i+1
        sum = (sum * (kol - kol1) + (x)) / (kol - kol1 + kol2)
        while sum<2.509 and y>sum:
            q=q+1
            sum = (sum * (kol - kol1) + (y)) / (kol - kol1 + kol2)
            break
print("надо получить",i,'<5>',"и",q,"<4>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum< 2.5:
    i=0
    q=0
    while sum<2.509  and z>sum:
        i=i+1
        sum = (sum * (kol - kol1) + (z)) / (kol - kol1 + kol2)
        while sum<2.509 and y>sum:
            q=q+1
            sum = (sum * (kol - kol1) + (y)) / (kol - kol1 + kol2)
            break
print("надо получить",i,'<3>',"и",q,"<4>","для",round(sum,2))
sum = eval(s) / (kol - kol1)


if sum< 2.5:
    i=0
    q=0
    while sum<2.509:
        i=i+1
        sum = (sum * (kol - kol1) + (x)) / (kol - kol1 + kol2)
        while sum<2.509 and z>sum:
            q=q+1
            sum = (sum * (kol - kol1) + (z)) / (kol - kol1 + kol2)
            break
print("надо получить",i,'<5>',"и",q,"<3>","для",round(sum,2))
sum = eval(s) / (kol - kol1)