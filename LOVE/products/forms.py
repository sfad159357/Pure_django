from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	#以下三個fields的標題必須和Meta底下3個域名相同
	#相同則ProductForm為Meta做修飾
	#不相同則ProductFrom會形成額外的輸入域
	tilte		= forms.CharField(
					label = "", #label為空格前主題
					widget = forms.TextInput(attrs={
					"placeholder": "your tilte"
					})
					) 	
	description = forms.CharField(
					required=False, #不一定必填
					widget=forms.Textarea(attrs={
					"class": "new",
					"id": "Song",
					"rows": 10,
					"cols": 30
					})
				) 
	price		= forms.DecimalField(initial=199.99) #起始值

	email 		= forms.EmailField(required=False)
	class Meta: #request.POST的資料會存在底下字典
		model = Product
		fields = [
			'tilte',
			'description',
			'price',
		]

	# def clean_tilte(self, *args, **kwargs):
	# 	tilte = self.cleaned_data.get("tilte") #從Meta那裡得到{"tilte" = "XXX",...}的data
	# 	if not "CFE" in tilte:
	# 		raise forms.ValidationError("This is not a valid tilte")
	# 	return tilte

	# def clean_email(self, *args, **kwargs):
	# 	email = self.cleaned_data.get("email") 
	# 	if not email.endswith("edu"):
	# 		raise forms.ValidationError("This is not a valid email")
	# 	return email


class RawProductForm(forms.Form):
	tilte		= forms.CharField(
					label = "產品名稱：", #label為空格前主題
					widget = forms.TextInput(attrs={
						"placeholder": "your tilte"
						})
					) 
	description = forms.CharField(
					required=False, #不一定必填
					widget=forms.Textarea(attrs={
						"class": "new",
						"id": "Song",
						"rows": 10,
						"cols": 30
						})
					) 
	price		= forms.DecimalField(initial=199.99) #起始值


