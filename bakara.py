
import random
import math

#カードをつくる
cards = {1: "♡1", 2:"♡2", 3:"♡3", 4:"♡4", 5:"♡5", 6:"♡6", 7:"♡7", 8:"♡8", 9:"♡9", 10:"♡10", 11:"♡j", 12:"♡q", 13:"♡k", 
        14:"♢1", 15:"♢2", 16:"♢3", 17:"♢4", 18:"♢5", 19:"♢6", 20:"♢7", 21:"♢8", 22:"♢9", 23:"♢10", 24:"♢j", 25:"♢q", 26:"♢k", 
        27:"♧1", 28:"♧2", 29:"♧3", 30:"♧4", 31:"♧5", 32:"♧6", 33:"♧7", 34:"♧8", 35:"♧9", 36:"♧10", 37:"♧j", 38:"♧q", 39:"♧k", 
        40:"♤1", 41:"♤2", 42:"♤3", 43:"♤4", 44:"♤5", 45:"♤6", 46:"♤7", 47:"♤8", 48:"♤", 49:"♤10", 50:"♤j", 51:"♤q", 52:"♤k"}

#トランプを数字に変換
number= {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:0, 11:0, 12:0, 13:0, 
        14:1, 15:2, 16:3, 17:4, 18:5, 19:6, 20:7, 21:8, 22:9, 23:0, 24:0, 25:0, 26:0, 
        27:1, 28:2, 29:3, 30:4, 31:5, 32:6, 33:7, 34:8, 35:9, 36:0, 37:0, 38:0, 39:0, 
        40:1, 41:2, 42:3,43:4, 44:5, 45:6, 46:7, 47:8, 48:9, 49:0, 50:0, 51:0, 52:0}

#関数化
#num = トランプの番号(cards関数のキー)：1〜52
#atai = トランプの種類(cards関数の値)：ハート1
#card = トランプの種類：ハート1
#suuji = トランプの数字：1:1 ~ 52:0 の右　(カードを数字に変換)

#cards
def num_atai():
    num,atai = random.choice(list(cards.items()))
    return num,atai

#cardsから削除
def card_kansuu(num):
    card = cards.pop(num)
    return card                                                                                                             

#numberから削除
def suuji_kansuu(num):
    suuji = number.pop(num)
    return suuji

#カードを引く
def namae():
    num,atai = num_atai()
    card = card_kansuu(num)
    suuji = suuji_kansuu(num)
    return card,suuji

#一の位を出す
def iti(suuji_k1,suuji_k2):
    goukei = suuji_k1+suuji_k2
    if 10 <= goukei <= 19:
        goukei = goukei - 10
    return suuji_k1,suuji_k2,goukei


#結果、手持ち計算
cls_kake = {"タイ":9,"プレイヤー":2,"バンカー":1.95}
def kekka(select,kake,temoti,hantei2):
    if hantei2 == select:
        temoti = temoti + kake*cls_kake[select]
        temoti = math.floor(temoti)
        print( "結果：" + hantei2 )
        print(f"予想があたり、賭け金が{str(cls_kake[select])}倍になりました。あなたの手持ちは{str(temoti)}円です。")
        print()
    else:
        temoti = temoti - kake
        print( "結果：" + hantei2 )
        print(f"予想が外れました。あなたの手持ちは{str(temoti)}円です。")
        print()
    return temoti

#勝敗判定
def hantei(pla_goukei,ban_goukei,temoti):
    if pla_goukei == ban_goukei:
        # temoti = tai(s_text,kake,temoti)
        kekka(select,kake,temoti,"タイ")
    elif pla_goukei >= ban_goukei:
        # temoti = player(s_text,kake,temoti)
        kekka(select,kake,temoti,"プレイヤー")
    else:
        # temoti = banker(s_text,kake,temoti)
        kekka(select,kake,temoti,"バンカー")
    return temoti


print()
print("バカラを開始します。")
print()

#バンカー、プレイヤー、タイを選ぶ
print("バンカー or プレイヤー or タイ のどれに賭けますか？")

#例外処理なし
select = input()
print("あなたは"+select+"に賭けました。")

#所持金100000円(10万)
#賭け金を入力してもらう
print("あなたの所持金は100000円(10万円)です。いくら賭けますか？")
temoti = 100000
kake = int(input())

