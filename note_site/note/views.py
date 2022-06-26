from http.client import HTTPResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Note
from django.db import connection
import json
from django.http import JsonResponse



def index(request):
    return render(request, 'note/index.html')

@login_required
def notes(request):
    rows=my_notes(request)

    dt = {}
    dt['data']=[]
    for note in rows:
        dt['data'].append({'id':note[0], 'parent':note[1],'text':note[2]})

    res={}
    res['core']=dt
    res['core']["multiple"]=False
    res['core']["check_callback"]= True   # без него не добавляется узел
    res['plugins']=['search','state','wholerow','changed']
    res_json=json.dumps(res, ensure_ascii=False)
    par="<script type=\"text/javascript\">$(\"#jstree\").jstree("+res_json+");</script>"

    context = {
         'tree_data': par,
    }
    return render(request, 'note/notes.html',context)

@login_required
def my_notes(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("select CAST(id as text) as idn,iif(parent_id==-1,'#',CAST(parent_id as text)) as parent,name as 'text' from note_note where user_id=="+str(request.user.id)+' order by level,name ')
            rows = cursor.fetchall()
            return rows
    except:
        print('render error')
        return {}

@login_required
def new_note(request):
    
    if request.method == "POST":
       par= json.loads(request.body.decode("utf-8"))
       try:
            lev=0
            parnt=-1
            nm=par['name']
            txt=' '

            if par['parent']!='#':               
                nt=Note.objects.get(pk=par['parent'])   
                lev=nt.level+1
                parnt=nt.id

            nwNote=Note()            
            nwNote.level=lev
            nwNote.parent_id=parnt
            nwNote.name=nm
            nwNote.text=txt
            nwNote.user=request.user
            nwNote.save()
 
            return JsonResponse({"id":str(nwNote.id),'parent':'#','name':nwNote.name}, status = 200)
       except Exception as e:
        print(e) 
        return JsonResponse({"error": ""}, status=400)



@login_required
def rename_note(request):    
    if request.method == "POST":
       par= json.loads(request.body.decode("utf-8"))
       try:
            nm=par['name']
            nid=par['id']
              
            nwNote=Note.objects.get(pk=nid)   
            nwNote.name=nm
            nwNote.save()
 
            return JsonResponse({"result":"OK"}, status = 200)
       except Exception as e:
        print(e) 
        return JsonResponse({"error": ""}, status=400)


@login_required
def delete_notes(request):    
    if request.method == "POST":
       par= json.loads(request.body.decode("utf-8"))
       try:
            nid=par['id']
            Note.objects.filter(id__in=nid).delete()   
           
            return JsonResponse({"result":"OK"}, status = 200)
       except Exception as e:
        print(e) 
        return JsonResponse({"error": ""}, status=400)


@login_required
def text_loading(request):    
    if request.method == "POST":
       par= json.loads(request.body.decode("utf-8"))
       try:
            res={}
            nid=par['id']
            nwNote=Note.objects.get(pk=nid) 
            txt=nwNote.text

            return JsonResponse({'id':nid,'text':txt}, status = 200)

       except Exception as e:
        print(e) 
        return JsonResponse({"error": ""}, status=400)

@login_required
def text_save(request):
    if request.method == "POST":
       par= json.loads(request.body.decode("utf-8"))
       try:
            res={}
            nid=par['id']
            txt=par['text']
            nwNote=Note.objects.get(pk=nid) 
            nwNote.text=txt
            nwNote.save()

            return JsonResponse({"result":"OK"}, status = 200)
       except Exception as e:
        print(e) 
        return JsonResponse({"error": ""}, status=400)