$(document).ready(() => {
    $('#btn_translate').on('click', translate);
    $('#language_code').on('keypress', (e) => {
        if (e.key === 13) {
            translate();
        }
    });
});

function translate() {
    const lang = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/' + lang;
    $.get(url, (data) => {
        $('#hello').html(data.hello);
    });
}
