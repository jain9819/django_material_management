$(document).ready(function () {
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
    $.getJSON('/fetchsupplier', function (data) {
        $.each(data, function (index, item) {
            $('#supplierid').append($('<option>').text(item[1]).val(item[0]))

        })

    })
})