class Cart():
    listCourse = []

    def __init__(self) -> None:
        self.Calculate = Calculate_Price(listCourse)
        self.totalPrice = self.Calculate.totalPrice()

    def addCourse():
        listCourse.append()

class Course():






oop.setCoupon

class Calculate_Price():
    
    def __init__(self,listCourse) -> None:
        self.listCourse =  listCourse


    def totalPrice():
        totalPrice = 0
        for course in self.listCourse :
            totalPrice  +=  course.price
        return totalPrice