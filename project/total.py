class User():
    def __init__(self,name,id,username,password,language,mail,about,active):
        self._name = name
        self._id = id
        self._username = username
        self._password = password
        self._language = language
        self._mail = mail
        self._about = about
        self._active = active

class Instructor(User):
    def __init__(self, name, id, username, password, language, mail, about, active, description):
        super().__init__(name, id, username, password, language, mail, about, active)
        self.__description = description

class Student(User):
    def __init__(self, name, id, username, password, language, mail, about, active, review):
        super().__init__(name, id, username, password, language, mail, about, active)
        self.__review = review

class StudentCourse():
    def __init__(self, progress):
        self.__progress = progress

class Review():
    def __init__(self, by, rating, course_name, description):
        self.__by = by
        self.__rating = rating
        self.__course_name = course_name
        self.__description = description

class Promotion():
    def __init__(self, percent, start_date, end_date, net):
        self.__percent = percent
        self.__start_date = start_date
        self.__end_date = end_date
        self.__net = net

class Payment():
    def __init__(self, country, method):
        self.__country = country
        self.__method = method
        
class Order():
    def __init__(self, id):
        self.__id = id

class Course():
    def __init__(self, id, name, short_description, date, language, purpose, content, requirement, description, target, price, info):
        self._id = id
        self._name = name
        self._short_description = short_description
        self._date = date
        self._language = language
        self._purpose = purpose
        self._content = content
        self._requirement = requirement
        self._description = description
        self._target = target
        self._price = price
        self._info = info
        
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

class CouponList():
    def __init__(self, type):
        self.__type = type

class Categories():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

class Cart():
    def __init__(self, price, net_promotion, net_coupon, net_price):
        self.__price = price
        self.__net_promotion = net_promotion
        self.__net_coupon = net_coupon
        self.__net_price = net_price