from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic import TemplateView
import json as simplejson

from .models import Slider, Post, Category, Synagogue, Restaurant, Kitchen, Photo, Phone, Email, Country, City, PhotoSynagogue, PhoneSynagogue, EmailSynagogue


class IndexView(TemplateView):
    template_name = 'guide/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sliders'] = Slider.objects.filter(published_date__lte=timezone.now()).order_by('sort', '-published_date')[
                          :5]
        data['posts'] = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
        data['categories'] = Category.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[
                             :20]
        data['kitchens'] = Kitchen.objects.all()

        return data


class PostDetailView(generic.ListView):
    template_name = 'guide/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).get(pk=self.kwargs['pk'])


def category_synagogues(request):
    data = {}
    dbCities = []

    queryCountries = request.GET.get('country')
    queryCities = request.GET.get('queryCities')

    dbSynagogues = Synagogue.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:50]

    # Получаем список стран
    dbCountries = Country.objects.all()

    # Получаем список городов по выбранней стране
    if queryCountries and queryCountries != '':
        dbCities = City.objects.filter(country__handle=queryCountries)

    # Фильтр по странам
    if queryCountries:
        dbSynagogues = Synagogue.objects.filter(country__handle=queryCountries).order_by('-published_date')[:50]
        data['queryCountries'] = queryCountries

    data['dbSynagogues'] = dbSynagogues
    data['dbCountries'] = dbCountries
    data['dbCities'] = dbCities

    return render(request, 'guide/synagogues.html', data)


def category_synagogues_detail(request, handle):
    import json

    data = {}

    synagogue = Synagogue.objects.get(handle=handle)
    gallery = PhotoSynagogue.objects.filter(synagogue=synagogue.id)
    phones = PhoneSynagogue.objects.filter(synagogue=synagogue.id)
    emails = EmailSynagogue.objects.filter(synagogue=synagogue.id)

    if synagogue.lat is None or synagogue.lng is None:
        jsonCoordinates = ''
    else:
        jsonCoordinates = json.dumps({'lat': synagogue.lat, 'lng': synagogue.lng})

    data['synagogue'] = synagogue
    data['gallery'] = gallery
    data['phones'] = phones
    data['emails'] = emails
    data['jsonCoordinates'] = jsonCoordinates

    return render(request, 'guide/synagogue.html', data)


def category_restaurants(request):
    data = {}
    dbCities = []

    queryKitchens = request.GET.get('kitchens')
    queryCountries = request.GET.get('country')
    queryCities = request.GET.get('queryCities')

    dbRestaurants = Restaurant.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:50]
    # Формируем теги по свойству кухни для ресторанов
    kitchens = {}
    for restaurant in dbRestaurants:
        kitchens[restaurant.id] = restaurant.kitchens.all()

    # Получаем список свойства кухни
    dbKitchens = Kitchen.objects.all()
    # Получаем список стран
    dbCountries = Country.objects.all()

    # Получаем список городов по выбранней стране
    if queryCountries and queryCountries != '':
        dbCities = City.objects.filter(country__handle=queryCountries)

    # Фильтр по кухням
    if queryKitchens and (queryCountries is None or queryCountries == ''):
        dbRestaurants = Restaurant.objects.filter(kitchens__handle=queryKitchens).order_by('-published_date')[:50]
        data['queryKitchens'] = queryKitchens

    # Фильтр по странам
    if queryCountries and (queryKitchens is None or queryKitchens == ''):
        dbRestaurants = Restaurant.objects.filter(country__handle=queryCountries).order_by('-published_date')[:50]
        data['queryCountries'] = queryCountries

    # Фильтр по странам и кухням
    if queryCountries and queryKitchens and queryCountries != '' and queryKitchens != '':
        dbRestaurants = Restaurant.objects.filter(country__handle=queryCountries,
                                                  kitchens__handle=queryKitchens).order_by('-published_date')[:50]
        data['queryCountries'] = queryCountries
        data['queryKitchens'] = queryKitchens

    data['dbRestaurants'] = dbRestaurants
    data['dbKitchens'] = dbKitchens
    data['kitchens'] = kitchens
    data['dbCountries'] = dbCountries
    data['dbCities'] = dbCities

    return render(request, 'guide/restaurants.html', data)


def category_restaurants_detail(request, handle):
    import json

    data = {}

    restaurant = Restaurant.objects.get(handle=handle)
    gallery = Photo.objects.filter(restaurant=restaurant.id)
    phones = Phone.objects.filter(restaurant=restaurant.id)
    emails = Email.objects.filter(restaurant=restaurant.id)
    kitchens = restaurant.kitchens.all()

    if restaurant.lat is None or restaurant.lng is None:
        jsonCoordinates = ''
    else:
        jsonCoordinates = json.dumps({'lat': restaurant.lat, 'lng': restaurant.lng})

    data['restaurant'] = restaurant
    data['gallery'] = gallery
    data['kitchens'] = kitchens
    data['phones'] = phones
    data['emails'] = emails
    data['jsonCoordinates'] = jsonCoordinates

    return render(request, 'guide/restaurant.html', data)


def map(request):
    import json

    data = {}
    sectionCode = request.GET.get('section')

    stores = {
        "type": "FeatureCollection",
        "features": []
    }

    if sectionCode == 'restaurants':
        dbRestaurants = Restaurant.objects.all()
        for restaurant in dbRestaurants:
            stores['features'].append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        restaurant.lng,
                        restaurant.lat
                    ]
                },
                "properties": {
                    "phoneFormatted": "8 (495) 690-62-66",
                    "phone": "84956906266",
                    "name": restaurant.title,
                    "handle": restaurant.handle,
                    "pic": restaurant.pic.url,
                    "address": restaurant.address,
                    "city": restaurant.city.title,
                    "country": restaurant.country.title,
                    "crossStreet": restaurant.address,
                    "postalCode": "123104",
                    "state": restaurant.city.title
                }
            })

    if sectionCode == 'synagogues':
        dbSynagogues = Synagogue.objects.all()
        for synagogue in dbSynagogues:
            stores['features'].append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        synagogue.lng,
                        synagogue.lat
                    ]
                },
                "properties": {
                    "phoneFormatted": "8 (495) 690-62-66",
                    "phone": "84956906266",
                    "name": synagogue.title,
                    "handle": synagogue.handle,
                    "pic": synagogue.pic.url,
                    "address": synagogue.address,
                    "city": synagogue.city.title,
                    "country": synagogue.country.title,
                    "crossStreet": synagogue.address,
                    "postalCode": "123104",
                    "state": synagogue.city.title
                }
            })

    jsonStores = json.dumps(stores)
    data['stores'] = jsonStores
    data['sectionCode'] = sectionCode

    return render(request, 'guide/map.html', data)


def search(request):
    data = {}
    query = request.GET.get('q')

    if query:
        restaurants = Restaurant.objects.filter(title__iregex=r'(' + query + ')')
        data['restaurants'] = restaurants

        synagogues = Synagogue.objects.filter(title__iregex=r'(' + query + ')')
        data['synagogues'] = synagogues
        print(synagogues)

    data['query'] = query

    return render(request, 'guide/search.html', data)
