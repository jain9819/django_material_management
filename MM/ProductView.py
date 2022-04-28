from django.shortcuts import render
from . import Pool
import uuid
import os
def AddProduct(request):
    try:
        result = request.session['ADMIN']
        return render(request,'Product.html')
    except Exception as e:
        return render(request, 'AdminLogin.html')

def SubmitProduct(request):
    try:
      subcategoryid=request.POST['subcategoryid']
      categoryid = request.POST['categoryid']
      pname = request.POST['pname']
      description = request.POST['description']
      gst = request.POST['gst']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
      q="insert into product(categoryid,subcategoryid,productname, description, gst, picture)values({},{},'{}','{}',{},'{}')".format(categoryid,subcategoryid,pname,description,gst,filename)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/ProductImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      return render(request,'Product.html',{'msg':'Product Added Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request,'Product.html',{'msg':'Fail To Add Product'})

def ShowAllProducts(request):
    try:
        result = request.session['ADMIN']
        db,cmd=Pool.ConnectionPool()
        q="select P.*,(select C.categoryname from category C where C.categoryid=P.categoryid) from product P"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"ShowAllProduct.html",{'rows':rows})

    except Exception as e:
        return render(request, 'AdminLogin.html')

def DisplayProductById(request):
     pid=request.GET['pid']
     try:
        db,cmd = Pool.ConnectionPool()
        q = "select P.*,(select C.categoryname from category C where C.categoryid=P.categoryid),(select SC.subcategoryname from subcategory SC where SC.subcategoryid=P.subcategoryid)from product P where productid={}".format(pid)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request,"DisplayProductById.html",{'row': row})

     except Exception as e:
        print("Error:", e)
        return render(request,"DisplayProductById.html",{'row': []})

def UpdateDeleteProduct(request):
    pid=request.GET['pid']
    btn=request.GET['btn']
    oldpic = request.GET['oldpic']
    if(btn=='Edit'):
        try:
          categoryid=request.GET['categoryid']
          subcategoryid = request.GET['subcategoryid']
          pname=request.GET['pname']
          description=request.GET['description']
          gst= request.GET['gst']

          db,cmd = Pool.ConnectionPool()
          q="update product set categoryid={},subcategoryid={},productname='{}', description='{}', gst={} where productid={}".format(categoryid,subcategoryid,pname,description,gst,pid)
          cmd.execute(q)
          db.commit()
          db.close()
          return ShowAllProducts(request)

        except Exception as e:
            print("Error:", e)
            return ShowAllProducts(request)

    elif(btn=='Delete'):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "delete from product where productid={}".format(pid)
            cmd.execute(q)
            db.commit()
            db.close()
            os.remove("D:/MM/assets/ProductImages/" + oldpic)
            return ShowAllProducts(request)

        except Exception as e:
            print("Error:", e)
            return ShowAllProducts(request)

def EditProductImage(request):
    try:
        pid=request.GET['pid']
        productname = request.GET['productname']
        productpic = request.GET['productpic']
        row=[pid,productname,productpic]

        return render(request,"EditProductImage.html",{'row':row})
    except Exception as e:
        print("Error:",e)
        return render(request, "EditProductImage.html", {'row': row})


def SaveProductImage(request):
    try:
      pid = request.POST['pid']
      oldpic=request.POST['oldpic']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]

      q="update product set picture='{}' where productid={}".format(filename,pid)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/ProductImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      os.remove("D:/MM/assets/ProductImages/"+oldpic)
      return ShowAllProducts(request)

    except Exception as e:
        print("Error:", e)
        return ShowAllProducts(request)







