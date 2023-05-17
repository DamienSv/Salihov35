#1
#Представьте себе стопку книг. Вы кладете первую, на нее вторую и т.д. А теперь хотите убрать книги. Если вы уберете нижнюю - 
#то вся стопка развалится. Поэтому нужно убирать сверху. В этом и заключается тип данных Stack - куча или стопка.
#Такой способ организации данных получил название LIFO (англ. last in, first out «последним пришёл — первым ушёл»).
#Задание: Создайте класс Batary, у которой будет определен атрибут capacity = [ ] (емкость), max_charge = 5 (максимальный заряд) по умолчанию, и методы:
#charge - заряжает батарею
#discharge - разряжает батарею.
#Переопределите метод __str__, чтобы при вызове экземпляра он представлялся в виде: [)))))] - максимально заряженная батарея.
#Подсказка: можете использовать методы очень похожего стандартного типа данных. Догадались какого?
class Battery:

    def __init__(self):
        self.capacity = []
        self.max_charge = 5

    def charge(self):

        if len(self.capacity) < self.max_charge:
            self.capacity.append(')')
        print('Батарея заряжена на', len(self.capacity), 'единиц заряда')

    def discharge(self):
        if len(self.capacity) > 0:
            self.capacity.pop()
        print('Батарея разряжена на', len(self.capacity), 'единиц заряда')

    def __str__(self):
        if len(self.capacity) == self.max_charge:
            return '[)))))] - батарея полностью заряжена'
        elif len(self.capacity) == 0:
            return '[-] - батарея не заряжена'
        else:
            return '[' + ')' * len(self.capacity) + '] - батарея заряжена на ' + str(len(self.capacity)) + ' единиц заряда'
my_battery = Battery()
print(my_battery) 
my_battery.charge() 
my_battery.charge() 
my_battery.discharge() 
print(my_battery) 
