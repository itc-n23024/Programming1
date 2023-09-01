class Person:
    def __init__(self, name="", nationary="", birth="", address=""):
        self.name = name
        self.nationary = nationary
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationary)
        print("生年:", self.birth)
        print("住所:", self.address)


unko = Person("足", "中国", "9999999999", "天国")
print(unko.show_attributes())
