from django.http import JsonResponse
from . import Pool

def FetchAllSize(request):
 try:
  db,cmd=Pool.ConnectionPool()
  q='select * from sizeunit'
  cmd.execute(q)
  rows=cmd.fetchall()
  db.close()
  return JsonResponse(rows,safe=False)
 except Exception as e:
  print(e)
  return JsonResponse([], safe=False)

def FetchAllWeight(request):
 try:
  db,cmd=Pool.ConnectionPool()
  q='select * from weightunit'
  cmd.execute(q)
  rows=cmd.fetchall()
  db.close()
  return JsonResponse(rows,safe=False)
 except Exception as e:
  print('Error:',e)
  return JsonResponse([], safe=False)
