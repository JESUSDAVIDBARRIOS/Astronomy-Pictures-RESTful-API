from django.db import models

class AstronomyPicture(models.Model):
    """
    This class represents the astronomy picture model.
    """
    title = models.CharField(max_length=200)
    explanation = models.TextField(null=True)
    hdurl = models.URLField(null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
