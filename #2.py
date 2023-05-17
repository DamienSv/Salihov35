#2
#Представьте себе очередь на кассе. К кассе подходит первый человек в очереди, а в конец очереди встает вновь пришедший. В программировании есть подобный тип данных - Queue (англ. "очередь"), 
#основанный на принципе FIFO (англ. first in, first out «первым пришёл — первым ушёл»).
#Задание:
#Реализовать класс Queue
#Определить атрибут inside, который будет хранить в себе имена людей в очереди.
#Переопределить метод __str__, чтобы преобразовать его к виду: Name1=>Name2=>...=>Name3
#Реализовать методы:
#add - который добавляет имя в очередь
#take_out убирает первого человека из списка
#Переопределить методы __add__ , __sub__, __iadd__, __isub__ чтобы они соответствовали методам add и take_out
class Queue:
    def __init__(self):
        self.inside = []

    def __str__(self):

        if len(self.inside) == 0:
            return ''

        result = ''
        for i in range(len(self.inside)-1):
            result += self.inside[i] + '=>'
        result += self.inside[-1]
        return result

    def add(self, name):
        self.inside.append(name)

    def take_out(self):

        if len(self.inside) == 0:
            return

        self.inside.pop(0)

    def __add__(self, name):
        self.add(name)
        return self

    def __sub__(self, name):
        self.take_out()
        return self

    def __iadd__(self, name):
        self.add(name)
        return self

    def __isub__(self, name):
        self.take_out()
        return self


q = Queue()
q.add('Алиса')
q.add('Иван')
q.take_out()
print(q)  
q += 'Маша'
q = q - 'Алиса'
print(q)  