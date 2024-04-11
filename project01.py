#a = input() #暫停等待使用者輸入字串
#a = int(input("請輸入一個數字")) #把輸入字串轉換成整數
#print(a)

#輸入
#性別 男女 
gender = input("你是(生理男/生理女)～？ ")
#年齡 age int
age = int(input("你幾歲啊～？ "))
#身高（公分）/100 ＝公尺  height float
height = float(input("身高幾公分？ "))
#體重（公斤) weight float
weight = float(input("偷偷告訴我你幾公斤? "))
#體脂率（百分比) fat float
fat = float(input("體脂計上面寫多少（％）"))
#活動因子 act float
act = float(input("你平常動次動程度呢～？每週運動1-3天是1.375; 3-5天是1.55; 6-7天是1.725; 整天都運動1.9。 "))
#壓力因子 stress float
stress = float(input("壓力山小吧？正常是1.0, 發燒1.13,懷孕是1.1,還有很多，自己上網查。 "))

#輸出
#BMI
BMI = round(weight / ((height/100)**2),1) 
#除脂體重
wei_nofat = round(weight*(100-fat)*0.01, 1)
#體重狀態（是否超重）由BMI判斷
if BMI < 18.5:
    BMI_stat = "太輕囉～"
elif 18.5 <= BMI < 24:
    BMI_stat = "你很棒！剛剛好！"
elif 24 <= BMI:
    BMI_stat = "超過健康標準囉～"
#基礎代謝率（BMR）if 生理男 生理女
if gender == "生理男":
    BMR = round(66 + (13.7*weight + 5*height - 6.8*age),1)
elif gender == "生理女":
    BMR = round(655 + (9.6*weight + 1.8*height - 4.7*age),1)
#總熱量消耗（TDEE)
TDEE = round(BMR * act * stress,1)

#低碳飲食法三大營養素的建議克數
#熱量Car20% Pro30% Fatt50%
carb = TDEE * 0.2
protein = TDEE * 0.3
fat = TDEE * 0.5
#克數 Carb/4 Protein/4 Fatt/9
carb_g = round(carb / 4, 1)
protein_g = round(protein / 4, 1)
fat_g = round(fat / 9, 1)

print("")
print("⭑你的身體現在狀況⭑")
print("BMI是:", BMI)
print("去掉脂肪的體重是:",wei_nofat)
print("體重狀態:", BMI_stat)
print("基礎代謝率:",BMR, "大卡")
print("現在每天的總熱量消耗:", TDEE, "大卡")
print("在低碳飲食法中，建議的三大營養素建議克數是")
print("碳水化合物:", carb_g, "g")
print("蛋白質:", protein_g, "g")
print("脂肪:",fat_g, "g")