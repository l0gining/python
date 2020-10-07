def bmi(mass, height):
    """Вычисляет индекс массы тела по введенным массе и росту человека"""
    return (mass/((height/100)**2))

person_mass, person_height = map(float, input('Введите свою массу в килограммах и рост в сантиметрах через пробел: ').split( ))
BMI = bmi(person_mass, person_height)

if BMI < 16:
    print('Выраженный дефицит массы тела')
elif 16 <= BMI <18.5:
    print('Недостаточная масса тела')
elif 18.5 <= BMI < 25:
    print('Нормальная масса тела')
elif 25 <= BMI < 30:
    print('Избыточная масса тела')
elif 30 <= BMI < 35:
    print('Ожирение первой степени')
elif 35 <= BMI < 40:
    print('Ожирение второй степени')
elif BMI >= 40:
    print('Ожирение третьей степени')
