from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(TranslatePage)

class InfoTranslateOptions(TranslationOptions):
    fields = ('name', 'title',)