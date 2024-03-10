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
    
}

const U_HEIGHT  = 44.45
const U_WIDTH   = 500.8
const RACK_U_DRAWING = ' <rect class="voidbg"    width="500.8" height="44.45" x="0"      y="0" />\
                    <rect class="solid"     width="25.4"  height="44.45" x="475.4"  y="0" />\
                    <rect class="marking"   width="4.76"  height="0.4"   x="489.64" y="44.05" />\
                    <rect class="voidbg"    width="9.52"  height="9.52"  x="476.99" y="33.34" />\
                    <rect class="voidbg"    width="9.52"  height="9.52"  x="476.99" y="17.465" />\
                    <rect class="voidbg"    width="9.52"  height="9.52"  x="476.99" y="1.59" />\
                    <rect class="marking"   width="4.76"  height="0.4"   x="489.64" y="0" />\
                    <rect class="solid"     width="25.4"  height="44.45" x="0"      y="0" />\
                    <rect class="marking"   width="4.76"  height="0.4"   x="6.4"    y="0" />\
                    <rect class="marking"   width="4.76"  height="0.4"   x="6.4"    y="44.05" />\
                    <rect class="voidbg"    width="9.52"  height="9.52"  x="14.29"  y="33.34" />\
                    <rect class="voidbg"    width="9.52"  height="9.52"  x="14.29"  y="17.465" />\
                    <rect class="voidbg"    width="9.52"  height="9.52"  x="14.29"  y="1.59" />';
const RACK_END_DRAWING = '  <rect class="voidbg" width="450" height="17.45" x="25.4" y="27" />\
                            <rect class="solid"  width="450" height="27" x="25.4" y="0" />\
                            <path class="solid"  d="m 0,27 25.4,-27 0,44.45 H 0 Z" />\
                            <path class="solid"  d="M 500.8,27 475.4,0 v 44.45 h 25.4 z" />\
                            <path class="voidbg" d="M 41.974435,3.5 H 45 L 33.025565,23.5 H 30 Z" />\
                            <path class="voidbg" d="m 56.873253,3.5 h 3 L 48,23.5 h -3 z" />\
                            <path class="voidbg" d="M 71.974435,3.5 H 75 L 63.025565,23.5 H 60 Z" />\
                            <path class="voidbg" d="m 86.873253,3.5 h 3 L 78,23.5 h -3 z" />\
                            <path class="voidbg" d="M 101.97444,3.5 H 105 L 93.02557,23.5 H 90 Z" />\
                            <path class="voidbg" d="m 116.87325,3.5 h 3 L 108,23.5 h -3 z" />\
                            <path class="voidbg" d="M 131.97444,3.5 H 135 L 123.02557,23.5 H 120 Z" />\
                            <path class="voidbg" d="m 146.87325,3.5 h 3 L 138,23.5 h -3 z" />\
                            <path class="voidbg" d="M 161.97443,3.5 H 165 L 153.02556,23.5 H 150 Z" />\
                            <path class="voidbg" d="m 176.87325,3.5 h 3 L 168,23.5 h -3 z" />\
                            <path class="voidbg" d="M 191.97443,3.5 H 195 L 183.02556,23.5 H 180 Z" />\
                            <path class="voidbg" d="m 206.87326,3.5 h 3 L 198,23.5 h -3 z" />\
                            <path class="voidbg" d="M 221.97444,3.5 H 225 L 213.02557,23.5 H 210 Z" />\
                            <path class="voidbg" d="m 236.87325,3.5 h 3 L 228,23.5 h -3 z" />\
                            <path class="voidbg" d="M 251.97444,3.5 H 255 L 243.02557,23.5 H 240 Z" />\
                            <path class="voidbg" d="m 266.87325,3.5 h 3 L 258,23.5 h -3 z" />\
                            <path class="voidbg" d="M 281.97443,3.5 H 285 L 273.02556,23.5 H 270 Z" />\
                            <path class="voidbg" d="m 296.87325,3.5 h 3 L 288,23.5 h -3 z" />\
                            <path class="voidbg" d="M 311.97443,3.5 H 315 l -11.97444,20 H 300 Z" />\
                            <path class="voidbg" d="m 326.87325,3.5 h 3 L 318,23.5 h -3 z" />\
                            <path class="voidbg" d="M 341.97444,3.5 H 345 L 333.02557,23.5 H 330 Z" />\
                            <path class="voidbg" d="m 356.87325,3.5 h 3 L 348,23.5 h -3 z" />\
                            <path class="voidbg" d="M 371.97444,3.5 H 375 l -11.97443,20 H 360 Z" />\
                            <path class="voidbg" d="m 386.87325,3.5 h 3 L 378,23.5 h -3 z" />\
                            <path class="voidbg" d="M 401.97443,3.5 H 405 L 393.02556,23.5 H 390 Z" />\
                            <path class="voidbg" d="m 416.87325,3.5 h 3 L 408,23.5 h -3 z" />\
                            <path class="voidbg" d="M 431.97443,3.5 H 435 L 423.02556,23.5 H 420 Z" />\
                            <path class="voidbg" d="m 446.87326,3.5 h 3 L 438,23.5 h -3 z" />\
                            <path class="voidbg" d="M 461.97444,3.5 H 465 L 453.02557,23.5 H 450 Z" />';
const RACK_DATA = {
    rack_label : '',
    rack_common_name : '',
    u_number : 12,
    draw_back : false
}

function draw_rack() {
    $('svg').each(function (index, element) {
        $(element).width(U_WIDTH);
        $(element).height(U_HEIGHT * (RACK_DATA.u_number+2));

        var content = ''
        for (let index = 0; index < RACK_DATA.u_number+2; index++) {
            let y_translate = U_HEIGHT * index;
            if (index == 0) {
                content += `<g>${RACK_END_DRAWING}</g>`;
            } else if (index == RACK_DATA.u_number+1) {
                content += `<g transform="translate(0, ${y_translate}) rotate(180, 250.40, 22.225)">${RACK_END_DRAWING}</g>`;
            } else {
                content += `<g transform="translate(0, ${y_translate})">${RACK_U_DRAWING}</g>`
            }
        }
        $(element).html(content)
    });
}

function update_rack_data() {
    RACK_DATA.rack_label = $('#rack_label').val();
    RACK_DATA.rack_common_name = $('#rack_common_name').val();
    RACK_DATA.u_number = parseInt($('#u_number').val());
    RACK_DATA.draw_back = $('#draw_back').prop('checked');

    console.log(RACK_DATA);

    draw_rack();
}



$(document).ready(function () {



    init_toolbar();

    update_fixed_pos();
    setInterval(update_fixed_pos, 300);

    update_rack_data
});