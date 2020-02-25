from django.db import models
# adding lines for the creation of model to upload the files


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
