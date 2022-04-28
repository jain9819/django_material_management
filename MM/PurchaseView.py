from django.shortcuts import render
from . import Pool

def PurchaseInterface(request):
    result = request.session['EMPLOYEE']
    return render(request,'PurchaseInterface.html',{'result':result})

def PurchaseSubmit(request):
    try:
      employeeid=request.GET['employeeid']
      categoryid = request.GET['categoryid']
      subcategoryid = request.GET['subcategoryid']
      productid = request.GET['productid']
      finalproductid = request.GET['finalproductid']
      date = request.GET['date']
      supplierid = request.GET['supplierid']
      stocks = request.GET['stocks']
      amount = request.GET['amount']
      
      q="insert into purchase(employeeid, categoryid, subcategoryid, productid, finalproductid, dateofpurchase, supplierid, stocks, amount)values({},{},{},{},{},'{}',{},{},{})".format(employeeid,categoryid,subcategoryid,productid,finalproductid,date,supplierid,stocks,amount)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      #update stocks
      q="update finalproduct set price=((price+{})/2),stocks=stocks+{} where finalproductid={}".format(amount,stocks,finalproductid)
      cmd.execute(q)
      print('xxxxxxxxxxxxxxxxxxxxxxxxxxccccccccccc')
      print(q)
      db.commit()
      db.close()
      return render(request, 'PurchaseInterface.html',{'msg':'Record Submitted Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request, 'PurchaseInterface.html',{'msg':'Fail to Submit'})

def DisplayAllPurchase(request):
    try:
        result = request.session['EMPLOYEE']
        db,cmd=Pool.ConnectionPool()
        q="select PR.*,(select C.categoryname from category C where C.categoryid=PR.categoryid),(select SC.subcategoryname from subcategory SC where SC.subcategoryid=PR.subcategoryid),(select P.productname from product P where P.productid=PR.productid),(select FP.finalproductname from finalproduct FP where FP.finalproductid=PR.finalproductid),(select S.suppliername from supplier S where S.supplierid=PR.supplierid) from purchase PR "
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllPurchase.html",{'rows':rows,'result':result})

    except Exception as e:
        print("Error:",e)
        return render(request, "DisplayAllPurchase.html", {'rows': []})

def UpdateDeletePurchaseRecord(request):
    transactionid=request.GET['transactionid']
    btn=request.GET['btn']
    if(btn=='Edit'):
        try:
          employeeid = request.GET['employeeid']
          categoryid = request.GET['categoryid']
          subcategoryid = request.GET['subcategoryid']
          productid = request.GET['productid']
          finalproductid = request.GET['finalproductid']
          date = request.GET['date']
          supplierid = request.GET['supplierid']
          stocks = request.GET['stocks']
          amount = request.GET['amount']
          db,cmd = Pool.ConnectionPool()
          q="update purchase set employeeid={}, categoryid={}, subcategoryid={}, productid={}, finalproductid={}, dateofpurchase='{}', supplierid={}, stocks={}, amount={} where transactionid={}".format(employeeid,categoryid,subcategoryid,productid,finalproductid,date,supplierid,stocks,amount,transactionid)
          cmd.execute(q)
          db.commit()
          db.close()
          return DisplayAllPurchase(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllPurchase(request)

    elif(btn=='Delete'):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "delete from purchase where transactionid={}".format(transactionid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayAllPurchase(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllPurchase(request)
