from django import forms
from .models import Article 

class ArticleForm(forms.ModelForm):
	title = forms.CharField(
		label = '標題：',
		widget = forms.TextInput(attrs={
			"palceholder" : "請輸入文章的標題"
				}
			) 

		)
	content = forms.CharField(
		required=False, #不一定必填
		widget=forms.Textarea(attrs={
		"class": "new",
		"id": "Song",
		
				}
			)
		)

	class Meta:
		model = Article
		fields = [
			'title',
			'content',


		]