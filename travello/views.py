from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Destination,subscribe,bookings, contact, comments,budgetplaces,nationalparks,religious,trecking,honeymoon,familyplaces
from django.contrib import messages
from travello.serializer import DestinationSerial,subscribeSerial
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import requests
import COVID19Py
from requests.exceptions import HTTPError
from django.core.paginator import Paginator


def Popular(request):
    desc_1= request.GET['field']
    dest = Destination.objects.all()
    context = {'dest':   dest,'desc_1': desc_1 }
    return render(request,'travel/destinations.html',context)

def Religious(request):
    desc_1= request.GET['field']
    dest1 = religious.objects.all()
    context = {'dest1':   dest1,'desc_1': desc_1 }
    return render(request,'travel/destinations.html',context)
def Familyplaces(request):
    desc_1= request.GET['field']
    dest2 = familyplaces.objects.all()
    context = {'dest2':   dest2,'desc_1': desc_1 }
    return render(request,'travel/destinations.html',context)
def Honeymoon(request):
    desc_1= request.GET['field']
    dest3 = honeymoon.objects.all()
    context = {'dest3':   dest3,'desc_1': desc_1 }
    return render(request,'travel/destinations.html',context)
def Trecking(request):
    desc_1= request.GET['field']
    dest4 = trecking.objects.all()
    context = {'dest4':   dest4,'desc_1': desc_1 }
    return render(request,'travel/destinations.html',context)
def Nationalparks(request):
    desc_1= request.GET['field']
    dest5 = nationalparks.objects.all()
    context = {'dest5':   dest5,'desc_1': desc_1 }
    return render(request,'travel/destinations.html',context)
def Budgetplaces(request):
    desc_1= request.GET['field']
    dest6 = budgetplaces.objects.all()
    context = {'dest6':   dest6,'desc_1':desc_1 }
    return render(request,'travel/destinations.html',context)

# Create your views here.
def blog(request):
    message = comments.objects.all()
    count = comments.objects.all().count()
    count1 = Destination.objects.all().count()
    count2 = religious.objects.all().count()
    count3 = familyplaces.objects.all().count()
    count4 = honeymoon.objects.all().count()
    count5 = trecking.objects.all().count()
    count6 = nationalparks.objects.all().count()
    count7 = budgetplaces.objects.all().count()    
    return render(request,'travel/blog.html',{'data':count,'data1':count1,'data2':count2,'data3':count3,'data4':count4,'data5':count5,'data6':count6,'data7':count7})


