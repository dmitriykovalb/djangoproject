from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """[Create fields of the table]

    Arguments:
        models {[text,img]} -- [user,img]
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default="default.jpg", upload_to="user_images")

    """[Returns a string representation of the username]

    Returns:
        [str] -- [Username]
    """

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"

    """[save image]
    """

    def save(self):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 64 or image.width > 64:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)
