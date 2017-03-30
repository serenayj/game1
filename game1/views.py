from django.utils.decorators import method_decorator
import os
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth import models
#from forms import UserForm,LoginForm
from forms import hidForm, UserForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import loader
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.utils import timezone
import models 
import random 

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt



# Set timer for Korina's function 
from match import *

@csrf_exempt
def index(request):
        return render_to_response('base.html')

def waiting(request):
    # get the url from session 
    #urls = request.session["url"]
    tid = request.session["turkid"]
    mobj = Pairs.objects.get(user1id=tid)
    if mobj:
        urls = mobj.

    while urls is None:
        urls = request.session["url"]
    #if urls:
        print "waiting...."
    return render_to_response('waiting.html',{"channelid":urls})
    #else:
        #return render_to_response('waiting.html',{"channelid":"not ready yet"})

@csrf_exempt
def foo(request):
    #return HttpResponseRedirect("test")
    print "Something"
    return HttpResponseRedirect("waiting")

# post_new for tuning 
@csrf_exempt
def post_new(request):
    if request.method == "POST":
        form = hidForm(request.POST)
        #print "form", form 
        tid = request.session["turkid"]
        print "session id",tid
        if form.is_valid():
            print "Something"

            #Original method, saving the whole form 
            #post = form.save(commit=False)
            #post.save()

            #New method to test if could pass the turkid by session
            if (HID.objects.filter(turkid=tid).exists()):
                print "found the username"
                mobj = HID.objects.get(turkid=tid)
                mobj.username = form.cleaned_data["username"]
                mobj.save()
                print "username updated success!!!"
            else:
                print "there is no such record "
      
            #print "hit id:", form.cleaned_data["hitid"]
            print "username:", form.cleaned_data["username"]
            status = "False"

            un = form.cleaned_data["username"]

            #turkid =form.cleaned_data["turkid"]
            packages = {'username':un, 'Status':status}
            print "saving to db!!!"

            #call Korina's function 
            entrance = check(packages,un)
            request.session["url"] = entrance

            #Right now, we need to get the url by user id 
            return HttpResponseRedirect("test")
    else:
        print "why"
        form = hidForm()
    return render(request, 'edit.html', {'form':form})

# Where Jeremy might send form from AMT 
@csrf_exempt
def get_hid(request):
    if request:

        print "Checking success!!" 
        return HttpResponseRedirect("waiting")
    else: 
        return HttpResponse("Something wrong with the connection...", status=403)
#
#def get(self, request):
@csrf_exempt
def get(request):
    #form = hidForm()
    if request.GET.get("hit_id") is not None and request.GET.get("mturk_id") is not None and request.GET.get("ass_id") is not None:
        print "get method"
        hitid = request.GET["hit_id"]
        turkid = request.GET["mturk_id"]
        assid = request.GET["ass_id"]
        provisional = True 

    #Using for testing when there are no AMT frontend     
    else:
        print "start get!"
        no = random.randint(1,100)
        hitid = "t"+str(no)
        turkid = "t"+str(no)
        assid = "t" +str(no)
        provisional = True 
        un = "t"+str(no)
        # Test to see if could pass turkid to post_new 
        #obj = [hitid,turkid,assid,provisional]
        request.session["turkid"] = turkid 
        #
        #hit_objects = hidForm(hitid = hitid,turkid = turkid,assid=assid,provisional=provisional,username = "None")
       
        #Try just directly through the db 
        hit_objects = HID(hitid = hitid,turkid = turkid,assid=assid,provisional=provisional,username = un) 
        hit_objects.save()
        print "saving to the db via get" 
        return HttpResponseRedirect("post/new") 
