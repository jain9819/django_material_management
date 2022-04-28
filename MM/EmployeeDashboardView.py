from django.shortcuts import render
from . import PoolDict
from . import Pool
import os
import uuid

def EmployeeLogin(request):
    try:
        result=request.session['EMPLOYEE']
        return render(request,'EmployeeDashboard.html',{'result':result})
    except Exception as e:
        return render(request,'EmployeeLogin.html')

def EmployeeLogout(request):
    del request.session['EMPLOYEE']
    return render(request, 'EmployeeLogin.html')

def ShowEmployeeDashboard(request):
    try:
        result = request.session['EMPLOYEE']
        return render(request, 'EmployeeDashboard.html',{'result':result})
    except Exception as e:
        return render(request, 'EmployeeLogin.html')


def CheckLoginEmployee(request):
    emailid=request.POST['emailid']
    password= request.POST['password']

    try:
        q="select * from employee where emailaddress='{}' and password='{}'".format(emailid,password)
        db, cmd = PoolDict.ConnectionPool()
        cmd.execute(q)
        result = cmd.fetchone()
        if(result):
            request.session['EMPLOYEE']=result
            return render(request,'EmployeeDashboard.html',{'result':result})
        else:
            return render(request, 'EmployeeLogin.html', {'result': result,'msg':'Invalid Email/Password'})
        db.close()

    except Exception as e:
        print('Error:',e)
        return render(request, 'EmployeeLogin.html', { 'msg': 'Server Error'})


# Display Product For Employee
# ==============================================================================
def ShowAllProductsEmployee(request):
    try:
        result = request.session['EMPLOYEE']
        db, cmd = Pool.ConnectionPool()
        q = "select P.*,(select C.categoryname from category C where C.categoryid=P.categoryid) from product P"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return render(request, "ShowAllProductEmployee.html", {'rows': rows,'result':result})

    except Exception as e:
        return render(request, 'EmployeeLogin.html')


# Display Final Product For Employee
# ==============================================================================
def ShowAllFinalProductsEmployee(request):
        try:
            result = request.session['EMPLOYEE']
            db, cmd = Pool.ConnectionPool()
            q = "select FP.*,(select S.sizeunitname from sizeunit S where S.sizeunitid=FP.sizeunitid),(select W.weightunitname from weightunit W where W.weightunitid=FP.weightunitid),(select C.categoryname from category C where C.categoryid=FP.categoryid),(select S.subcategoryname from subcategory S where S.subcategoryid=FP.subcategoryid),(select P.productname from product P where P.productid=FP.productid) from finalproduct FP"
            cmd.execute(q)
            rows = cmd.fetchall()
            db.close()
            return render(request, "DisplayAllFinalProductEmployee.html", {'rows': rows,'result':result})

        except Exception as e:
            return render(request, 'EmployeeLogin.html')
