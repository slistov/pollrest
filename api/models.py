from django.db import models

from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.db.models.fields.related import ForeignKey


class Poll(models.Model):
    title = models.CharField('Название', max_length=200)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    description = models.CharField('Описание', max_length=500)
    
    def __str__(self):
        return self.title

@receiver(pre_save, sender=Poll)
def signal_before_model_update(sender, instance, **kwargs):
    """Перед сохранением экземпляра бросить исключение
    при попытке изменить readonly-поле.

    По задаче: у опроса после создания нельзя изменять start_date
    """
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass  # Инсерт, не препятствовать
    else:
        if not obj.start_date == instance.start_date:  # Попытка изменить поле
            raise models.ProtectedError("Нельзя изменять поле 'start_date'", None)



# class AnswerType(models.Model):
TEXT = 'Text'
SINGLE = 'Single'
MULTI = 'Multi'
CHOICES = [
    (TEXT, 'текстом'),
    (SINGLE, 'выбор одного варианта'),
    (MULTI, 'выбор нескольких вариантов')
]        


class Question(models.Model):
    poll_id= models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField('Текст вопроса', max_length=200)
    answer_type = models.CharField(
        'Тип ответа',
        max_length = 6,
        choices=CHOICES,
        default = TEXT
    )

    def __str__(self):
        return self.question_text