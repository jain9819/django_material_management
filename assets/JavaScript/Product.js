$(document).ready(function () {
    $.getJSON('/fetchallcategory', function (data) {
        $.each(data, function (index, item) {
            $('#categoryid').append($('<option>').text(item[1]).val(item[0]))

        })

    })

    $('#categoryid').change(function () {
        $.getJSON('/fetchallsubcategory', {categoryid: $('#categoryid').val()}, function (data) {
            $('#subcategoryid').empty()
            $('#subcategoryid').append($('<option>').text('-SubCategory-'))
            $.each(data, function (index, item) {
                $('#subcategoryid').append($('<option>').text(item[2]).val(item[1]))

            })
        })
    })
})