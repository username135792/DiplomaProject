from django.db import models


class Vacancy(models.Model):
    title = models.CharField('Название', max_length=255)
    company = models.CharField('Компания/отдел', max_length=255)
    location = models.CharField('Локация', max_length=255)
    salary = models.CharField('Зарплата', max_length=255)
    employment_type = models.CharField('Тип занятости', max_length=100, blank=True)
    experience = models.CharField('Опыт', max_length=100, blank=True)
    is_new = models.BooleanField('Новая вакансия', default=False)
    skills = models.TextField('Навыки', blank=True, help_text='Каждый навык с новой строки')
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    MARITAL_STATUS_CHOICES = [
        ('single', 'Холост/Не замужем'),
        ('married', 'Женат/Замужем'),
        ('divorced', 'Разведен(а)'),
        ('widowed', 'Вдовец/Вдова'),
    ]

    vacancy_title = models.CharField('Вакансия', max_length=255, blank=True)
    last_name = models.CharField('Фамилия', max_length=100)
    first_name = models.CharField('Имя', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    birth_date = models.DateField('Дата рождения')
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    registration_address = models.TextField('Адрес прописки')
    residence_address = models.TextField('Адрес проживания')
    citizenship = models.CharField('Гражданство', max_length=100)
    education = models.CharField('Образование', max_length=255)
    specialty = models.CharField('Специальность', max_length=255)
    municipal_experience = models.CharField('Стаж муниципальной службы', max_length=255, blank=True)
    work_experience = models.TextField('Трудовая деятельность', blank=True)
    marital_status = models.CharField('Семейное положение', max_length=20, choices=MARITAL_STATUS_CHOICES)
    children = models.CharField('Наличие детей', max_length=255, blank=True)
    photo = models.FileField('Фото', upload_to='photos/', blank=True, null=True)
    resume = models.FileField('Резюме', upload_to='resumes/')
    vacancy_source = models.TextField('Откуда узнал(а)', blank=True)
    created_at = models.DateTimeField('Дата подачи', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка на вакансию'
        verbose_name_plural = 'Заявки на вакансии'

    def __str__(self):
        return f'{self.last_name} {self.first_name} — {self.vacancy_title or "без вакансии"}'
