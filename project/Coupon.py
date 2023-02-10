class Coupon():
    def __init__(self, id, passcode, start_date, end_date):
        self.id = id
        self.passcode = passcode
        self.start_date = start_date
        self.end_date = end_date
        
class Coupon_Course(Coupon):
    def __init__(self, id, passcode, start_date, end_date, condition, target):
        super().__init__(id, passcode, start_date, end_date)
        self.target = target
        self.condition = condition

class Coupon_Instructor(Coupon):
    def __init__(self, id, passcode, start_date, end_date, condition, target):
        super().__init__(id, passcode, start_date, end_date)
        self.target = target
        self.condition = condition

class Coupon_All(Coupon):
    def __init__(self, id, passcode, start_date, end_date, condition, target):
        super().__init__(id, passcode, start_date, end_date)
        self.target = target
        self.condition = condition