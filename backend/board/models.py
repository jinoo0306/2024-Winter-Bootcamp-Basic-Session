from datetime import timezone

from django.db import models

class Poster(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True,default=None)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()  # 삭제 시간을 기록
        self.save()  # 데이터는 삭제하지 않고 저장