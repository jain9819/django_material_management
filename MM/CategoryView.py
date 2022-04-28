from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
import uuid
import os

def AddCategory(request):
    try:
        result = request.session['ADMIN']
        return render(request,'Category.html')
    except Exception as e:
        return render(request, 'AdminLogin.html')

def CategorySubmit(request):
    try:
      categoryname=request.POST['categoryname']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
      q="insert into category(categoryname, categorypic)values('{}','{}')".format(categoryname,filename)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/CategoryImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      return render(request,'Category.html',{'msg':'Category Added Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request,'Category.html',{'msg':'Fail To Add Category'})

def ShowAllCategory(request):
    try:
        result = request.session['ADMIN']
        db,cmd=Pool.ConnectionPool()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"ShowAllCategory.html",{'rows':rows})

    except Exception as e:
        return render(request, 'AdminLogin.html')

def ShowCategoryJson(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)

    except Exception as e:
        print("Error:",e)
        return JsonResponse(rows,safe=False)


def DisplayCategoryById(request):
    cid=request.GET['cid']
    try:
            db,cmd = Pool.ConnectionPool()
            q = "select * from category where categoryid={}".format(cid)
            cmd.execute(q)
            row = cmd.fetchone()
            db.close()
            return render(request, "DisplayCategoryById.html", {'row': row})

    except Exception as e:
       print("Error:", e)
       return render(request,"DisplayCategoryById.html", {'row': []})

def UpdateDeleteCategory(request):
    cid=request.GET['cid']
    btn=request.GET['btn']
    oldpic = request.GET['oldpic']
    if(btn=='Edit'):
        try:
          categoryname=request.GET['categoryname']
          db,cmd = Pool.ConnectionPool()
          q="update category set categoryname='{}' where categoryid={}".format(categoryname,cid)
          cmd.execute(q)
          db.commit()
          db.close()
          return ShowAllCategory(request)

        except Exception as e:
            print("Error:", e)
            return ShowAllCategory(request)

    elif(btn=='Delete'):
        try:
            db, cmd = Pool.ConnectionPool()
            q="delete from category where categoryid={}".format(cid)
            cmd.execute(q)
            db.commit()
            db.close()
            os.remove("D:/MM/assets/CategoryImages/"+oldpic)
            return ShowAllCategory(request)

        except Exception as e:
            print("Error:", e)
            return ShowAllCategory(request)
def EditCategoryImage(request):
    try:
        cid=request.GET['cid']
        categoryname = request.GET['categoryname']
        categorypic = request.GET['categorypic']
        row=[cid,categoryname,categorypic]

        return render(request,"EditCategoryImage.html",{'row':row})
    except Exception as e:
        print("Error:",e)
        return render(request, "EditCategoryImage.html", {'row': row})

def SaveCategoryImage(request):
    try:
      cid1 = request.POST['cid1']
      oldimg=request.POST['oldimg']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]

      q="update category set categorypic='{}' where categoryid={}".format(filename,cid1)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/CategoryImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      os.remove("D:/MM/assets/CategoryImages/"+oldimg)
      return ShowAllCategory(request)

    except Exception as e:
        print("Error:", e)
        return ShowAllCategory(request)


