import random

import pandas as pd
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Handle,Pupil,Expert,Candidate_Master,Master,Specialist,Counter
import json
import requests
def Tag_Entry(ob,target):
    if target == 1200:
        ob.Pupil += 1
        ob.save()
    if target == 1400:
        ob.Specialist += 1
        ob.save()
    if target == 1600:
        ob.Expert += 1
        ob.save()
    if target == 1900:
        ob.Candidate_Master += 1
        ob.save()
    if target == 2100:
        ob.Master += 1
        ob.save()
def Data_Entry(handle, current , target):
    columns = ['ID', 'Index', 'Rating', 'Tags']
    url = 'https://codeforces.com/api/user.rating?handle=' + handle
    try:
        response = requests.get(url)
    except:
        return
    x = response.json()
    start = 0
    end = 0
    paisi = 0
    for con in x['result']:
        if start == 0 and con['newRating'] >= current and con['oldRating'] != 0:
            start = con['ratingUpdateTimeSeconds']
        if start >= 0:
            end = con['ratingUpdateTimeSeconds']
        if con['newRating'] >= target:
            paisi = 1
            break

    if paisi == 0:
        return
    else:
        ob = Counter.objects.filter(Tag_Name='users').last()
        if ob == None:
            ob=Counter(
                Tag_Name = 'users',
                Pupil = 0,
                Specialist = 0,
                Expert = 0,
                Candidate_Master = 0,
                Master = 0
            )
            ob.save()
        Tag_Entry(ob,target)
    url = 'https://codeforces.com/api/user.status?handle=' + handle + '&from=1'
    try:
        response = requests.get(url)
    except:
        return
    x = response.json()
    cnt = 0
    for sub in x['result']:
        if start <= sub['creationTimeSeconds'] <= end and sub['verdict'] == 'OK':
            if 'rating' in sub['problem'] and sub['problem']['rating'] > current:
                con_id = sub['contestId']
                index = sub['problem']['index']
                rating = sub['problem']['rating']
                tags = sub['problem']['tags']
                for i in range(len(tags)):
                    tags[i] = tags[i].replace(" ", "");
                    tags[i] = tags[i].replace("-", "");
                    ob = Counter.objects.filter(Tag_Name=tags[i]).last()
                    if ob == None:
                        ob = Counter(
                            Tag_Name=tags[i],
                            Pupil=0,
                            Specialist=0,
                            Expert=0,
                            Candidate_Master=0,
                            Master=0
                        )
                        ob.save()
                    Tag_Entry(ob, target)

                tags = ', '.join(tags)
                row = [con_id, index, rating, tags]
                if target == 1200:
                    ob = Pupil(
                        PID = con_id,
                        Index = index,
                        Rating = rating,
                        Tags = tags

                    )
                    if not Pupil.objects.filter(PID=con_id, Index=index).exists():
                        ob.save()
                elif target == 1400:
                    ob = Specialist(
                        PID = con_id,
                        Index = index,
                        Rating = rating,
                        Tags = tags

                    )
                    if not Specialist.objects.filter(PID=con_id, Index=index).exists():
                        ob.save()
                elif target == 1600:
                    ob = Expert(
                        PID = con_id,
                        Index = index,
                        Rating = rating,
                        Tags = tags

                    )
                    if not Expert.objects.filter(PID=con_id, Index=index).exists():
                        ob.save()
                elif target == 1900:
                    ob = Candidate_Master(
                        PID = con_id,
                        Index = index,
                        Rating = rating,
                        Tags = tags

                    )
                    if not Candidate_Master.objects.filter(PID=con_id, Index=index).exists():
                        ob.save()
                elif target == 2100:
                    ob = Master(
                        PID = con_id,
                        Index = index,
                        Rating = rating,
                        Tags = tags

                    )
                    if not Master.objects.filter(PID=con_id, Index=index).exists():
                        ob.save()

    print("Data Inserted Successfully for Level", target)

def Add(request):
    if request.method=='POST':
        handle=request.POST.get('handle')
        if(handle is not None):
            print(handle)
            handle = handle.lower()
            try:
                obj = Handle.objects.get(handle=handle)
            except Handle.DoesNotExist:
                ob=Handle(
                    handle=handle
                )
                ob.save()
                Data_Entry(handle, 0, 1200)
                Data_Entry(handle, 1201, 1400)
                Data_Entry(handle, 1401, 1600)
                Data_Entry(handle,1601,1900)
                Data_Entry(handle, 1901, 2100)

    return render(request,'donate.html')


from .weak_tags import  get_weak_tags
from .Target import get_lo_hi
from .problem_giver import  give_me_problem
import random
def Show(request):
    handle = request.session['handle']
    (ase,target)=get_lo_hi(handle)
    if target==1200:
        Table = Pupil
    if target == 1400:
        Table = Specialist
    if target == 1600:
        Table = Expert
    if target == 1900:
        Table = Candidate_Master
    if target == 2100:
        Table = Master
        ####
    Table = pd.DataFrame.from_records(Table.objects.all().values())
    res= give_me_problem(request.session['weak_tags'],Table)
    #apatoto 1 ta pathacchi
    random_index = random.randint(0, len(res) - 1)
    pathabo = Table.iloc[res[random_index]]
    s = pathabo.Tags
    Tags= s.split(',')
    return  render(request,'show.html',{'i':pathabo,'Tags':Tags})

def Recommend(request):
    if request.method=='POST':
        handle=request.POST.get('handle')
        if(handle is not None):
            weak_tags=get_weak_tags(handle)
            request.session['weak_tags']=weak_tags
            request.session['handle'] = handle
            return HttpResponseRedirect('show.html')

    return render(request,'input.html')

def Home(request):
    return render(request,'home.html')