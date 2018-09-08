from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)#题目
    category = models.CharField(max_length = 50, blank = True)#标签
    date_time = models.DateTimeField(auto_now_add = True)#日期
    content = models.TextField(blank = True, null = True)#正文
    
    #其中__str__(self) 函数Article对象要怎么表示自己, 
    #一般系统默认使用<Article: Article object> 来表示对象, 
    #通过这个函数可以告诉系统使用title字段来表示这个对象
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']#按时间降序排列