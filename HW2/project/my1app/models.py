from django.db import models
from random import choice

# Создайте модель для запоминания бросков монеты: орёл или решка.Также запоминайте время броска
# Добавьте статический метод для статистики по n последним броскам монеты.
# Метод должен возвращать словарь с парой ключей/значений, для орла и для решки.

class HeadsAndTailsModel(models.Model):
    SIDES=('Heads', 'Tails')
    side = models.CharField(max_length=10, default=choice(SIDES))
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Coinside is {self.side}'
    
    @staticmethod
    def staistic(n):
        result = HeadsAndTailsModel.objects.all()[-n:]
        headcount = 0
        for res in result:
            if res.side == 'Heads':
                headcount += 1
        return {'heads': headcount, 'tails': n-headcount}

    