const DISPLAY_MODES = {
    GENERIC : 0,
    ZOOM_ON : 1
};

const RACK_DATA = {
    rack_label : '',
    rack_common_name : '',
    u_number : 12,
    draw_back : false,
    display_mode : DISPLAY_MODES.GENERIC,
};

function update_fixed_pos() {
    let $toolbar = $('#toolbar');
    $('#topbar').css('left', $toolbar.width());
    $('#main-area').css('left', $toolbar.width());
    $('#main-area').css('top', $('#topbar').height());
}

function init_toolbar() {
    $('.toolbar-group').each(function(index, element) {
        let header  = $(element.children).filter('.toolbar-toplevel-header')[0];
        let arrow   = $(header.children).filter('.group-arrow')[0];
        let content = $(element.children).filter('.toolbar-toplevel-content')[0];
        $(header).click(function() {
            $(arrow).toggleClass('down');
            $(content).toggleClass('hidden');
        });
    });
    $('#toolbar-group_rack input').each(function (index, element) {
        $(element).change(update_rack_data);
    })
    $('button#home').click(function () {
        console.log(window.location.href = 'home.html');
    })
    
}

function draw_generic_rack() {
    svg_draw_rack($('#generic-rack-front'), RACK_DATA.u_number);
    svg_draw_rack($('#generic-rack-back'),  RACK_DATA.u_number);

    if (RACK_DATA.draw_back) {
        $('#generic-drawings div#back').css('display', 'block');
    } else {
        $('#generic-drawings div#back').css('display', 'none');
    }
}

function update_rack_data() {
    RACK_DATA.rack_label = $('#rack_label').val();
    RACK_DATA.rack_common_name = $('#rack_common_name').val();
    RACK_DATA.u_number = parseInt($('#u_number').val());
    RACK_DATA.draw_back = $('#draw_back').prop('checked');

    if(RACK_DATA.display_mode == DISPLAY_MODES.GENERIC) {
        draw_generic_rack();
    }
}



$(document).ready(function () {
    init_toolbar();
    update_fixed_pos();
    setInterval(update_fixed_pos, 300);
    update_rack_data();
});