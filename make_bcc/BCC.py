rcc = 20  # C_C間距離(nm)
rch = 0.109  # C_H間距離(nm)
a = rcc/3**0.5
b = rcc/3**0.5
x = 22  # 箱の基準長さ
met = 1  # メタンの通し番号
atom = 1 # 原子の通し番号

print("methane")
print(x**3)
for i in range(2*x):
    for j in range(int(x/2)):
        for k in range(int(x/2)):
            print(" "*(5-len(str(met)))+f"{met}MET", " C", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i, 3)))))+str('{:.3f}'.format(round(2*a*i, 3))),\
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j, 3)))))+str('{:.3f}'.format(round(2*a*j, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k, 3)))))+str('{:.3f}'.format(round(2*a*k, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i+b, 3)))))+str('{:.3f}'.format(round(2*a*i+b, 3))),\
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j+b, 3)))))+str('{:.3f}'.format(round(2*a*j+b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k+b, 3)))))+str('{:.3f}'.format(round(2*a*k+b, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i+b, 3)))))+str('{:.3f}'.format(round(2*a*i+b, 3))),\
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j-b, 3)))))+str('{:.3f}'.format(round(2*a*j-b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k-b, 3)))))+str('{:.3f}'.format(round(2*a*k-b, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i-b, 3)))))+str('{:.3f}'.format(round(2*a*i-b, 3))),\
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j+b, 3)))))+str('{:.3f}'.format(round(2*a*j+b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k-b, 3)))))+str('{:.3f}'.format(round(2*a*k-b, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i-b, 3)))))+str('{:.3f}'.format(round(2*a*i-b, 3))),\
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j-b, 3)))))+str('{:.3f}'.format(round(2*a*j-b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k+b, 3)))))+str('{:.3f}'.format(round(2*a*k+b, 3))))
            atom += 1
            met += 1
    for j in range(int(x/2)):
        for k in range(int(x/2)):
            print(" "*(5-len(str(met)))+f"{met}MET", " C", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i+a, 3)))))+str('{:.3f}'.format(round(2*a*i+a, 3))), \
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j+a, 3)))))+str('{:.3f}'.format(round(2*a*j+a, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k+a, 3)))))+str('{:.3f}'.format(round(2*a*k+a, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i+a+b, 3)))))+str('{:.3f}'.format(round(2*a*i+a+b, 3))), \
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j+a+b, 3)))))+str('{:.3f}'.format(round(2*a*j+a+b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k+a+b, 3)))))+str('{:.3f}'.format(round(2*a*k+a+b, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i+a+b, 3)))))+str('{:.3f}'.format(round(2*a*i+a+b, 3))), \
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j+a-b, 3)))))+str('{:.3f}'.format(round(2*a*j+a-b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k+a-b, 3)))))+str('{:.3f}'.format(round(2*a*k+a-b, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i+a-b, 3)))))+str('{:.3f}'.format(round(2*a*i+a-b, 3))), \
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j+a+b, 3)))))+str('{:.3f}'.format(round(2*a*j+a+b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k+a-b, 3)))))+str('{:.3f}'.format(round(2*a*k+a-b, 3))))
            atom += 1
            print(" "*(5-len(str(met)))+f"{met}MET", " H", " "*(6-len(str(atom)))+str(atom),\
                " "*(9-len(str('{:.3f}'.format(round(2*a*i+a-b, 3)))))+str('{:.3f}'.format(round(2*a*i+a-b, 3))), \
                    " "*(8-len(str('{:.3f}'.format(round(2*a*j+a-b, 3)))))+str('{:.3f}'.format(round(2*a*j+a-b, 3))),\
                        " "*(8-len(str('{:.3f}'.format(round(2*a*k+a+b, 3)))))+str('{:.3f}'.format(round(2*a*k+a+b, 3))))
            atom += 1
            met += 1
print(round(4*x*a, 5), round(x*a, 5), round(x*a, 5))