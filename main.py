7
matn = "Salom dunyo"
uzunlik = len(matn)
print(matn(uzunlik // 2))

8
i = input("matn kirit: ")

if i[0] == "a" or i[0] == "A":
    print("YES")
else:
    print("NO")

9
matn = "salom dunya"
print(matn.count("a"))

10
matn = "Salom"
print(matn)

for i in range(len(matn), -1, -1):
    print(matn[i], end=" ")

11
ism = "Jamshid"
fam = "Yangiboev"

print(ism + fam)
