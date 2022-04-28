$(document).ready(function () {
    $.getJSON('/fetchallsize', function (data) {
        $.each(data, function (index, item) {
            $('#sizeunit').append($('<option>').text(item[1]).val(item[0]))

        })

    })
    $.getJSON('/fetchallweight', function (data) {
        $.each(data, function (index, item) {
            $('#weightunit').append($('<option>').text(item[1]).val(item[0]))

        })

    })
})

