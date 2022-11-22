from abc import ABC, abstractmethod
class Borrow(ABC):
    def borrowstaff(self):
        pass
    def borrowsturdent(self):
        pass
class Magazines(Borrow):
    magazines={
        "magazines1":"0",
        "magazines2":"0",
        "magazines3":"0",
    }
    def borrowstaff(self):
        pass
    def borrowsturdent(self):
        print("you cannot borrow this item")

class books(Borrow):
    books={
        "book1":"0",
        "book2":"0",
        "book2":"0",
    }
    def borrowstaff(self):
        pass
    def borrowsturdent(self):
        pass

class SolutionManuels(Borrow):
    solutions={
        "solution1":"0",
        "solution2":"0",
        "solution3":"0",    
    }
    def borrowstaff(self):
        pass
    def borrowsturdent(self):
        print("you cannot borrow this item")

class Cds(Borrow):
    cd={
        "cd1":"0",
        "cd2":"0",
        "cd3":"0",
    }
    def borrowstaff(self):
        pass
    def borrowsturdent(self):
        pass

class Register():
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.maxBook=3
        self.maxLandingDay=5
        self.penaltyCost

class Student(Register):
    def __init__(self,name,id):
        self.name = name
        self.id=id
        self.maxBook=3
        self.maxLandingDay=5
        self.day
    take = {}
    def pencost(self, day):
        return day.get() * self.penaltyCost
    def take(self, type):
        if type == 0:
            take = {"SolutionManuels":"Book1"}
        elif type == 1:
            take = {"Books":"Book1"}
        elif type == 2:
            take = {"Cds":"CD1"}
        else :
            take = {"Manuals": "Manual1"}
class AcademicStaff(Register):
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.maxBook = 3
        self.maxLandingDay = 5
        self.day


