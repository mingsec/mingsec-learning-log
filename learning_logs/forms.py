# -*- coding: utf-8 -*-
# @Author: ZhuZefeng
# @Date:   2018-10-31 14:21:35
# @Last Modified by:   ZhuZefeng
# @Last Modified time: 2018-11-01 16:53:34


from django  import forms
from .models import Topic, Entry, Blog

class TopicForm(forms.ModelForm):
    class Meta:
        model  = Topic
        fields = ['text', 'name']
        labels = {'text':'主题名称','name':'主题简称'}

class EntryForm(forms.ModelForm):
    class Meta:
        model   = Entry
        fields  = ['text', 'name']
        labels  = {'text':'科目名称','name':'科目简称'}
        #widgets = {'text': forms.Textarea(attrs={'cols': 50})}

class BlogForm(forms.ModelForm):
    class Meta:
        model   = Blog
        fields  = ['title', 'name', 'text']
        labels  = {'title':'条目名称', 'name':'条目简称', 'text':'学习内容'}
        widgets = {'text': forms.Textarea(attrs={'cols': 22})}

