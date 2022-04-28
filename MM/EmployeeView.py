from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
import uuid
import random
import os
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def EmployeeInterface(request):
    try:
        result=request.session['ADMIN']
        return render(request,'EmployeeInterface.html')
    except Exception as e:
        return render(request, 'AdminLogin.html')

@xframe_options_exempt
def EmployeeSubmit(request):
    try:
      firstname=request.POST['firstname']
      lastname = request.POST['lastname']
      gender = request.POST['gender']
      birthdate = request.POST['birthdate']
      paddress = request.POST['paddress']
      state = request.POST['state']
      city = request.POST['city']
      caddress = request.POST['caddress']
      email = request.POST['email']
      mnumber = request.POST['mnumber']
      designation = request.POST['designation']

      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
      password="".join(random.sample(['a','b','m','*','%','#','66','9','5'],k=6))

      q="insert into employee(firstname, lastname, gender, dob, paddress, stateid, cityid, caddress, emailaddress, mobilenumber, designation, picture, password)values('{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".format(firstname, lastname, gender, birthdate, paddress, state, city, caddress, email, mnumber, designation,filename,password)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      return render(request, 'EmployeeInterface.html',{'msg':'Record Submitted Successfully'})

    except Exception as e:
        print("Error:",e)
        return render(request, 'EmployeeInterface.html',{'msg':'Fail to Submit'})

@xframe_options_exempt
def DisplayAllEmployee(request):
    try:
        result = request.session['ADMIN']
        db,cmd=Pool.ConnectionPool()
        q="select E.*,(select C.cityname from cities C where C.cityid=E.cityid ),(select S.statename from states S where S.stateid=E.stateid ) from employee E"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAll.html",{'rows':rows})

    except Exception as e:
        return render(request, 'AdminLogin.html')

def DisplayAllEmployeejson(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select E.*,(select C.cityname from cities C where C.cityid=E.cityid ),(select S.statename from states S where S.stateid=E.stateid ) from employee E"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)

    except Exception as e:
        return JsonResponse([], safe=False)


@xframe_options_exempt
def DisplayById(request):
    empid=request.GET['empid']
    try:
            db,cmd = Pool.ConnectionPool()
            q = "select E.*,(select C.cityname from cities C where C.cityid=E.cityid ),(select S.statename from states S where S.stateid=E.stateid ) from employee E where employeeid={}".format(empid)
            cmd.execute(q)
            row = cmd.fetchone()
            db.close()
            return render(request, "DisplayEmployeeById.html", {'row': row})

    except Exception as e:
       print("Error:", e)
       return render(request, "DisplayEmployeeById.html", {'row': []})

@xframe_options_exempt
def UpdateDeleteRecord(request):
    empid=request.GET['empid']
    btn=request.GET['btn']
    if(btn=='Edit'):
        try:
          firstname = request.GET['firstname']
          lastname = request.GET['lastname']
          gender = request.GET['gender']
          birthdate = request.GET['birthdate']
          paddress = request.GET['paddress']
          state = request.GET['state']
          city = request.GET['city']
          caddress = request.GET['caddress']
          email = request.GET['email']
          mnumber = request.GET['mnumber']
          designation = request.GET['designation']
          db,cmd = Pool.ConnectionPool()
          q="update employee set firstname='{}', lastname='{}', gender='{}', dob='{}', paddress='{}', stateid={}, cityid={}, caddress='{}', emailaddress='{}', mobilenumber='{}', designation='{}' where employeeid={}".format(firstname, lastname, gender, birthdate, paddress, state, city, caddress, email, mnumber, designation,empid)
          cmd.execute(q)
          db.commit()
          db.close()
          return DisplayAllEmployee(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllEmployee(request)

    elif(btn=='Delete'):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "delete from employee where employeeid='{}'".format(empid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayAllEmployee(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllEmployee(request)

@xframe_options_exempt
def EditEmployeeImage(request):
    try:
        empid=request.GET['empid']
        firstname = request.GET['firstname']
        lastname = request.GET['lastname']
        picture = request.GET['picture']
        row=[empid,firstname,lastname,picture]

        return render(request,"EditEmployeeImage.html",{'row':row})
    except Exception as e:
        print("Error:",e)
        return render(request, "EditEmployeeImage.html", {'row': row})

@xframe_options_exempt
def SaveEmployeeImage(request):
    try:
      empid = request.POST['empid']
      oldpic=request.POST['oldpic']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]

      q="update employee set picture='{}' where employeeid={}".format(filename,empid)
      db,cmd=Pool.ConnectionPool()
      cmd.execute(q)
      F = open("D:/MM/assets/"+filename, "wb")
      for chunk in picture.chunks():
          F.write(chunk)
      F.close
      db.commit()
      db.close()
      os.remove("D:/MM/assets/"+oldpic)
      return DisplayAllEmployee(request)

    except Exception as e:
        print("Error:", e)
        return DisplayAllEmployee(request)






