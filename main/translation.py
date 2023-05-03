from .models import Tour, TourDate, TourDetail, TourDropDown
from modeltranslation.translator import register, TranslationOptions


@register(Tour)
class TourTrans(TranslationOptions):
    fields = ('location', 'city', 'duration', 'description')


@register(TourDate)
class TourDateSeri(TranslationOptions):
    fields = ('date',)


@register(TourDetail)
class TourDetailTrans(TranslationOptions):
    fields = ('title', 'content', 'description')


@register(TourDropDown)
class TourDropTrans(TranslationOptions):
    fields = ('name', 'text')
