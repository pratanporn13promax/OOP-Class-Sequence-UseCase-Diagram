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