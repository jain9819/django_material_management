$(document).ready(function () {
    $('#pattern').keyup(function () {
        $.getJSON('/searchfinalproductjson', {pattern:$('#pattern').val()},function (data) {
            var htm="<table class='table'><thead class='thead-dark'><tr><th>Category ID</th><th>SubCategory ID</th><th>Product ID</th><th>FinalProduct ID</th><th>FinalProduct Name</th><th>Colour</th><th>Size</th><th>Weight</th><th>Stocks</th><th>Price</th><th>Picture</th></tr></thead>"
          $.each(data, function (index, item) {
              htm+="<tr><td>"+item.categoryid+"/"+item.categoryname+"</td><td>"+item.subcategoryid+"/"+item.subcategoryname+"</td><td>"+item.productid+"/"+item.productname+"</td><td>"+item.finalproductid+"</td><td>"+item.finalproductname+"</td><td>"+item.color+"</td><td>"+item.sizee+"/"+item.sizeunit+"</td><td>"+item.weight+"/"+item.weightunit+"</td><td>"+item.stocks+"</td><td>"+item.price+"</td><td><img src='/static/FinalProductImages/"+item.finalproductpicture+"' width='40'></td></tr>"
          })
            htm+="</table>"
            $('#result').html(htm)
        })

    })

})