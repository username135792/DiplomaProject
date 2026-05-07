from django.db import models


class Tender(models.Model):
    CATEGORY_CHOICES = [
        ('info', 'Информация о тендерах'),
        ('results', 'Результаты тендеров'),
        ('rules', 'Правила тендеров'),
    ]

    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField('Название', max_length=255)
    link = models.FileField('Файл', upload_to='tenders/')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'
        ordering = ['-created_at']

    def __str__(self):
        return f'[{self.get_category_display()}] {self.name}'


class StaffMember(models.Model):
    name = models.CharField('Имя', max_length=255)
    role = models.CharField('Должность', max_length=255)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Фото', upload_to='staff/', blank=True, null=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['order']

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    # сюда идет дожность муниципальная или техническая (возможно)
    title = models.CharField('Название', max_length=255) # нет 
    # направлении профессии (внутренний фактор который не визуализируется на вакансии)
    company = models.CharField('Компания/отдел', max_length=255) # да
    location = models.CharField('Локация', max_length=255) # нет
    salary = models.CharField('Зарплата', max_length=255) # нет
    employment_type = models.CharField('Тип занятости', max_length=100, blank=True) # нет
    experience = models.CharField('Опыт', max_length=100, blank=True) # потом возможно
    is_new = models.BooleanField('Новая вакансия', default=False) # нет
    skills = models.TextField('Навыки', blank=True, help_text='Каждый навык с новой строки') # возможно
    is_active = models.BooleanField('Активна', default=True) # отлетает
    created_at = models.DateTimeField('Дата создания', auto_now_add=True) # отлетает

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
