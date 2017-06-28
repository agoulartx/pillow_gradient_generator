"""
Pallets from:
 - http://www.colourlovers.com/blog/2007/10/16/color-inspiration-blends-gradients-steps-oh-my
 - https://colorfulgradients.tumblr.com/
"""


def pallet_picker(pallet_id):
    if pallet_id:
        gradient = pallets.get(pallet_id)
        initial_color, final_color = gradient['initial'], gradient['final']
        return initial_color, final_color


big_bird_barney_blend = {'initial': [255, 222, 7], 'final': [156, 49, 155]}
as_it_is_in_heaven = {'initial': [135, 34, 70], 'final': [222, 171, 115]}
cherry_valance = {'initial': [125, 20, 51], 'final': [215, 99, 119]}
peachbelle = {'initial': [237, 175, 170], 'final': [115, 39, 89]}
sixth_ave_heartache = {'initial': [83, 10, 21], 'final': [224, 127, 21]}
gradigram = {'initial': [139, 0, 85], 'final': [244, 90, 0]}
aqua_rainbow = {'initial': [0, 216, 138], 'final': [166, 0, 224]}
easy_summer = {'initial': [0, 211, 207], 'final': [236, 112, 47]}
candysse = {'initial': [201, 106, 147], 'final': [1, 208, 162]}
super_light = {'initial': [226, 136, 155], 'final': [201, 106, 147]}

pallets = {

    1: big_bird_barney_blend,
    2: as_it_is_in_heaven,
    3: cherry_valance,
    4: peachbelle,
    5: sixth_ave_heartache,
    6: gradigram,
    7: aqua_rainbow,
    8: easy_summer,
    9: candysse,
    10: super_light
}

if __name__ == '__main__':
    pallet_picker(None)
