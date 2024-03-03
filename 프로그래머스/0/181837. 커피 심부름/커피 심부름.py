def solution(order):
    americano = ["americano", "iceamericano", "americanoice", "hotamericano", "americanohot", "anything"]
    cafelatte = ["cafelatte", "icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot"] 
    
    money = 0
    
    for i in order:
        if i in americano: money += 4500
        if i in cafelatte: money += 5000    
    
    return money