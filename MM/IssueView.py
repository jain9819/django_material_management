from django.shortcuts import render
from . import Pool

def IssueInterface(request):
    result = request.session['EMPLOYEE']
    return render(request, 'IssueInterface.html',{'result':result})


def IssueSubmit(request):
    try:
        employeeid = request.GET['employeeid']
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        productid = request.GET['productid']
        finalproductid = request.GET['finalproductid']
        demand_employeeid = request.GET['demand_employeeid']
        dateissue = request.GET['dateofissue']
        stockissue = request.GET['stockissue']
        remark = request.GET['remark']

        q = "insert into issue(employeeid, categoryid, subcategoryid, productid, finalproductid, demand_employeeid, dateofissue, stockissue, remark)values({},{},{},{},{},{},'{}',{},'{}')".format(employeeid, categoryid, subcategoryid, productid, finalproductid, demand_employeeid, dateissue, stockissue, remark)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        # update stocks
        q = "update finalproduct set stocks=stocks-{} where finalproductid={}".format(stockissue, finalproductid)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, 'IssueInterface.html', {'msg': 'Record Submitted Successfully'})

    except Exception as e:
        print("Error:", e)
        return render(request, 'IssueInterface.html', {'msg': 'Fail to Submit'})

def DisplayAllIssue(request):
    try:
        result = request.session['EMPLOYEE']
        db,cmd=Pool.ConnectionPool()
        q="select I.*,(select C.categoryname from category C where C.categoryid=I.categoryid),(select SC.subcategoryname from subcategory SC where SC.subcategoryid=I.subcategoryid),(select P.productname from product P where P.productid=I.productid),(select FP.finalproductname from finalproduct FP where FP.finalproductid=I.finalproductid),(select E.firstname from employee E where E.employeeid=I.demand_employeeid),(select E.lastname from employee E where E.employeeid=I.demand_employeeid) from issue I "
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllIssue.html",{'rows':rows,'result':result})

    except Exception as e:
        print("Error:",e)
        return render(request, "DisplayAllIssue.html", {'rows': []})

def UpdateDeleteIssueRecord(request):
    issueid=request.GET['issueid']
    btn=request.GET['btn']
    if(btn=='Edit'):
        try:
            employeeid = request.GET['employeeid']
            categoryid = request.GET['categoryid']
            subcategoryid = request.GET['subcategoryid']
            productid = request.GET['productid']
            finalproductid = request.GET['finalproductid']
            demand_employeeid = request.GET['demand_employeeid']
            dateissue = request.GET['dateofissue']
            stockissue = request.GET['stockissue']
            remark = request.GET['remark']
            db,cmd = Pool.ConnectionPool()
            q="update issue set employeeid={}, categoryid={}, subcategoryid={}, productid={}, finalproductid={}, demand_employeeid={}, dateofissue='{}', stockissue={}, remark='{}' where issueid={}".format(employeeid, categoryid, subcategoryid, productid, finalproductid, demand_employeeid, dateissue, stockissue, remark,issueid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayAllIssue(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllIssue(request)

    elif(btn=='Delete'):
        try:
            db, cmd = Pool.ConnectionPool()
            q = "delete from issue where issueid={}".format(issueid)
            cmd.execute(q)
            db.commit()
            db.close()
            return DisplayAllIssue(request)

        except Exception as e:
            print("Error:", e)
            return DisplayAllIssue(request)