#playerの手札(2枚)
card1,suuji1 = namae()
card2,suuji2 = namae()
#一の位を出す
suuji1,suuji2,pla_goukei = iti(suuji1,suuji2)
print(f"プレイヤーのカード：{card1}・{card2}、合計後の一の位：【{str(pla_goukei)}】")


#bankerの手札(2枚)
card3,suuji3 = namae()
card4,suuji4 = namae()
#一の位を出す
suuji3,suuji4,ban_goukei = iti(suuji3,suuji4)
print(f"バンカーのカード：{card3}・{card4}、合計後の一の位：【{str(ban_goukei)}】")
print()


#ナチュラルウィン
if pla_goukei >= 8 and pla_goukei == ban_goukei:
    print("タイです。")
    print()
    hantei2 = "タイ"
    temoti = kekka(select,kake,temoti,hantei2)
    

elif ban_goukei == 8 or ban_goukei == 9:
    if ban_goukei > pla_goukei:
        print("ナチュラルウィン！バンカーの勝ちです。")
        print()
        hantei2 = "バンカー"
        temoti = kekka(select,kake,temoti,hantei2)
    elif pla_goukei > ban_goukei:
        print("ナチュラルウィン！プレイヤーの勝ちです。")
        print()
        hantei2 = "プレイヤー"
        temoti = kekka(select,kake,temoti,hantei2)


elif pla_goukei == 8 or pla_goukei == 9:
    print("ナチュラルウィン！プレイヤーの勝ちです。")
    print()
    hantei2 = "プレイヤー"
    temoti = kekka(select,kake,temoti,hantei2)


#playerが6か7の場合
elif pla_goukei == 6 or pla_goukei == 7:
    if 0 <= ban_goukei <= 5:
        card_2,suuji_2 = namae()
        ban_goukei,suuji_2,ban_goukei3 = iti(ban_goukei,suuji_2)
        print("プレイヤーの数字が【6,7】の場合、プレイヤーはカードを引けません。")
        print()
        print("バンカーの数字が【0〜5】のため、バンカーがカードを1枚引きました。")
        print(f"バンカーが引いたカード：{card_2}、合計後の一の位：【{ban_goukei3}】です。")
        print()
        hantei(pla_goukei,ban_goukei3,temoti)
    elif ban_goukei >= 6:
        print("プレイヤーの数字が【6,7】の場合、プレイヤーはカードを引けません。")
        print("バンカーの数字が【6〜9】の場合、バンカーはカードを引けません。")
        print()
        hantei(pla_goukei,ban_goukei,temoti)


