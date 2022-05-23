from tkinter.ttk import Style
from django import forms


class Search(forms.Form):
    search_text=forms.CharField(max_length=50, label='نام خواننده', required=False)
