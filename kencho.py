prefectures = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨木県', '栃木県', '群馬県', '埼玉県', '千葉県',
                '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県',
                '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県',
                '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']
prefecturesEN = ['Hokkaidō', 'Aomori', 'Iwate', 'Miyagi', 'Akita', 'Yamagata', 'Fukushima', 'Ibaraki', 'Tochigi', 'Gunma',
                    'Saitama', 'Chiba', 'Tōkyō', 'Kanagawa', 'Niigata', 'Toyama', 'Ishikawa', 'Fukui', 'Yamanashi', 'Nagano',
                    'Gifu', 'Shizuoka', 'Aichi', 'Mie', 'Shiga', 'Kyōto', 'Ōsaka', 'Hyōgo', 'Nara', 'Wakayama', 'Tottori',
                    'Shimane', 'Okayama', 'Hiroshima', 'Yamaguchi', 'Tokushima', 'Kagawa', 'Ehime', 'Kōchi', 'Fukuoka', 'Saga',
                    'Nagasaki', 'Kumamoto', 'Ōita', 'Miyazaki', 'Kagoshima', 'Okinawa']
capitals = ['札幌市', '青森市', '盛岡市', '仙台市', '秋田市', '山形市', '福島市', '水戸市', '宇都宮市', '前橋市', 'さいたま市', '千葉市',
                '新宿区', '横浜市', '新潟市', '富山市', '金沢市', '福井市', '甲府市', '長野市', '岐阜市', '静岡市', '名古屋市', '津市',
                '大津市', '京都市', '大阪市', '神戸市', '奈良市', '和歌山市', '鳥取市', '松江市', '岡山市', '広島市', '山口市', '徳島市',
                '高松市', '松山市', '高知市', '福岡市', '佐賀市', '長崎市', '熊本市', '大分市', '宮崎市', '鹿児島市', '沖縄市']
capitalsEN = ['Sapporo', 'Aomori', 'Morioka', 'Sendai', 'Akita', 'Yamagata', 'Fukushima', 'Mito', 'Utsunomiya', 'Maebashi',
                'Saitama', 'Chiba', 'Shinjuku', 'Yokohama', 'Niigata', 'Toyama', 'Kanazawa', 'Fukui', 'Kōfu', 'Nagano', 'Gifu',
                'Shizuoka', 'Nagoya', 'Tsu', 'Ōtsu', 'Kyoto', 'Osaka', 'Kobe', 'Nara', 'Wakayama', 'Tottori', 'Matsue', 'Okayama',
                'Hiroshima', 'Yamaguchi', 'Tokushima', 'Takamatsu', 'Matsuyama', 'Kōchi', 'Fukuoka', 'Saga', 'Nagasaki',
                'Kumamoto', 'Ōita', 'Miyazaki', 'Kagoshima', 'Okinawa']

while True:
    print ('Type 1 for Kanji only. Type 2 for Kanji with romaji')

    gameType = input("")
    gameType = int(gameType)

    problems = input("Number of Problems: ")
    problems = int(problems)

    questionNumber = 0

    def generateProblem():
        #generate random question number
        from random import randint
        questionNumber = randint(0, len(prefectures)-1)
        return questionNumber

    if (gameType == 1):

        print('これから表示される都道府県の県庁所在地を当ててください。好きなキーを押せば答えが表示されます。')

        for i in range(problems):

            print(prefectures[generateProblem()])

            answerinput = input("")

            # show answer after pressing enter
            print(capitals[generateProblem()])

    elif (gameType == 2):

        print('これから表示(hyōji)される都道府県(todōfuken)の県庁所在地(kenchōshozaichi)を当ててください。好きなキーを押せば答えが表示されます。')

        for i in range(problems):

            print(prefectures[generateProblem()] + "(" + prefecturesEN[generateProblem()] + ")")

            answerinput = input("")

            # show answer after pressing enter
            print(capitals[generateProblem()] + "(" + capitalsEN[generateProblem()] + ")")

    else:
        print("else")

