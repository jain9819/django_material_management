from django.shortcuts import render

from . import Pool
import uuid
import os
def AddSubCategory(request):
    try:
        result = request.session['ADMIN']
        return render(request,'SubCategory.html')
    except Exception as e:
        return render(request, 'AdminLogin.html')

def SubCategorySubmit(request):
    try:
      subcategoryname=request.POST['subcategoryname']
      categoryid = request.POST['categoryid']
      description = request.POST['description']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
      q="insert into subcategory(categoryid,subcategoryname,description,subcategorypic)values({},'{}','{}','{}')".format(categoryid,subcategoryname,description,filename)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/SubCategoryImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      return render(request,'SubCategory.html',{'msg':'Sub-Category Added Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request,'SubCategory.html',{'msg':'Fail To Add Sub-Category'})


def ShowAllSubCategory(request):
    try:
        result = request.session['ADMIN']
        db,cmd=Pool.ConnectionPool()
        q="select * from subcategory"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"ShowAllSubCategory.html",{'rows':rows})

    except Exception as e:
        return render(request, 'AdminLogin.html')


def DisplaySubCategoryById(request):
    scid=request.GET['scid']
    try:
            db,cmd = Pool.ConnectionPool()
            q = "select SC.*,(select C.categoryname from category C where C.categoryid=SC.categoryid)from subcategory SC where subcategoryid={}".format(scid)
            cmd.execute(q)
            row = cmd.fetchone()
            db.close()
            return render(request, "DisplaySubCategoryById.html", {'row': row})

    except Exception as e:
       print("Error:", e)
       return render(request,"DisplaySubCategoryById.html", {'row': []})

def UpdateDeleteSubCategory(request):
    scid=request.GET['scid']
    btn=request.GET['btn']
    oldpic = request.GET['oldpic']
    if(btn=='Edit'):
        try:
          categoryid=request.GET['categoryid']
          subcategoryname=request.GET['subcategoryname']
          description=request.GET['description']

          db,cmd = Pool.ConnectionPool()
          q="update subcategory set categoryid={},subcategoryname='{}', description='{}' where subcategoryid={}".format(categoryid,subcategoryname,description,scid)
          cmd.execute(q)
          db.commit()
          db.close()
          return ShowAllSubCategory(request)

        except Exception as e:
            print("Error:", e)
            return ShowAllSubCategory(request)

    elif(btn=='Delete'):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "delete from subcategory where subcategoryid={}".format(scid)
            cmd.execute(q)
            db.commit()
            db.close()
            os.remove("D:/MM/assets/SubCategoryImages/" + oldpic)
            return ShowAllSubCategory(request)

        except Exception as e:
            print("Error:", e)
            return ShowAllSubCategory(request)

def EditSubCategoryImage(request):
    try:
        scid=request.GET['scid']
        subcategoryname = request.GET['subcategoryname']
        subcategorypic = request.GET['subcategorypic']
        row=[scid,subcategoryname,subcategorypic]

        return render(request,"EditSubCategoryImage.html",{'row':row})
    except Exception as e:
        print("Error:",e)
        return render(request, "EditSubCategoryImage.html", {'row': row})

def SaveSubCategoryImage(request):
    try:
      scid = request.POST['scid']
      oldpic=request.POST['oldpic']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]

      q="update subcategory set subcategorypic='{}' where subcategoryid={}".format(filename,scid)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/SubCategoryImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      os.remove("D:/MM/assets/SubCategoryImages/"+oldpic)
      return ShowAllSubCategory(request)

    except Exception as e:
        print("Error:", e)
        return ShowAllSubCategory(request)


