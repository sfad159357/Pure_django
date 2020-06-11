from django.db import models

from django.urls import reverse

# Create your models here.
class Product(models.Model):
	tilte		= models.CharField(max_length=120, ) #CharField唯一行文字框，max_length一定要限制輸入的長度。
	description = models.TextField(blank=True, null=True) #空白是可以被允許的，若沒填回傳null值
	price		= models.DecimalField(max_digits=100, decimal_places=2)
	summary		= models.TextField()
	featured	= models.BooleanField(default=True)

#更改models相關變數或參數要在cmd輸入$pytohn manage.py makemigrations/migrate變更 

	def get_absolute_url(self):
   		return f"/products/{self.id}/"
   	# 需要搭配from django.urls import reverse	才可以使用這method

	def get_absolute_url2(self): #用來回溯到某name的url路徑，與其標籤變數相連結
   		# reverse()第一個參數：輸入之前url中的每個path所設定的name
   		return reverse("productA", kwargs={
   			"my_id": self.id,
   			# 記住！此my_id變數要和urls中某個name的path的網址一樣，
   			# path('products/<int:my_id>/')context變數要和<int>標籤變數一樣。
   			})
