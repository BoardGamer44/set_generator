def generate_set(feature_number=4,feature_variety=3):
#    функция генерирует массив кодов, определяющих изображение на картах, т.к. для целей игры
#    вариативность каждого признака должна быть одинаковой - процесс похож на перечисление всех чисел
#    системы счисления с основанием feature_variety (по умолчанию - троичная система счисления)
#    feature_number число признаков(разрядность, возможные варианты - 4(по умолчанию) и 3(только зеленый цвет))
#    feature_variety вариативность признаков(основание системы счисления, минимум 2, 
#   максимум - максимальное число методов в классе Card(пока 3), теоритический максимум алгоритма - 9)
    code_of_set_list=[0 for i in range(feature_variety**feature_number)] # массив кодов(число возможных вариаций чисел в заданной разрядности)
    append_list=[0 for i in range(feature_number)] # массив приращений(нужен для работы механизма переноса разряда)
    start_code_value=int('1'*feature_number) # стартовое значение(нулевое число системы счисления с учетом разрядов, в данном случае - 1111)
    code_counter=0 # счетчик массива кодов
    while feature_variety**feature_number>code_counter: # цикл четырехразрядного приращения feature_variety-ричной системы счисления
        # выполнять пока не достигнуто максимальное число комбинаций(максимальное число в системе отсчета)
        code_of_set_list[code_counter]=start_code_value
        for i in range(feature_number): # цикл приращения
            code_of_set_list[code_counter]+=append_list[i] 
        code_counter+=1
        append_list[feature_number-1]+=1
        for j in range(feature_number-1): # цикл переноса разряда с права на лево
            if append_list[feature_number-1-j]==feature_variety*(int(round(0.1**(-j), 1))):
                append_list[feature_number-1-j]=0
                append_list[feature_number-2-j]+=(int(round(0.1**(-j-1), 1)))
    return code_of_set_list
