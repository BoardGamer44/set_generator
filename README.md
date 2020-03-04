<h1>Генератор сетов</h1>

Существуют настольные игры, основной механикой которых является поиск комбинаций карт с различающимися или совпадающими признаками.\
Например Ётта https://tesera.ru/game/IOTA/ или Сет https://tesera.ru/game/set/. В качестве примера далее используется Сет.\
На каждой карте есть изображение содержащее в себе четыре признака в одном из трех вариантов.

![пример1](https://github.com/BoardGamer44/set_generator/blob/master/drw3.jpg)\
Левая карты - один зеленый пустой ромб, средняя карта - две синие штрихованные кривули, правая карта - три красных залитых овала. Вместе они составляют набор в котором все 4 признака различаются.
Каждая карта уникальна, их количество можно вычислить по формуле вариативность_признаков^число_признаков=3^4=81 карта.

**Причины по которым я работаю над этим проектом:**\
Мне не мне не понравился дизайн игры.\
Люди с разными вариантами цветовой слепотой могут испытывать проблемы при определении цвета.\
Названия цветов и форм фигур могут быть слишком длинными в различных языках.\
Возможность создавать новые варианты игры путем изменения числа и вариативности признаков.\
Прокачка навыков програмирования.

**Описание проекта**\
Set Generator создает файл векторной графики(swg), содержащий карты 64x90мм готовые для распечатки на формате A4.\
На данный момент дизайн выглядит так:\
![пример2](https://github.com/BoardGamer44/set_generator/blob/master/drw4.jpg)\
Левая карта - один зеленый полу залитый круг, средняя карта один зеленый полу залитый крест, правая карт - один зеленый полу залитый квадрат. Вместе они составляют набор в котором три признака совпадают, один(форма) различается.\
Вместо штриховки используется заливка градиентом от белого до целевого цвета. Контуры фигур толще и имеют более темный оттенок. Фигуры имеют четырехстороннюю симметрию.

На данный момент можно изменением ключевых переменных относительно легко менять генерацию в следующих аспектах:\
генерировать сеты 3^4, 2^4, 3^3, 2^3\
менять цвета заливки и контуров фигур в формате RGB,\
менять размер фигур и карт,\
немного сложнее менять форму фигур.

**В планах:**\
увеличить число и вариативность признаков,\
генерировать сеты от 2^2 до 5^5,\
графический интерфейс,\
конвертирование в другие форматы графики,\
русская и английская документация,\
оптимизация кода.

**Библиотеки необходимые для работы**\
svgwrite 1.3.1
