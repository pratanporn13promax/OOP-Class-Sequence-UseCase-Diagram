class User():
    def __init__(self,name,id,username,password,language,mail,about,active):
        self.name = name
        self.id = id
        self.username = username
        self.password = password
        self.language = language
        self.mail = mail
        self.about = about
        self.active = active

class Instructor(User):
    def __init__(self, name, id, username, password, language, mail, about, active, description):
        super().__init__(name, id, username, password, language, mail, about, active)
        self.description = description

class Student(User):
    def __init__(self, name, id, username, password, language, mail, about, active, review):
        super().__init__(name, id, username, password, language, mail, about, active)
        self.review = review