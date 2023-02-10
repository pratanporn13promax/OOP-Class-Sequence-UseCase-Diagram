class Cart():
    def __init__(self, price, net_promotion, net_coupon, net_price):
        self.__price = price
        self.__net_promotion = net_promotion
        self.__net_coupon = net_coupon
        self.__net_price = net_price