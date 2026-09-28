from django.db import models



class Book(models.Model):
    STATUS_CHOICES=[
        ("want", "Want To Read"),
        ("reading", "Currently Reading"),
        ("read", "Finished"),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length = 200)
    description = models.TextField()
    isbn = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="want") 
    published_at = models.DateField(blank=True, null=True, auto_now_add=True )
    updated_at = models.DateField(blank=True, null=True, auto_now=True)

    class Meta:
        ordering = ['published_at']

    def __str__(self):
        return self.title[:50]
