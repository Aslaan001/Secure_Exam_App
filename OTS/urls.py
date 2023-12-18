from django.urls import path
from OTS.views import *
app_name='OTS'

urlpatterns = [
    path('',welcome),
    path('new-candidate',CandidateRegistrationForm,name='registrationfrom'),
    path('store-candiadate',CandidateRegistration,name='storecandidate'),
    path('login',loginview,name='login'),
    path('home',CandidateHome,name='home'),
    path('test-papper',Testpapper,name="testpapper"),
    path('calculate-result',CalculateTestResult,name='calculatetest'),
    path('test-history',TestHistory,name="testHistory"),
    path('result',ShowTestResult,name='result'),
    path('logout',loginview,name='logout'),
    
   
]