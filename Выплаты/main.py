# coding: utf-8
def calculate_cost(hours_worked, hourly_rate, social_security_rate):
    gross_pay = hours_worked * hourly_rate # Брутто-зарплата
    social_security = gross_pay * social_security_rate / 100.0 
    # Отчисления на соц. страхование
    net_pay = gross_pay - social_security # Нетто-зарплата
    return gross_pay, social_security, net_pay

def main(): 
    try:
        hours_worked = float(raw_input("Введите количество проработанных часов: "))
        hourly_rate = float(raw_input("Введите почасовую ставку: "))
        social_security_rate = 30.0 # Процент отчислений на соц. страхование
        
        gross_pay, social_security, net_pay = calculate_cost(hours_worked, hourly_rate, social_security_rate)
        
        print ("Брутто-зарплата: {:.2f} руб.".format(gross_pay))
        print ("Отчисления на соц. страхование: {:.2f} pyб.".format(social_security))
        print ("Нетто-зарплата: {:.2f} руб.".format(net_pay))

    except ValueError:
        print ("Пожалуйста, введите корректные числовые значения.")

if_name_== "_main_":
main()