def singleblog(request):
    message = comments.objects.all()
    paginator = Paginator(message, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = comments.objects.all().count()
    count1 = Destination.objects.all().count()
    count2 = religious.objects.all().count()
    count3 = familyplaces.objects.all().count()
    count4 = honeymoon.objects.all().count()
    count5 = trecking.objects.all().count()
    count6 = nationalparks.objects.all().count()
    count7 = budgetplaces.objects.all().count()    
    context = {'message' : page_obj,'data': count,'data1':count1,'data2':count2,'data3':count3,'data4':count4,'data5':count5,'data6':count6,'data7':count7 }
    return render(request,'travel/singleblog.html',context)

''' def temprature(request):
        city= request.POST['city_data']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=e97bb1eb01dcd766c9703c75b2014009'
        r = requests.get(url.format(city)).json()
        city_weather = {
                'discription' : r['weather'][0]['description'],
                'city' : city,
                'temp' : r['main']['temp']-273,
                'feels_like' : r['main']['feels_like'],
                'temp_min' : r['main']['temp_min'],
                'temp_max' : r['main']['temp_max'],
                'pressure' : r['main']['pressure'],
        }
        context = {'city_weather' : city_weather}
        return render(request,'temprature.html',context) '''

def index(request):

    dest = Destination.objects.all()
    count1 = Destination.objects.all().count()
    count2 = religious.objects.all().count()
    count3 = familyplaces.objects.all().count()
    count4 = honeymoon.objects.all().count()
    count5 = trecking.objects.all().count()
    count6 = nationalparks.objects.all().count()
    count7 = budgetplaces.objects.all().count()
    paginator = Paginator(dest, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    covid19 = COVID19Py.COVID19()
    location = covid19.getLocationByCountryCode("NP")
    for i in location:
        data = i['latest']
    covid_data = {
            'confirmed' : data['confirmed'],
            'deaths' : data['deaths'],
            'recovered' : data['recovered'],
        }
    context = {'covid_data' : covid_data,'dest1':dest,'dest':page_obj,'data1':count1,'data2':count2,'data3':count3,'data4':count4,'data5':count5,'data6':count6,'data7':count7}

    return render(request,'travel/index.html',context)

def covid(request):
        city= request.POST['covid_data']
        covid19 = COVID19Py.COVID19()  
        try:
            location = covid19.getLocationByCountryCode(city)
            for i in location:
                data = i['latest']
            covid_data = {
                'name' : city,
                'confirmed' : data['confirmed'],
                'deaths' : data['deaths'],
                'recovered' : data['recovered'],
                }
            context = {'covid_data' : covid_data}

            return render(request,'covid.html',context)
        except HTTPError:
            messages.info(request,'CODE NOT FOUND')
            return render(request,'covid.html')
    

#@login_required(login_url='login')
def search(request):
    name = request.POST['name']
    if Destination.objects.filter(name=name).exists():
        dest = Destination.objects.all()
        data2 = Destination.objects.all()
        data_1 = Destination.objects.get(name=name)
        return render(request, 'travel/destination_details.html', {'desc_1': data_1,'data2':data2, 'dest': dest})
    else:
        messages.info(request,'SEARCH NOT FOUND')
        #return render(request, 'travel/index.html')
        return redirect('/')

#@login_required(login_url='login')
def discription(request):
    desc_1= request.GET['field']
    if Destination.objects.filter(name=desc_1).exists():
        data_1= Destination.objects.get(name=desc_1)
    elif religious.objects.filter(name=desc_1).exists():
        data_1= religious.objects.get(name=desc_1)
    elif budgetplaces.objects.filter(name=desc_1).exists():
        data_1= budgetplaces.objects.get(name=desc_1)
    elif nationalparks.objects.filter(name=desc_1).exists():
        data_1= nationalparks.objects.get(name=desc_1)
    elif honeymoon.objects.filter(name=desc_1).exists():
        data_1= honeymoon.objects.get(name=desc_1)
    elif familyplaces.objects.filter(name=desc_1).exists():
        data_1= familyplaces.objects.get(name=desc_1)
    elif trecking.objects.filter(name=desc_1).exists():
        data_1= trecking.objects.get(name=desc_1)
    else:
        messages.info(request,'SEARCH NOT FOUND')
    data2 =Destination.objects.all()
    dest = Destination.objects.all()
    return render(request,'travel/destination_details.html', {'desc_1': data_1,'data2':data2, 'dest': dest})
    
def destinations(request):
    desc_1= request.GET['field']
    dest =Destination.objects.all()
    paginator = Paginator(dest, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    dest1 = religious.objects.all()
    paginator1 = Paginator(dest1, 4)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number1)    
    dest2 = familyplaces.objects.all()
    paginator2 = Paginator(dest2, 4)
    page_number2 = request.GET.get('page')
    page_obj2 = paginator2.get_page(page_number2)    
    dest3 = honeymoon.objects.all()
    paginator3 = Paginator(dest3, 4)
    page_number3 = request.GET.get('page')
    page_obj3 = paginator3.get_page(page_number3)    
    dest4 = trecking.objects.all()
    paginator4 = Paginator(dest4, 4)
    page_number4 = request.GET.get('page')
    page_obj4 = paginator4.get_page(page_number4)    
    dest5 = nationalparks.objects.all()
    paginator5 = Paginator(dest5, 4)
    page_number5 = request.GET.get('page')
    page_obj5 = paginator5.get_page(page_number5)
    dest6 = budgetplaces.objects.all()
    paginator6 = Paginator(dest6, 4)
    page_number6 = request.GET.get('page')
    page_obj6 = paginator6.get_page(page_number6)
    return render(request,'travel/destinations.html', {'dest': page_obj,'desc_1':desc_1,'dest1':page_obj1,'dest2':page_obj2,'dest3':page_obj3,'dest4':page_obj4,'dest5':page_obj5,'dest6':page_obj6})
def subscribed(request):
    if request.method == 'POST':
        email = request.POST['email']
        Subscribe = subscribe.objects.create(email=email)
        Subscribe.save()
        messages.info(request,'SUBSCRIBED')
        return redirect('/')
    else:
        dest = Destination.objects.all()
        return render(request,'travel/destination_details.html', {'dest': dest})

def contacts(request):
    if request.method == 'POST':
        #username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contact = contact.objects.create(first_name=first_name, last_name=last_name, email=email, subject=subject, message=message)
        Contact.save();
        #return redirect('/')
        resp = {
            'sent': True
        }
        return JsonResponse(resp)
    else:
        return render(request,'travel/contact.html')

def comment(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        website = request.POST['website']
        
        Comments = comments.objects.create(name=name, message=message, email=email, website=website)
        Comments.save();
        resp1 = {
            'sent': True
        }
        return JsonResponse(resp1)
        
        
        

''' def book(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        plocation = request.POST['plocation']
        destination = request.POST['destination']
        phone = request.POST['phone']
        date = request.POST['date']
        hour = request.POST['hour']
        min = request.POST['min']
        zone= request.POST['zone']
        book_flight = bookings.objects.create(name=name,email=email,plocation=plocation,destination=destination,phone=phone,date=date,hour=hour,min=min,zone=zone)
        book_flight.save()
        booki = bookings.objects.all()
        messages.info(request, 'SUCCESSFULLY BOOKED')
        return redirect('/')
    else:
        return render(request,'book.html') '''



    # Generic Class Based Api View

class GenericAPIDestination(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    queryset = Destination.objects.all()
    serializer_class = DestinationSerial
    authentication_classes = [SessionAuthentication, BasicAuthentication ,TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def put(self, request, pk=None):
        if pk:
            return self.update(request, pk)
        else:
            return self.create(request)

    def delete(self, request, pk):
        return self.destroy(request, pk)

class subscribeViewSet(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):

    queryset = subscribe.objects.all()
    serializer_class = subscribeSerial
    authentication_classes = [SessionAuthentication, BasicAuthentication ,TokenAuthentication ]
    permission_classes = [IsAuthenticated]

    lookup_field = 'pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)
        else:
            return self.list(request)

    def put(self, request, pk=None):
        if pk:
            return self.update(request, pk)
        else:
            return self.create(request)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# from Generic View sets
'''
class subscribeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = subscribe.objects.all()
    serializer_class = subscribeSerial
'''
# from normal viewset
'''class subscribeViewSet(viewsets.ViewSet):
    def list(self,request,pk=None):
        if pk:
            queryset = subscribe.objects.all()
            article = get_object_or_404(queryset, pk=pk)
            sears = subscribeSerial(article)
            return Response(sears.data)
        else:
            serializer = subscribe.objects.all()
            sears = subscribeSerial(serializer, many=True)
            return Response(sears.data)
    def put(self,request,pk=None):
        if pk:
            serializer = subscribeSerial(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        else:
            serializer = subscribeSerial(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
    def delete(self, request,pk):
        queryset = subscribe.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        sears = subscribeSerial(article)
        return Response(status=status.HTTP_204_NO_CONTENT)

'''



'''

    class Newapi(APIView):

        def get(self,request):
            serializer = Article.objects.all()
            sears = ArticleSearilizers(serializer, many=True)
            return Response(sears.data)

        def put(self,request):
                serializer = ArticleSearilizers(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_201_CREATED)


    class Articledetail(APIView):
        def get_object(self, id):
            try:
                return Article.objects.get(id=id)

            except Article.DoesNotExist:
                return Response(status=status.HTTP_200_OK)

        def get(self , request , id):
            arc = self.get_object(id)
            serializer = ArticleSearilizers(arc)
            return Response(serializer.data)
        def put(self, request , id):
            serializer = ArticleSearilizers(data=Response.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)

        def delete(self,request,id):
            arc = self.get_object(id)
            arc.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




    '''

'''

    @api_view(['GET', 'POST'])
    def Api(request):
        if request.method == 'GET':
            sear = Article.objects.all()
            sears = ArticleSearilizers(sear,many=True)
            return Response(sears.data)

        elif request.method == 'POST':
            serializer = ArticleSearilizers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
'''
    @csrf_exempt
    def Article_detail(request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            arc = Article.objects.get(pk=pk)

        except Article.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ArticleSearilizers(arc)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ArticleSearilizers(arc, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            arc.delete()
            return HttpResponse(status=204)
    '''

# Api View Method(function)
'''
    @api_view(['GET', 'POST','DELETE'])
    def Article_detail(request, pk):
        """
        Retrieve, update or delete a code Article.
        """
        try:
            arc = Article.objects.get(pk=pk)

        except Article.DoesNotExist:
            return Response(status=status.HTTP_200_OK)

        if request.method == 'GET':
            serializer = ArticleSearilizers(arc)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ArticleSearilizers(data=Response.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            arc.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
         '''




