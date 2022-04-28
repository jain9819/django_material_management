"""MM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import EmployeeView
from . import StateCityView
from . import ProductView
from . import CategoryView
from . import SubCategoryView
from . import CategorySubCategoryView
from . import FinalProductView
from . import UnitsView
from . import FinalSubCatProView
from . import SupplierView
from . import PurchaseView
from . import AdminView
from . import IssueView
from . import EmployeeDashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    # AdminLogin
    path('adminlogin/',AdminView.AdminLogin),
    path('checklogin/',AdminView.CheckLogin),
    path('dashboard/',AdminView.ShowDashboard),
    path('adminlogout/',AdminView.AdminLogout),
    #Employee
    path('employeeinterface/',EmployeeView.EmployeeInterface),
    path('employeesubmit',EmployeeView.EmployeeSubmit),
    path('displayall/',EmployeeView.DisplayAllEmployee),
    path('displayemployeejson/',EmployeeView.DisplayAllEmployeejson),
    path('displayemployeebyid/',EmployeeView.DisplayById),
    path('updatedeleterecord/',EmployeeView.UpdateDeleteRecord),
    path('displayemployeepicture/',EmployeeView.EditEmployeeImage),
    path('saveemployeeimage',EmployeeView.SaveEmployeeImage),


    #States & Cities:-
    path('fetchallstates/',StateCityView.FetchAllStates),
    path('fetchallcities/',StateCityView.FetchAllCities),

    #Category:-
    path('addcategory/',CategoryView.AddCategory),
    path('categorysubmit',CategoryView.CategorySubmit),
    path('displayallcategory/',CategoryView.ShowAllCategory),
    path('categoryjason/',CategoryView.ShowCategoryJson),
    path('displaycategorybyid/',CategoryView.DisplayCategoryById),
    path('editdeletecategory/',CategoryView.UpdateDeleteCategory),
    path('diaplaycategorypic/',CategoryView.EditCategoryImage),
    path('savecategoryimage',CategoryView.SaveCategoryImage),

    #sub-category:-
    path('subcategory/',SubCategoryView.AddSubCategory),
    path('subcategorysubmit',SubCategoryView.SubCategorySubmit),
    path('showallsubcategory',SubCategoryView.ShowAllSubCategory),
    path('displaysubcategorybyid/',SubCategoryView.DisplaySubCategoryById),
    path('editdeletesubcategory/',SubCategoryView.UpdateDeleteSubCategory),
    path('displaysubcategorypic/',SubCategoryView.EditSubCategoryImage),
    path('savesubcategoryimage',SubCategoryView.SaveSubCategoryImage),

    #product:-
    path('product/',ProductView.AddProduct),
    path('productsubmit',ProductView.SubmitProduct),
    path('allproduct/',ProductView.ShowAllProducts),
    path('displayproductbyid/',ProductView.DisplayProductById),
    path('editdeleteproduct/',ProductView.UpdateDeleteProduct),
    path('displayproductpic/',ProductView.EditProductImage),
    path('saveproductimage',ProductView.SaveProductImage),

    #Category & SubCategory
    path('fetchallcategory/',CategorySubCategoryView.FetchAllCategory),
    path('fetchallsubcategory/',CategorySubCategoryView.FetchAllSubcategory),
   #Final Product
    path('finalproduct/',FinalProductView.FinalProductInterface),
    path('finalproductsubmit',FinalProductView.FinalProductSubmit),
    path('showallfinalproduct/',FinalProductView.DisplayAllFinalProduct),
    path('editdeletefinal/',FinalProductView.UpdateDeleteFinalRecord),
    path('savefinalproductimage',FinalProductView.SaveFinalProductImage),
    path('getfinalproductbyidjson/',FinalProductView.DisplayAllFinalProductByIdJson),
    path('searchfinalproductjson/',FinalProductView.SearchFinalProductsJson),
    path('searchfinalproduct/',FinalProductView.SearchFinalProductsAll),

   #Units
    path('fetchallsize/',UnitsView.FetchAllSize),
    path('fetchallweight/',UnitsView.FetchAllWeight),

   #Category & SubCategory & Product
    path('fetchcategory/',FinalSubCatProView.FetchAllCategory),
    path('fetchsubcategory/',FinalSubCatProView.FetchAllSubcategory),
    path('fetchproduct/',FinalSubCatProView.FetchAllProduct),

   #Supplier
    path('supplier/',SupplierView.SupplierInterface),
    path('suppliersubmit/',SupplierView.SupplierSubmit),
    path('showallsupplier/',SupplierView.DisplayAllSupplier),
    path('fetchsupplier/',SupplierView.GetSupplierJson),

    #Purchase
    path('purchase/',PurchaseView.PurchaseInterface),
    path('submitpurchase/',PurchaseView.PurchaseSubmit),
    path('showallpurchase/',PurchaseView.DisplayAllPurchase),
    path('editdeletepurchase/',PurchaseView.UpdateDeletePurchaseRecord),

    # Category & SubCategory & Product
    path('fetchfinalproduct/',FinalSubCatProView.FetchAllFinalProduct),

    #Issue
    path('issue/',IssueView.IssueInterface),
    path('issuesubmit/',IssueView.IssueSubmit),
    path('displayallissue/',IssueView.DisplayAllIssue),
    path('editdeleteissue/',IssueView.UpdateDeleteIssueRecord),


    #
    path('employeelogin/',EmployeeDashboardView.EmployeeLogin),
    path('employeedashboard/',EmployeeDashboardView.ShowEmployeeDashboard),
    path('checkemployeelogin',EmployeeDashboardView.CheckLoginEmployee),
    path('employeelogout/',EmployeeDashboardView.EmployeeLogout),
    #product employee
    path('showallproductsemployee/', EmployeeDashboardView.ShowAllProductsEmployee),
     #Final Product employee
    path('showallfinalproductsemployee/', EmployeeDashboardView.ShowAllFinalProductsEmployee)
]
