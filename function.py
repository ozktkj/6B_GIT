#消費税の計算関数
# 金額は整数
# 税率は少数 10％ → 0.1
def add_tax(price, tax_rate):
    return int(price + price * tax_rate)

if __name__ == "__main__":
    assert add_tax(1000,0.1) == 1100 #一般
    assert add_tax(1000,0.08) == 1080 # 軽減税率