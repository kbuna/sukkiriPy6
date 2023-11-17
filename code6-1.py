# 6-1
tpl = "3人目は{}さん"
names = ["松田","浅木"]
names.append("工藤")
massage = tpl.format(names[2])
print(massage)

# 6-3
userinfo = input("名前と血液型をカンマで区切って1行で入力>>")
[name,blood] = userinfo.split(",")
blood = blood.upper().strip()
print(f"{name}さんは{blood}")

