class User:
    def __init__(self, name, age, hobbies,cuisine, diet) -> None:
        self.name = name
        self.age = age
        self.hobbies = hobbies
        self.cusuine = cuisine
        self.diet = diet
        self.prev_liked = []
        self.prev_disliked = []

    def get_age(self):
        return int(self.age)
    def get_name(self):
        return self.name
    def get_hobbies(self):
        return self.hobbies
    def get_diet(self):
        return self.cusuine + " with dietary restrictions including : " + self.diet
    
    def __lt__(self, other):
        return self.get_age() < other.get_age()



class AllCurrentUsers:
    def __init__(self):
        self.current = []

    def addUser(self,user):
        self.current.append(user)
    
    def youngest(self):
        return min(self.current).get_age()
    
    def toString(self, mood):
        together = ""
        count = 1
        if mood == 'food':
            for user in self.current:
                together += f'user{count} : is aged{user.get_age()} and prefers {user.get_diet()}\t'
                count += 1
        else:
            for user in self.current:
                together += f'user{count} : is aged{user.get_age()} and has the following hobbies {user.get_hobbies()}\t'
                count += 1
        return together


            


    