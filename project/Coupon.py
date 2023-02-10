class Coupon():
    def __init__(self, id, passcode, start_date, end_date):
        self._id = id
        self._passcode = passcode
        self._start_date = start_date
        self._end_date = end_date
        
class CouponCourse(Coupon):
    def __init__(self, id, passcode, start_date, end_date, condition, target):
        super().__init__(id, passcode, start_date, end_date)
        self.__target = target
        self.__condition = condition

class CouponInstructor(Coupon):
    def __init__(self, id, passcode, start_date, end_date, condition, target):
        super().__init__(id, passcode, start_date, end_date)
        self.__target = target
        self.__condition = condition

class CouponAll(Coupon):
    def __init__(self, id, passcode, start_date, end_date, condition, target):
        super().__init__(id, passcode, start_date, end_date)
        self.__target = target
        self.__condition = condition