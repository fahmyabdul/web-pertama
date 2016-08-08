from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text','created_date','published_date')

	def __init__(self, *args, **kwargs):
		super(PostForm, self).__init__(*args, **kwargs)
		self.fields['title'] = forms.CharField()
		self.fields['text'] = forms.CharField()
		self.fields['created_date'].disabled = forms.DateTimeField(input_formats=['%Y-%m-%d'])
		self.fields['published_date'].disabled = forms.DateTimeField(input_formats=['%Y-%m-%d'])

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)