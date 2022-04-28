from django.http import JsonResponse
from . import Pool

def FetchAllCategory(request):
    try:
        db, cmd = Pool.ConnectionPool()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return JsonResponse(rows, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse(rows, safe=False)

def FetchAllSubcategory(request):
 try:
  db,cmd=Pool.ConnectionPool()
  categoryid=request.GET['categoryid']
  q='select * from subcategory where categoryid={}'.format(categoryid)
  cmd.execute(q)
  rows=cmd.fetchall()
  db.close()
  return JsonResponse(rows,safe=False)
 except Exception as e:
  print('Error:',e)
  return JsonResponse([], safe=False)
