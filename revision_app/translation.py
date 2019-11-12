
import modeltranslation.translation as t

print(dir(t))


class GoodsTranslationOptions(TranslationOptions):
    fields = ('name', 'quantity', 'price')


translator.register(Goods, GoodsTranslationOptions)from .models import Goods