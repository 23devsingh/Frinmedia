from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class PostImage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='images_created', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True, max_length=500)
    created = models.DateField(auto_now_add=True)
    privacy = models.CharField(
        max_length=10,
        choices=[('public', 'Public'), ('private', 'Private')],
        default='public'
    )

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return f"Image by {self.user.username} - {self.description[:30]}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.description[:50]) or "untitled"
        super().save(*args, **kwargs)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name= 'images_liked',
                                        blank=True)

def validate_image(image):
    max_size = 5 * 1024 * 1024  # 5MB limit
    if image.size > max_size:
        raise ValidationError("Image file too large ( > 5MB )")
    if not image.name.lower().endswith(('jpg', 'jpeg', 'png')):
        raise ValidationError("Unsupported file format. Use JPG, JPEG, or PNG.")


