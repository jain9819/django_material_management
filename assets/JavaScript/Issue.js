$(document).ready(function () {
    var d=new Date()
    var cd=(d.getFullYear())+"-"+(d.getMonth()+1)+"-"+(d.getDate())
    $('#issuedate').val(cd)
    $.getJSON('/fetchcategory', function (data) {
        $.each(data, function (index, item) {
            $('#categoryid').append($('<option>').text(item[1]).val(item[0]))

        })

    })

    $('#categoryid').change(function () {
        $.getJSON('/fetchsubcategory', {categoryid: $('#categoryid').val()}, function (data) {
            $('#subcategoryid').empty()
            $('#subcategoryid').append($('<option>').text('-SubCategory-'))
            $.each(data, function (index, item) {
                $('#subcategoryid').append($('<option>').text(item[2]).val(item[1]))

            })
        })
    })
    $('#subcategoryid').change(function () {
        $.getJSON('/fetchproduct', {subcategoryid: $('#subcategoryid').val()}, function (data) {
            $('#productid').empty()
            $('#productid').append($('<option>').text('-Product-'))
            $.each(data, function (index, item) {
                $('#productid').append($('<option>').text(item[3]).val(item[2]))

            })
        })
    })
    $('#productid').change(function () {
        $.getJSON('/fetchfinalproduct', {productid: $('#productid').val()}, function (data) {
            $('#finalproductid').empty()
            $('#finalproductid').append($('<option>').text('-Final Product-'))
            $.each(data, function (index, item) {
                $('#finalproductid').append($('<option>').text(item[4]).val(item[3]))

            })
        })
    })
    $.getJSON('/displayemployeejson', function (data) {
        $.each(data, function (index, item) {
            $('#demand_employeeid').append($('<option>').text((item[1])+" "+(item[2])).val(item[0]))

        })

    })
    $('#finalproductid').change(function () {
        $.getJSON('/getfinalproductbyidjson', {finalproductid: $('#finalproductid').val()}, function (data) {
            $('#currentstocks').html(data.stocks)
        })
    })
     $('#stockissue').keyup(function () {
         if(parseInt($('#currentstocks').html())>=parseInt($('#stockissue').val()))
         { $('#btnsubmit').attr('disabled',false)}
         else{
             $('#btnsubmit').attr('disabled',true)
         }
        })
})