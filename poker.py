import random
import math


numbers = {1: '2', 2:'3', 3:'4', 4:'5', 5:'6', 6:'7',7: '8',8: '9', 9:'10', 10:'J', 11:'Q', 12:'K',13:'A'}
kigou = ['spade','heart','diamond','club']


#関数化
#key = トランプの番号(numbers関数のキー)：1〜13
#atai = トランプの種類(numbers関数の値)：1〜10、JQK
#card = トランプの種類：ハート1

#numbersからキーと値をランダムで取り出す
def key_atai():
    key,atai = random.choice(list(numbers.items()))
    return key,atai


#numbersから削除
def number_delete(key):
    card = numbers.pop(key)
    return card                                                                                                             

#カードを引く
def namae():
    #kigouから記号をランダムで取り出す(重複なし)
    n = random.randint(0,3)
    symbol = kigou[n]

    key,atai = key_atai()
    card = number_delete(key)
    cards = f"{symbol}.{atai}"
    return cards
    

print()
print("ポーカーを開始します。")

def gomai():
    card1 = namae()
    card2 = namae()
    if card1 == card2:
        card3 = namae()

    card3 = namae()
    if card1==card3 or card2==card3:
        card4 = namae()

    card4 = namae()
    if card1==card4 or card2==card4 or card3==card4:
        card5 = namae()
    card5 = namae()
    return card1,card2,card3,card4,card5


#playerの手札(5枚)
pla_card1, pla_card2,pla_card3,pla_card4,pla_card5= gomai()
print("プレイヤーの手札【1:"+pla_card1+"　2:"+pla_card2+"　3:"+pla_card3+"　4:"+pla_card4+" 5:"+pla_card5+" 】")
print()

#computerの手札(5枚)
com_card1,com_card2,com_card3,com_card4,com_card5 = gomai()

#プレイヤーが手札を変更するか
print("手札を変更しますか？ yes / no (全て小文字で記入してください。)")
situmon = input()
if situmon == "yes":
    print("どのカードを変更しますか？ 1〜5 (何枚でも可能です。変更したい番号を全て記入してください。)")
    henkou = input()




