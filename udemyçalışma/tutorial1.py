def person(name,age,pay_e):
    global pay_c
    print("merhaba",name)
    def calculate_pay(pay_e):
        rate_of_pay=7.5
        if age>=21:
            rate_of_pay+=2.5
        return rate_of_pay*pay_e
    pay_c=calculate_pay(pay_e)
    return pay_c

mustafa=person("mustafa",23,300)
yusuf=person("yusuf",24,600)
