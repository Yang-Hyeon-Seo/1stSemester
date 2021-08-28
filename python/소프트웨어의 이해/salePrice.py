def salePrice(price, rate):
    result = price*(1-rate/100)
    return result

print(salePrice(48000,30))
#매개변수, 가격 : price, 할인율 : rate
