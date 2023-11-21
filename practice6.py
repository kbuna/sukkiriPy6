# 6-1
a = "Python"
b = [1,3,5]
class MyClass:
    def hello(self):
        print("Hello" + a)
c = MyClass()
c.hello()
"""
a str型 不変オブジェクト
b list型 可変オブジェクト
c 関数型 可変オブジェクト

"""
print()

# 6-2
x = ["ABC"]
y = [input()]
print(x[0] == y[0])
print(id(x[0]) == id(y[0]))
y = x
y[0] = "XYZ"

print(x[0])
"""
True
    等価判定で同じ 値が同じ
False
    等値判定で違う identityが違う
XYZ
    書き換えが生じる
"""

#6-3
def welcome(u):
    print(f"ようこそ{(u['name'])}さん")
    u['age'] = u['age'] +1
    print(f"あなたは来年{(u['age'])}歳だから大吉です！！")

username = input("名前を入力してください >>")
userage = int(input("年齢を入力してください >>"))
user = {'name':username,'age':userage}
copied_user = user.copy()
welcome(copied_user)
print(f"{(user['age'])}歳の{user['name']}さん、またプレイしてくださいね")

"""
welcomeが呼び出されたときに、
userageを、userディクショナリに入れて、関数に送り
関数の側では、そのageに入れて、新たにu[age]を作ろうとしているが

u['age']の中には、userのidが入っており、
参照元に+1したあと、表示している。

そのため、別々に分けたと思就ているuser[age]という風に指定したときも
+1した値が表示されてしまう。

"""

