from django.shortcuts import render, redirect
# from django.views.generic import TemplateView

from JKC_numbering_system.forms import LoginForm
# import gmaps
# from pysafebrowsing import SafeBrowsing

# Create your views here.
def index(request):
    #implement google maps api request here.

    # gmaps.configure(api_key='AIzaSyABv1puoKOaP2CekhpYMNkdtgZJn2HQD8o')
    # if request.method == 'POST':
    #     print("post")

    return render(request, 'JKC_numbering_system/home.html')

def login(request):
    return render(request, 'JKC_numbering_system/login.html')

def authenticate(request):
    print(">>>>post()")
    print("request method: %s",request.method)
    if request.method == 'POST':
        print(">>>>request is POST")
        form = LoginForm(request.POST)
        if form.is_valid():
            print(">>>>form.is_valid()")
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return redirect('/home')
    print(">>>>form is not valid and not POST")
    return render(request, 'JKC_numbering_system/login.html')

# class VenuesResource(Resource):
#     id = fields.CharField(attribute='id')
#     name = fields.CharField(attribute='name')
#     address = fields.CharField(attribute='address', null=True)

#     class Meta:
#         resource_name = 'venues'
#         allowed_methods = ['get', 'post']
#         object_class = VenueObject
#         authorization = Authorization()
#         authentication = BasicAuthentication()

#         def _client(self):
#     		return GooglePlaces(settings.GOOGLE_API_KEY)

#     	def detail_uri_kwargs(self, bundle_or_obj):
# 		    kwargs = {}

# 		    if isinstance(bundle_or_obj, Bundle):
# 		        kwargs['pk'] = bundle_or_obj.obj.id
# 		    else:
# 		        kwargs['pk'] = bundle_or_obj['id']

# 		    return kwargs

# 		 #GET
# 		 def obj_get(self, request=None, **kwargs):
# 		    result = self._client().get_place(kwargs['pk'])
# 		    result.get_details()
# 		    return VenueObject(result.reference, result.name, result.formatted_address)

# 		 #POST
# 		 def obj_create(self, bundle, request=None, **kwargs):
# 		    result = self._client().add_place(name=str(bundle.data['name']),
# 		        lat_lng={'lat':bundle.data['latitude'],'lng':bundle.data['longitude']},
# 		        accuracy=bundle.data['accuracy'],
# 		        types=str(bundle.data['type']),
# 		        language=lang.ENGLISH,
# 		        sensor=True)
# 		    bundle.obj = VenueObject(result['reference'], bundle.data['name'])
# 		    bundle = self.full_hydrate(bundle)
# 		    return bundle

# class LoginView(TemplateView):

#     def post(self, request):
#         print(">>>>post()")
#         if request.method == 'POST':
#             print(">>>>request is POST")
#             form = LoginForm(request.POST)
#             if form.is_valid():
#                 print(">>>>form.is_valid()")
#                 post = form.save(commit=False)
#                 post.user = request.user
#                 post.save()

#                 name = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 return redirect('/home')
#         print(">>>>form is not valid and not POST")
#         return render(request, 'JKC_numbering_system/home.html')




