print ('Type 1 for Kanji only')

print('これから表示される都道府県の県庁所在地を当ててください。好きなキーを押せば答えが表示されます。')

prefectures = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨木県', '栃木県', '群馬県', '埼玉県', '千葉県',
                '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県',
                '滋賀県', '京都府', '大阪府', '兵庫県']
capitals = ['札幌市', '青森市', '盛岡市', '仙台市', '秋田市', '山形市', '福島市', '水戸市', '宇都宮市', '前橋市', 'さいたま市', '千葉市',
                '新宿区', '横浜市', '新潟市', '富山市', '金沢市', '福井市', '甲府市', '長野市', '岐阜市', '静岡市', '名古屋市', '津市',
                '大津市', '京都市', '大阪市', '神戸市']

#generate random question number
from random import randint
questionNumber = randint(0, len(prefectures)-1)

print(prefectures[questionNumber])

input = input("")

# show answer after pressing enter
print(capitals[questionNumber])