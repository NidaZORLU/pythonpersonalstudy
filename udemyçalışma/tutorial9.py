class Person:
    """:3 tırnak veya tek tırnak.. 
    burası class açıklaması,burayı görüntülemek için;
    print(Person.__doc__)
    """

    def __init__(self):
        "burası method açıklaması"
        print('class oluşturuldu')
        print('burası sınıf örneği oluşturulursa otomatik olarak çalışır...')

    def __str__(self):
        "burası method açıklaması"
        return "burası açıklama yeri"

    def deneme1(self):
        "burası method açıklaması"
        print("burası örneğe ait method")

    @classmethod
    def deneme2(cls):
        "burası class method açıklaması"
        print("burası class method")

    @staticmethod
    def deneme3():
        "burası static method açıklaması"
        print("burası static method")
