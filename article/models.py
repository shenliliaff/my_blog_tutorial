from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)#��Ŀ
    category = models.CharField(max_length = 50, blank = True)#��ǩ
    date_time = models.DateTimeField(auto_now_add = True)#����
    content = models.TextField(blank = True, null = True)#����
    
    #����__str__(self) ����Article����Ҫ��ô��ʾ�Լ�, 
    #һ��ϵͳĬ��ʹ��<Article: Article object> ����ʾ����, 
    #ͨ������������Ը���ϵͳʹ��title�ֶ�����ʾ�������
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']#��ʱ�併������