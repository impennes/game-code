"""
terrain: a-p
catus: 1
plant: 2
rock: 3
skeleton: 4
tree: 5
crate: T
player: P

"""



level_map = [
'                            ',
'                            ',
'          T2                 ',
'          np                ',
'    C135EC                  ',
'     noop                   ',
'1T          CE1E45TC        ',
'np           noooop         ',
'431P25T    232    2T  322T1 ',
'abbbbbc   2abbcT  ac  abbbc ',
'deeeeef   aheejc  df  deeejc']


tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
others = {
    '1': 'cactus',
    '2': 'plant',
    '3': 'rock',
    '4': 'skeleton',
    '5': 'tree'
}




