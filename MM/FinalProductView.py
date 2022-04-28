from django.shortcuts import render
from django.http import JsonResponse
import uuid
from . import Pool
from . import PoolDict
import os
from django.http import JsonResponse

def FinalProductInterface(request):
    try:
        result = request.session['ADMIN']
        return render(request,'FinalProductInterface.html')
    except Exception as e:
        return render(request, 'AdminLogin.html')

def FinalProductSubmit(request):
    try:
      categoryid=request.POST['categoryid']
      subcategoryid = request.POST['subcategoryid']
      productid = request.POST['productid']
      finalproductname = request.POST['finalproductname']
      color = request.POST['color']
      sizee = request.POST['sizee']
      sizeunit = request.POST['sizeunit']
      weight = request.POST['weight']
      weightunit = request.POST['weightunit']
      stocks = request.POST['stocks']
      price = request.POST['price']

      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]

      q="insert into finalproduct(categoryid, subcategoryid, productid,finalproductname, color, sizee, sizeunitid, weight, weightunitid, stocks, price, finalproductpicture)values({},{},{},'{}','{}',{},{},{},{},{},{},'{}')".format(categoryid, subcategoryid, productid, finalproductname, color, sizee, sizeunit, weight, weightunit, stocks, price,filename)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/FinalProductImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      return render(request, 'FinalProductInterface.html',{'msg':'Record Submitted Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request, 'FinalProductInterface.html',{'msg':'Fail to Submit'})

def DisplayAllFinalProduct(request):
    try:
        result = request.session['ADMIN']
        db,cmd=Pool.ConnectionPool()
        q="select FP.*,(select S.sizeunitname from sizeunit S where S.sizeunitid=FP.sizeunitid),(select W.weightunitname from weightunit W where W.weightunitid=FP.weightunitid),(select C.categoryname from category C where C.categoryid=FP.categoryid),(select S.subcategoryname from subcategory S where S.subcategoryid=FP.subcategoryid),(select P.productname from product P where P.productid=FP.productid) from finalproduct FP"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllFinalProduct.html",{'rows':rows})

    except Exception as e:
        return render(request, 'AdminLogin.html')


def DisplayAllFinalProductByIdJson(request):
    finalproductid=request.GET['finalproductid']
    try:
        result = request.session['EMPLOYEE']
        db,cmd=PoolDict.ConnectionPool()
        q="select * from finalproduct where finalproductid={}".format(finalproductid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return JsonResponse(row,safe=False)

    except Exception as e:
        return JsonResponse([], safe=False)



def UpdateDeleteFinalRecord(request):
    fpid=request.GET['fpid']
    btn=request.GET['btn']
    oldpic = request.GET['oldpic']
    if(btn=='Edit'):
        try:
          categoryid = request.GET['categoryid']
          subcategoryid = request.GET['subcategoryid']
          productid = request.GET['productid']
          finalproductname = request.GET['finalproductname']
          color = request.GET['color']
          sizee = request.GET['sizee']
          sizeunit = request.GET['sizeunit']
          weight = request.GET['weight']
          weightunit = request.GET['weightunit']
          stocks = request.GET['stocks']
          price = request.GET['price']
          db,cmd = Pool.ConnectionPool()
          q="update finalproduct set categoryid={}, subcategoryid={}, productid={},finalproductname='{}', color='{}', sizee={}, sizeunitid={}, weight={}, weightunitid={}, stocks={}, price={} where finalproductid={}".format(categoryid, subcategoryid, productid, finalproductname, color, sizee, sizeunit, weight, weightunit, stocks, price,fpid)
          cmd.execute(q)
          db.commit()
          db.close()
          return DisplayAllFinalProduct(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllFinalProduct(request)

    elif(btn=='Delete'):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "delete from finalproduct where finalproductid={}".format(fpid)
            cmd.execute(q)
            db.commit()
            db.close()
            os.remove("D:/MM/assets/FinalProductImages/" + oldpic)
            return DisplayAllFinalProduct(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllFinalProduct(request)

def SaveFinalProductImage(request):
    try:
      fpid1 = request.POST['fpid1']
      oldimg=request.POST['oldimg']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]

      q="update finalproduct set finalproductpicture='{}' where finalproductid={}".format(filename,fpid1)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/FinalProductImages/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      os.remove("D:/MM/assets/FinalProductImages/"+oldimg)
      return DisplayAllFinalProduct(request)

    except Exception as e:
        print("Error:", e)
        return DisplayAllFinalProduct(request)


def SearchFinalProductsJson(request):
    pattern=request.GET['pattern']
    try:
        result = request.session['EMPLOYEE']
        db,cmd=PoolDict.ConnectionPool()
        q="select FP.*,(select C.categoryname from category C where C.categoryid=FP.categoryid) as categoryname ,(select S.subcategoryname from subcategory S where S.subcategoryid=FP.subcategoryid) as subcategoryname ,(select P.productname from product P where P.productid=FP.productid) as productname ,(select S.sizeunitname from sizeunit S where S.sizeunitid=FP.sizeunitid) as sizeunit ,(select W.weightunitname from weightunit W where W.weightunitid=FP.weightunitid) as weightunit from finalproduct FP where finalproductname like '%{}%'".format(pattern)
        cmd.execute(q)
        row=cmd.fetchall()
        db.close()
        return JsonResponse(row,safe=False)

    except Exception as e:
        return JsonResponse([], safe=False)

def SearchFinalProductsAll(request):
    try:
        result = request.session['EMPLOYEE']
        return render(request,'SearchFinalProductsEmployee.html',{'result':result})
    except Exception as e:
        return render(request, 'EmployeeLogin.html')

