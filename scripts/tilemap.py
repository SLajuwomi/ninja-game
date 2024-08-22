# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Suplicates OK. FASTER

import pygame

# Want to set up collision metrics only for tiles near the player
# In this case the nearest 9 tiles
# Gets all neighboring tiles
NEIGHBOR_OFFSETS = [(-1,0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        # Can use tuples or strings
        # tile     item   
        """
        {(0, 0): 'grass', (0, 1): 'dirt', (9999, 0): 'grass'}
        {'1;1': 'grass', '0;1': 'dirt', '9999;0': 'grass'}
        """  

        for i in range(10):
            self.tilemap[str(3 + i) + ';10'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 10)}
            self.tilemap[ '10;' + str(5 + i)] = {'type': 'stone', 'variant': 1, 'pos': (10, 5 + i)}
    
    def tiles_around(self, pos):
        tiles = []
        # // - integer division, removes remainder (ex. - 3/2 = 1 not 1.5)
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size)) # converts pixel position into grid position
        for offset in NEIGHBOR_OFFSETS:
            # adds base location from tile loc to offsets to get 9 tiles in off set area
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surface):
        for tile in self.offgrid_tiles:
            surface.blit(self.game.assets[tile['type']][tile['variant']], tile['pos'])

        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surface.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
            
        