from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} - {self.company} ({self.location})"


class Education(models.Model):
    title = models.CharField(max_length=100)
    university = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    degree = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return (f"{self.title} - {self.university} ({self.location})\n"
                f"{self.degree} ({self.start_date} - {self.end_date})")


class Technology(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    github_url = models.URLField()
    live_url = models.URLField()
    image_url = models.ImageField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
