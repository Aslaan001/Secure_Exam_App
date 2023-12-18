from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from OTS.models import *
from django.template import loader
import random

def welcome(request):
    template=loader.get_template('welcome.html')
    return HttpResponse(template.render())

def CandidateRegistrationForm(request):
    res=render(request,'register.html')
    return res

def CandidateRegistration(request):
    if request.method=='POST':
        username=request.POST['username']
        # check if the user exists
        if(len(Candidate.objects.filter(username=username))):
            userstatus=1
            
        else:
            candidate=Candidate()
            candidate.username=username
            candidate.password=request.POST['password']
            candidate.name=request.POST['name']
            candidate.save()
            userstatus=2
            
    else:
        userstatus=3  # method not post
        
    context={
        'userstatus':userstatus
    }
    
    res=render(request,'registration.html',context)
    return res
             
           

def loginview(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        candidate=Candidate.objects.filter(username=username,password=password)
        if len(candidate)==0:
            loginerror="INVALID CREDENTIALS"
            res=render(request,'login.html',{'loginerror':loginerror})
            
        else:
            request.session['username']=candidate[0].username
            request.session['name']=candidate[0].name
            res=HttpResponseRedirect("home")
    else:       
        res=render(request,'login.html')
    return res
    
 
def CandidateHome(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
    else:
        res=render(request,'home.html')
        return res
    
    
    
def Testpapper(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
        
    n=int(request.GET['n'])
    questions_pool=list(Question.objects.all())
    random.shuffle(questions_pool)
    question_list=questions_pool[:n]
    context={'questions':question_list}
    res=render(request,'testpapper.html',context)
    return res

def CalculateTestResult(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
        
    total_attempt=0
    total_right=0
    total_wrong=0
    qid_list=[]
    
    for k in request.POST:
        if k.startswith('qno'):
            qid_list.append(int (request.POST[k]))
    
    
    for n in qid_list:
        question=Question.objects.get(qid=n)
        try:
            if question.ans==request.POST['q'+str(n)]:
                total_right+=1
            else:
                total_wrong+=1
            total_attempt+=1
        except:
            pass
    
    
    points=(total_right-total_wrong)/len(qid_list)*10
    
    result=Result()
    result.username=Candidate.objects.get(username=request.session['username'])
    result.attempt=total_attempt
    result.right=total_right
    result.wrong=total_wrong
    result.points=points
    result.save()
    
    candidate=Candidate.objects.get(username=request.session['username'])
    candidate.test_attempted+=1
    candidate.points=(candidate.points*(candidate.test_attempted-1)+points)/candidate.test_attempted
    candidate.save()
    
    return HttpResponseRedirect('result')
                        
        

def TestHistory(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
        
    candidate=Candidate.objects.filter(username=request.session['username'])
    results=Result.objects.filter(username_id=candidate[0].username)
    
    context={'candidate':candidate[0],'results':results}
    res=render(request,'candidate_history.html',context)
    return res

def ShowTestResult(request):
    if 'name' not in request.session.keys():
        res=HttpResponseRedirect("login")
        
    result=Result.objects.filter(resultid=Result.objects.latest('resultid').resultid,username_id=request.session['username'])
    context={
        'result':result
    } 
    
    res=render(request,'show_result.html',context)
    return res

def logoutView(request):
   if 'name' in request.session.keys():
       del request.session['username']
       del request.session['name']
       return HttpResponseRedirect("login") 

    