#playerが0〜5の場合
elif 0 <= pla_goukei <= 5:
    card_1,suuji_1 = namae()
    pla_goukei,suuji_1,pla_goukei3 = iti(pla_goukei,suuji_1)
    print("プレイヤーの数字が【0〜5】のため、プレイヤーがカードを1枚引きました。")
    print(f"プレイヤーのカード：{card1}・{card2}・{card_1}、合計後の一の位：【{str(pla_goukei3)}】")
    print()


    #プレイヤーの3枚目が【0,1】の場合
    #バンカーの手札の合計が【0〜3】の場合のみ3枚目を引く
    if suuji_1==0 or suuji_1==1:
        if 0<=ban_goukei<=3:
            card_2,suuji_2 = namae()
            ban_goukei,suuji_2,ban_goukei3 = iti(ban_goukei,suuji_2)
            print("プレイヤーの3枚目の数字が【0,1】バンカーの数字が【0〜3】のため、バンカーがカードを1枚引きました。")
            print()
            print(f"バンカーのカード：{card3}・{card4}・{card_2}、合計後の一の位：【{str(ban_goukei3)}】")
            print()
            hantei(pla_goukei3,ban_goukei3,temoti)
        else:
            print("プレイヤーの3枚目の数字は【0,1】ですが、バンカーの数字が【0〜3】ではないため、バンカーはカードを引けません。")
            print()
            hantei(pla_goukei3,ban_goukei,temoti)


    #プレイヤーの3枚目が【2,3】の場合
    #バンカーの手札の合計が【0〜4】の場合のみ3枚目を引く
    elif suuji_1==2 or suuji_1==3:
        if 0<=ban_goukei<=4:
            card_2,suuji_2 = namae()
            ban_goukei,suuji_2,ban_goukei3 = iti(ban_goukei,suuji_2)
            print("プレイヤーの3枚目の数字が【2,3】バンカーの数字が【0〜4】のため、バンカーがカードを1枚引きました。")
            print(f"バンカーのカード：{card3}・{card4}・{card_2}、合計後の一の位：【{str(ban_goukei3)}】")
            print()
            hantei(pla_goukei3,ban_goukei3,temoti) 
        else:
            print("プレイヤーの3枚目の数字は【2,3】ですが、バンカーの数字が【0〜4】ではないため、バンカーはカードを引けません。")
            print()
            hantei(pla_goukei3,ban_goukei,temoti)


    #プレイヤーの3枚目が【4,5】の場合
    #バンカーの手札の合計が【0〜5】の場合のみ3枚目を引く
    elif suuji_1==4 or suuji_1==5:
        if 0<=ban_goukei<=5:
            card_2,suuji_2 = namae()
            ban_goukei,suuji_2,ban_goukei3 = iti(ban_goukei,suuji_2)
            print("プレイヤーの3枚目の数字が【4,5】バンカーの数字が【0〜5】のため、バンカーがカードを1枚引きました。")
            print(f"バンカーのカード：{card3}・{card4}・{card_2}、合計後の一の位：【{str(ban_goukei3)}】")
            print()
            hantei(pla_goukei3,ban_goukei3,temoti)
  
        else:
            print("プレイヤーの3枚目の数字は【4,5】ですが、バンカーの数字が【0〜5】ではないため、バンカーはカードを引けません。")
            print()
            hantei(pla_goukei3,ban_goukei,temoti)
          

    #プレイヤーの3枚目が【6,7】の場合
    #バンカーの手札の合計が【0〜6】の場合のみ3枚目を引く
    elif suuji_1==6 or suuji_1==7:
        if 0<=ban_goukei<=6:
            card_2,suuji_2 = namae()
            ban_goukei,suuji_2,ban_goukei3 = iti(ban_goukei,suuji_2)
            print("プレイヤーの3枚目の数字が【6,7】バンカーの数字が【0〜6】のため、バンカーがカードを1枚引きました。")
            print(f"バンカーのカード：{card3}・{card4}・{card_2}、合計後の一の位：【{str(ban_goukei3)}】")
            print()
            hantei(pla_goukei3,ban_goukei3,temoti)
        else:
            print("プレイヤーの3枚目の数字は【6,7】ですが、バンカーの数字が【0〜6】ではないため、バンカーはカードを引けません。")
            print()
            hantei(pla_goukei3,ban_goukei,temoti)


    #プレイヤーの3枚目が【8】の場合
    #バンカーの手札の合計が【0〜3】の場合のみ3枚目を引く
    elif suuji_1==8:
        if 0<=ban_goukei<=3:
            card_2,suuji_2 = namae()
            ban_goukei,suuji_2,ban_goukei3 = iti(ban_goukei,suuji_2)
            print("プレイヤーの3枚目の数字が【8】バンカーの数字が【0〜3】のため、バンカーがカードを1枚引きました。")
            print(f"バンカーのカード：{card3}・{card4}・{card_2}、合計後の一の位：【{str(ban_goukei3)}】")
            print()
            hantei(pla_goukei3,ban_goukei3,temoti)
        else:
            print("プレイヤーの3枚目の数字は【8】ですが、バンカーの数字が【0〜3】ではないため、バンカーはカードを引けません。")
            print()
            hantei(pla_goukei3,ban_goukei,temoti)
            

    #プレイヤーの3枚目が【9】の場合
    #バンカーの手札の合計が【0〜4】の場合のみ3枚目を引く
    elif suuji_1==9:
        if 0<=ban_goukei<=4:
            card_2,suuji_2 = namae()
            ban_goukei,suuji_2,ban_goukei3 = iti(ban_goukei,suuji_2)
            print("プレイヤーの3枚目の数字が【9】バンカーの数字が【0〜4】のため、バンカーがカードを1枚引きました。")
            print(f"バンカーのカード：{card3}・{card4}・{card_2}、合計後の一の位：【{str(ban_goukei3)}】")
            print()
            hantei(pla_goukei3,ban_goukei3,temoti)
            
        else:
            print("プレイヤーの3枚目の数字は【9】ですが、バンカーの数字が【0〜4】ではないため、バンカーはカードを引けません。")
            print()
            hantei(pla_goukei3,ban_goukei,temoti)
