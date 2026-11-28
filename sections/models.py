from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Client(models.Model):
    name = models.CharField(max_length=150)
    industry = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    start_date = models.DateField()
    is_finished = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title


class NewsPost(models.Model):
    CATEGORIES = [
        ('company', 'Company'),
        ('projects', 'Projects'),
        ('events', 'Events'),
    ]

    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES)
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
