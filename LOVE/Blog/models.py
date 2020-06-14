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
         # 直接切到name='article_detail'的url路徑
   		return reverse("Blog:article_detail", kwargs={
            "akb48": self.id,
   			# 記住！此self.id變數要和urls中path的detail_view的標籤變數<int:akb48>一樣
            # 物件的id會儲存於akb48變數當中，然後會送到urls的<int:akb48>裡頭作為參數->ArticleDetailView->article_detail.html->user
   			})