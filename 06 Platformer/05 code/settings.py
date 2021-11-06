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
'                            ',
'                            ',
'                            ',
'                            ',
'            CE1E4C          ',
'             noop           ',
' 54P21T    2 2    2         ',
'bbbbbbc   2abbc   ac  abc   ',
'eeeeeef   aheejc  df  dejc  ']


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




