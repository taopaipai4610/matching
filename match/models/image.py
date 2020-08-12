from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    objects = models.Manager
    origin = models.ImageField(upload_to="photos/%y/%m/%d/")

    big = ImageSpecField(source="origin",
                        processors=[ResizeToFill(1280, 1024)],
                        format="JPEG"
                        )
    thumbnail = ImageSpecField(source="origin",
                        processors=[ResizeToFill(250, 250)],
                        format="JPEG",
                        options={'quality': 60}
                        )
    middle = ImageSpecField(source="origin",
                        processors=[ResizeToFill(600, 400)],
                        format="JPEG",
                        options={'quality': 75}
                        )
    small = ImageSpecField(source="origin",
                        processors=[ResizeToFill(75, 75)],
                        format="JPEG",
                        options={'quaality': 50}
                        )
