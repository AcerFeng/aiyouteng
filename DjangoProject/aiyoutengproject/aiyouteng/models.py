from django.db import models

# Create your models here.

class Platform(models.Model):
    """来源平台"""
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class VideoCategory(models.Model):
    """视频分类：电视剧、电影、综艺"""
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class SeriesCategory(models.Model):
    """电视剧分类：全部热播、内地、网剧、韩剧、美剧"""
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class MoviesCategory(models.Model):
    """电影分类：全部热播、院线、内地、香港、美国"""
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
        
class VerietyCategory(models.Model):
    """综艺分类：全部热播、内地、港台、美国"""
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Video(models.Model):
    """视频模型"""
    name = models.CharField(max_length=80)
    image = models.CharField(max_length=200)
    desc = models.CharField(max_length=100)
    play_num = models.CharField(max_length=50)
    update_num = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    score = models.CharField(max_length=10)

    platform = models.ForeignKey(Platform)
    video_category = models.ManyToManyField(VideoCategory, blank=True)
    movies_category = models.ManyToManyField(MoviesCategory, blank=True)
    veriety_category = models.ManyToManyField(VerietyCategory, blank=True)

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    def __str__(self):
        return self.name
        