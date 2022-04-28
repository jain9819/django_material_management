from django.shortcuts import render
from . import PoolDict

def AdminLogin(request):
    try:
        result=request.session['ADMIN']
        return render(request,'Dashboard.html')
    except Exception as e:
        return render(request, 'AdminLogin.html')


def AdminLogout(request):
    del request.session['ADMIN']
    return render(request, 'AdminLogin.html')

def ShowDashboard(request):
    return render(request, 'Dashboard.html')


def CheckLogin(request):
    emailid=request.GET['emailid']
    password= request.GET['password']

    try:
        q="select * from admins where emailid='{}' and password='{}'".format(emailid,password)
        db, cmd = PoolDict.ConnectionPool()
        cmd.execute(q)
        result = cmd.fetchone()
        if(result):
            request.session['ADMIN']=result
            return render(request,'Dashboard.html',{'result':'result'})
        else:
            return render(request, 'AdminLogin.html', {'result': 'result','msg':'Invalid Email/Password'})
        db.close()

    except Exception as e:
        print('Error:',e)
        return render(request, 'AdminLogin.html', {'result': 'result', 'msg': 'Server Error'})
