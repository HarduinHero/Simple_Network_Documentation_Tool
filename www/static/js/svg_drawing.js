const U_HEIGHT  = 44.45;
const U_WIDTH   = 500.8;
const RACK_U_DRAWING = '<rect class="voidbg"    width="500.8" height="44.45" x="0"      y="0" />\
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
const RACK_END_DRAWING = '<rect class="voidbg" width="450" height="17.45" x="25.4" y="27" />\
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

const U_DEVICE_WIDTH = 478.8;
const DEVICE_X_POS = 11;

const RJ45 = {
    height : 13.1,
    width : 16.26,
    drawing : '<rect class="device" width="16.26" height="13.1" x="0" y="0" /> \
    <path class="solid" d="M 2.316036,2.4310353 H 13.943965 V 8.2394838 H 12.363106 V 9.6971714 H 10.442602 V 10.668964 H 8.1300003 5.8173981 V 9.6971714 H 3.8968942 V 8.2394838 H 2.316036 Z" />'
};
const SFP = {
    height : 13.1,
    width : 16.26,
    drawing : '<rect class="device" width="16.26" height="13.1" x="0" y="0" /> \
    <rect class="solid" width="14" height="9.45" x="1.13" y="1.825" />'
};
const SC = {
    height : 0,
    width : 0,
    drawing : ''
};

const INTERFACES_TYPES = {
    'eth' : RJ45,
    'sfp' : SFP,
     'sc' : SC
};

const GROUP_SPACING = 5;


function svg_draw_rack (svg_object, u_size) {
    $(svg_object).attr('width', U_WIDTH);
    $(svg_object).attr('height', U_HEIGHT * (u_size+2));
    $(svg_object).attr('viewBox', `0 0 ${U_WIDTH} ${U_HEIGHT * (u_size+2)}`);
    var content = ''
    for (let index = 0; index < u_size+2; index++) {
        let y_translate = U_HEIGHT * index;
        if (index == 0) {
            content += `<g>${RACK_END_DRAWING}</g>`;
        } else if (index == u_size+1) {
            content += `<g transform="translate(0, ${y_translate}) rotate(180, 250.40, 22.225)">${RACK_END_DRAWING}</g>`;
        } else {
            content += `<g transform="translate(0, ${y_translate})">${RACK_U_DRAWING}</g>`
        }
    }
    $(svg_object).html(content);
}

function svg_interface_string (device_name, interface_type, id, x, y, on_top=false, color_inversed_label=false) {
    content  = `<g id="${device_name}-${interface_type}-${id}" class="interface${color_inversed_label ? ' combo' : ''}" transform="translate(${x}, ${y})">`;  
    content += INTERFACES_TYPES[interface_type].drawing;

    let lable_x = (RJ45.width - 7) / 2
    let label_y = on_top ? (-7.5) : (RJ45.height+1.5)
    content += `<rect class="marking_border" x="${lable_x}" y="${label_y}" height="6" width="7"/>`;
    content += `<text class="smallfont solid" x="${lable_x+0.75}" y="${label_y+4.7}">${id<10 ? '0'+id : id}</text>`;
    content += '</g>';
    return content;
}

function svg_device_string (device_data, force_redraw=false) {

    if (device_data.svg_drawing == null || force_redraw) {

        // Initialaze interfaces origine
        let interfaces_string = '';
        let y_top_line = 0;
        let y_bot_line = 0 + RJ45.height;
        let x_int = 0; // redefined after parameter calculation for index=0

        // Identify combo interfaces id by iterating interfaces
        let combo_interfaces = new Set();
        let viewed_id = new Set();
        for (let group_index = 0; group_index < device_data.interface_groups.length; group_index++) {
            const current_group  = device_data.interface_groups[group_index];
            for (let interface_index = 0; interface_index < current_group.interfaces.length; interface_index++) {
                const current_int = device_data.interface_groups[group_index].interfaces[interface_index];
                if (viewed_id.has(current_int.id)) {
                    combo_interfaces.add(current_int.id);
                } else {
                    viewed_id.add(current_int.id);
                }
            }
        }
    
        // Iterating interfaces to draw them 
        for (let group_index = 0; group_index < device_data.interface_groups.length; group_index++) {
            const current_group  = device_data.interface_groups[group_index];
            const current_patern = current_group.patern;

            for (let interface_index = 0; interface_index < current_group.interfaces.length; interface_index++) {
                const current_int = current_group.interfaces[interface_index];
    
                // Defining interfaces coordinates from group patern
                if (current_patern == '-') {
                    x_int += RJ45.width;
                    y = y_bot_line;
                    on_top = false;
                } else if (current_patern == 'M') {
                    if (interface_index %2 == 0) {
                        y = y_bot_line;
                        on_top = false;
                        x_int += RJ45.width;
                    } else {
                        y = y_top_line;
                        on_top = true;
                    }
                } else if (current_patern == 'W') {
                    if (interface_index %2 == 0) {
                        y = y_top_line;
                        on_top = true;
                        x_int += RJ45.width;
                    } else {
                        y = y_bot_line;
                        on_top = false;
                    }
                }
                // Add interface string with parameters
                is_combo = combo_interfaces.has(current_int.id);
                interfaces_string += svg_interface_string(device_data.label, current_int.type, current_int.id, x_int, y, on_top, is_combo);
            }
            x_int += GROUP_SPACING;
        }
    
        let height = device_data.u_size * U_HEIGHT;
        // centering the interface group
        let y_g_interface = 9.125;
        let x_g_interface = (U_DEVICE_WIDTH-x_int)/2;
    
        content += `<rect class="device" width="${U_DEVICE_WIDTH}" height="${height}" x="0" y="0"/>`;
        content += `<g transform="translate(${x_g_interface}, ${y_g_interface})">${interfaces_string}</g>`;
        return content;

    } else {
        return device_data.svg_drawing;
    }
}