import os, random, time
from django.conf import settings
from django.core.urlresolvers import reverse

from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

def path(filename):
    return '{}{}'.format(settings.STATIC_URL, os.path.join('burgers', filename))

BURGERS = [
    {'id'         : 1,
     'name'       : 'Seitan Burger',
     'notes'      : 'Made from seitan in the Cetus system, imported to Coffee Port by the Intergalactic Vegan Association.',
     'vegetarian' : True,
     'promoted'   : False,
     'bitcoin'      : 599,
     'image'      : path('seitan.jpg')},

    {'id'         : 2,
     'name'       : 'Diner Burger',
     'notes'      : 'We periodically send spies to Earth to bring this delicacy back to Coffee Port.',
     'vegetarian' : False,
     'promoted'   : True,
     'bitcoin'      : 750,
     'image'      : path('diner.jpg')},

    {'id'         : 3,
     'name'       : 'Halloumi Avocado Burger',
     'notes'      : "After the great halloumi depression of 2138 this is probably the rarest ingredient you'll find anywhere in the galaxy.",
     'vegetarian' : True,
     'promoted'   : False,
     'bitcoin'      : 9999,
     'image'      : path('halloumi.jpg')},

    {'id'         : 4,
     'name'       : 'Grizzly Bear Burger',
     'notes'      : 'The origin of this burgers name is unknown but it tastes great none the less. Just like fresh over the counter in Aldebaran.',
     'vegetarian' : False,
     'promoted'   : False,
     'bitcoin'      : 888,
     'image'      : path('grizzly.jpg')},

    {'id'         : 5,
     'name'       : 'Demolisher',
     'notes'      : 'One all time favourite of Klingons and Vogons. Earthlings might find this to be ... demolishing.',
     'vegetarian' : False,
     'promoted'   : False,
     'bitcoin'      : 5000,
     'image'      : path('demolisher.jpg')},

    {'id'         : 6,
     'name'       : 'Lava Burger',
     'notes'      : 'If dragons were a spacefaring species, this would be their burger.',
     'vegetarian' : False,
     'bitcoin'      : 749,
     'promoted'   : False,
     'image'      : path('lava.jpg')},

    {'id'         : 7,
     'name'       : 'Bean burger',
     'notes'      : "After Bitcoin replaced beans as the intergalactic currency, these are finally affordable again for the common spacefarer.",
     'vegetarian' : True,
     'promoted'   : True,
     'bitcoin'      : 799,
     'image'      : path('bean.jpg')},

    {'id'         : 8,
     'name'       : 'Skyscraper',
     'notes'      : "Rumor has it that one of these was once structural support for an intergalactic peace treaty.",
     'vegetarian' : False,
     'promoted'   : False,
     'bitcoin'      : 1250,
     'image'      : path('skyscraper.jpg')},         
    ]

class BurgerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    bitcoin = serializers.FloatField()

    def validate_id(self, attrs, source):
        if not attrs[source] in [b['id'] for b in BURGERS]:
            raise serializers.ValidationError("Sorry. It appears that we're out of this particular burger.")
        return attrs

    def validate_bitcoin(self, attrs, source):
        try:
            burger = [b for b in BURGERS if b['id'] == attrs['id']][0]
        except IndexError:
            raise serializers.ValidationError("Sorry. It appears that we're out of this particular burger.")

        if not attrs[source] >= burger['bitcoin']:
            raise serializers.ValidationError("Sorry. You appear to not have enough BTC.")
        return attrs

class IndexView(APIView):
    def get(self, request):
        return Response({'burgers': reverse('burgers')})

class BurgerIndexView(ListCreateAPIView):
    serializer_class = BurgerSerializer
    def latency(self):
        """ We're in space. Communication takes time ... """
        if settings.DEBUG:
            return 0
        latency = random.randint(1, 20)
        time.sleep(latency)
        return latency

    def get(self, request):
        response = {
            'burgers': BURGERS,
            'latency': self.latency()}
        return Response(response)

    def post(self, request):
        ser = BurgerSerializer(data = request.DATA)
        if not ser.is_valid():
            return Response(ser.errors)
        resp = {'message': 'Order placed.',
                'latency': self.latency()}
        return Response(resp)
