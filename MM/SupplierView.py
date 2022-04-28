from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
def SupplierInterface(request):
    return render(request,'SupplierInterface.html')

def SupplierSubmit(request):
    try:
      suppliername=request.GET['suppliername']
      lnumber = request.GET['lnumber']
      mnumber = request.GET['mnumber']
      email = request.GET['email']
      address = request.GET['address']
      state = request.GET['state']
      city = request.GET['city']
      
      q="insert into supplier(suppliername, landlinenumber, mobilenumber, emailaddress, address, stateid, cityid)values('{}','{}','{}','{}','{}',{},{})".format(suppliername, lnumber, mnumber,email,address,state,city)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      db.commit()
      db.close()
      return render(request, 'SupplierInterface.html',{'msg':'Record Submitted Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request, 'SupplierInterface.html',{'msg':'Fail to Submit'})

def DisplayAllSupplier(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select SP.*,(select C.cityname from cities C where C.cityid=SP.cityid ),(select S.statename from states S where SP.stateid=S.stateid ) from supplier SP"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllSupplier.html",{'rows':rows})

    except Exception as e:
        print("Error:",e)
        return render(request, "DisplayAllSupplier.html", {'rows': []})

def GetSupplierJson(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from supplier"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)

    except Exception as e:
        print("Error:",e)
        return JsonResponse([], safe=False)
