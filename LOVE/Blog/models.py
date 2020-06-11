from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	title	 = models.CharField(max_length=20)
	content  = models.TextField(blank=True, null=True)

	#用CreateView模組下，訪問create網頁輸入完data後save後
	#被要求立即返回所創造no.新的網頁物件，所以必須import reverse。
	def get_absolute_url(self): 
   		# reverse()第一個參數：輸入之前url中的每個path所設定的name
   		return reverse("Blog:article_detail", kwargs={
   			"akb48": self.id,
   			# 記住！此self.id變數要和urls中path的detail_view的標籤變數<int:akb48>一樣，
   			# path('products/<int:akb48>/')context變數要和<int>標籤變數一樣。
   			})