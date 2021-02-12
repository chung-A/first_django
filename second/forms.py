# from django import forms


# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=50)
#     content = forms.CharField(label='내용', widget=forms.Textarea)

from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            # 다국어 설정을 위해서 _는 넣어주는 식으로 할 것
            'title': _('제목'),
            'content': _('내용'),
        }
        help_texts = {
            'title': _('제목을 입력해 주세요'),
            'content': _('내용을 입력해 주세요'),
        }
        error_messages = {
            'name': {
                'max_length': _('제목이 너무 깁니다. 30자 이하로 입력해주세요')
            }
        }
