from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')# related_name : 항목명 의미
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) # 현재 날짜를 지정함
    updated = models.DateTimeField(auto_now_add=True)

    class Meta: # Photo에 종속클래스
        ordering = ['-updated'] # 내림차순 최신들어온것이 위로 올라감

    def __str__(self):
        return self.author.username + " " + self.created.strftime('%Y-%m-%d %H:%M:%S') # created 지정한 형식으로 날짜와 시간을 출력한다

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)]) # app의 이름을 지정해준다,

