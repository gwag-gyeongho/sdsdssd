class person :
    def __init__(self, name, age, height, weight):
        self.m_name = name
        self.m_age = age
        self.m_height = height
        self.m_weight = weight

    def greeting(self):
        print('안녕하세요 저는', self.m_name, '입니다')
    def HappyBirthday(self):
        self.m_age+=1

james = person('홍길동', 27, 185, 74)
james.greeting()
print(james.m_age)
print(james.m_height)
print(james.m_weight)
james.HappyBirthday()

