from django.db import models

class Soru(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    ust_soru = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='alt_sorular')

    def __str__(self):
        return self.baslik
