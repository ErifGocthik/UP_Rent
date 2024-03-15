(function () {
    $(document).ready(function (e) {
        let mw = document.getElementById('modal_window');

        $('.btn-modal').click(function (event) {
            event.preventDefault();
            let split_class_name = event.target.className.split('_');
            let request_id = split_class_name[split_class_name.length - 1];
            let href_denied = document.getElementsByClassName('btn-request-denied')[0];
            let href_accept = document.getElementsByClassName('btn-request-accept')[0];
            $.ajax({
                url:`/moder/request-detail/${request_id}/`,
                type: 'GET',
                dataType: 'json',
                success: function (response)
                {
                    href_denied.setAttribute('href', `/request_denied/${request_id}/`)
                    href_accept.setAttribute('href', `/request_accept/${request_id}/`)
                    $('.request-user').html(`${response['user']}`);
                    $('.request-phone_number').html(`<span>Номер телефона: </span>${response['phone_number']}`);
                    $('.request-email').html(`<span>Эл. почта: </span>${response['email']}`);
                    if (response['patronymic'] == null) {
                        $('.request-fullname').html(`<span>Ф.И.О.: </span>${response['surname']} ${response['name']}`);
                    } else {
                        $('.request-fullname').html(`<span>Ф.И.О.: </span>${response['surname']} ${response['name']} ${response['patronymic']}`);
                    }
                },
                error: function (response)
                {

                },
            })
            $(mw).css({'display': 'flex'});
        });
        $('.btn-close').click(function () {
            $(mw).css({'display': 'none'});
        });
    });
})();