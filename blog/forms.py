# blog/forms.py

from django import forms
from django.forms import ValidationError

from .models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        required=True, label='글 제목', help_text='기왕이면 성의껏...'
    )
    content = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if '카지노' in title:
            self.add_error('카지노 단어는 금지 됨')


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'content', 'tags', )
        # exclude = ('title', 'category', )
        # fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if '바보' in title:
            raise ValidationError('바보스러운 기운이 난다')
        return title.strip()

    def clean(self):
        title = self.cleaned_data.get('title', '')
        content = self.cleaned_data.get('content', '')

        if '안녕' in title:
            self.add_error('title', '안녕은 이제 그만 안녕')
        if '안녕' in content:
            self.add_error('content', '안녕은 이제 그만 안녕')

