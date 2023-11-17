# 6-1
tpl = "3人目は{}さん"
names = ["松田","浅木"]
names.append("工藤")
massage = tpl.format(names[2])
print(massage)

# 6-2
num = 10
print(num.bit_length())
names =["松田","浅木"]
names.append("工藤")

# 6-3
userinfo = input("名前と血液型をカンマで区切って1行で入力>>")
[name,blood] = userinfo.split(",")
blood = blood.upper().strip()
print(f"{name}さんは{blood}")

print()

#6-4 リテラルやクラス名関数を用いたオブジェクトの生成
int_value1 = 0
int_value2 = int()
int_value3 = int(9)
int_value4 = []
int_value5 = list
int_value6 = list(("松田","浅木"))

def add(x,y):
    return x + y
sum = add
print(type(add))
print(sum(5,10))


print()
#6-5 オブジェクトの設計図

"""リテラルによるオブジェクト生成の指示
小数点を含まない数字 intクラスを用いてオブジェクトを生成
小数点を含む数字     float
''や""で囲まれた文字 str
[]で囲まれた文字     list
{}で囲まれた文字     {～:～}形式ならdictクラス
                    {～}ならsetクラスでオブジェクトを生成

"""

class Hero:
    name = "松田"
    hp = 100

    def __init__(self,name="松田",hp=32):
        self.name = name
        self.hp = hp

    def sleep(self,hours):
        print(f"{self.name}は{hours}時間寝た！")
        self.hp += hours
#クラスの中でも関数はグローバル関数で使わないと値にアクセスできない
#ゲーム開始
print("スッキリファンタジーⅫ ～金色の理想郷～")
h = Hero()
h.sleep(3)
print(f"{h.name}のHPは現在{h.hp}")

#オブジェクトの個々のデータは属性 attributeという
#関数はメソッド

print()

#6-6 オブジェクトのidentity
#オブジェクトは生み出されると他と重複しない整数の値がidentityとして付与される
#idで判定 等値 要素でチェック 等価
#オブジェクトを丸々変数名同じで書き換えたらidの値も変わる
scores1 = [80,40,50]
scores2 = [80,40,50]
print(f"scores1のidentity:{id(scores1)}")
print(f"scores2のidentity:{id(scores2)}")

if scores1 == scores2:
    print("scores1とscores2は同じ内容です")
else:
    print("scores1とscores2は違う内容です")

if id(scores1) == id(scores2):
    print("scores1とscores2は同じ存在です")
else:
    print("scores1とscores2は違う存在です")

print()
#6-7 リストオブジェクトのコピーによる不可解な動作
scores1 =[80,40,50]
scores2 =[80,40,50]
print(f"scores1の先頭要素は{scores1[0]}")
print(f"scores2の先頭要素は{scores2[0]}")

print(f"変数scores2の中身を変数scores1に代入します")
scores1 = scores2

print("scores1の先頭要素を90に書き換えます")
scores1[0] = 90

print(f"90を代入したscores1の先頭要素は{scores1[0]}")
print(f"90を代入したscores2の先頭要素は{scores2[0]}")


#6-8
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + "さん"
        return names
before_names = ["松田","浅木","工藤"]
after_names = add_suffix(before_names)
print("さん付け後:" + after_names[0])
print("さん付け前:" + before_names[0])
print()


#6-9 防御的コピーを用いて悪影響を防ぐ
def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + "さん"
        return names
before_names = ["松田","浅木","工藤"]
copies_names =list()
for n in before_names:
    copies_names.append(n)
    #before_names.copy()
    #berore_names[:] すべての範囲をスライス
after_names = add_suffix(copies_names)
print("さん付け後:" + after_names[0])
print("さん付け前:" + before_names[0])

print()


#6-10 不変オブジェクト
def add_suffix(name):
    name = name + "さん"
    return name
before_name = "松田"
after_name = add_suffix(before_name)
print("さん付け後:"+after_name)
print("さん付け前:"+before_name)

print()
#6-11 リストと文字列による書き換え時のidentity値の変化
names =list()
print(f"変更前のlistのidentity:{id(names)}")
names.append("松田")
print(f"変更後のlistのidentity:{id(names)}")

name="松田"
print(f"変更前のstrのidentity:{id(names)}")
name="スーパー"+name
print(f"変更後のstrのidentity:{id(names)}")



#ラムダ式 もしくはアロー関数
"""
javascriptでよくある形
() => {
}

(a,b) => a+b
"""


#

