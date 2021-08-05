from django.db import models


class Industry(models.Model):
    """Индустрия"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отрасль'
        verbose_name_plural = 'Отрасли'


class StartDate(models.Model):
    """Начало Стартапа"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Начало стартапа'
        verbose_name_plural = 'Начало стартапа'


class StartUP(models.Model):
    """Стартап"""
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    stage = models.ForeignKey(StartDate, on_delete=models.CASCADE, default=1)
    info = models.TextField()

    def __str__(self):
        return self.title

    def get_url(self):
        return f'/all_startups/{self.id}/'

    class Meta:
        verbose_name = 'Стартап'
        verbose_name_plural = 'Стартапы'


class Investor(models.Model):
    """Инвестор"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    stage = models.ManyToManyField(StartDate)
    industry_prefer = models.ManyToManyField(Industry, related_name='prefer')
    industry = models.ManyToManyField(Industry, related_name='all_industry')

    def __str__(self):
        return self.name

    def get_url(self):
        return f'/all_investors/{self.id}/'

    class Meta:
        verbose_name = 'Инвестор'
        verbose_name_plural = 'Инвесторы'


class Mail(models.Model):
    """Письма"""
    destination = models.ForeignKey(Investor, on_delete=models.CASCADE)
    start_up = models.ForeignKey(StartUP, on_delete=models.CASCADE)
    sent = models.BooleanField(default=False)
    sent_date = models.DateField(auto_now=False, auto_now_add=False)
    industry_prefer = models.BooleanField(default=False)

    def __str__(self):
        return self.start_up.title

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
