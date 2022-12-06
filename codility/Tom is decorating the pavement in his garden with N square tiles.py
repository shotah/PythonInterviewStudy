# four triangles of different colors (white - 'W', red - 'R', green - 'G' and blue - 'B')
# upper, right, bottom and left triangle
# Tom arranged the tiles in a row
# Given A = ["RGBW", "GBRW"], the function should return 1.

def rotate_right(tile: str) -> str:
    """
    Rotates the tile clockwise
    """
    arr_tile = list(tile)
    arr_tile.insert(0, arr_tile.pop())
    after_tile = "".join(arr_tile)
    print("rotating right", tile, after_tile)
    return after_tile

def rotate_left(tile: str) -> str:
    """
    rotates tile counter clockwise
    """    
    arr_tile = list(tile)
    arr_tile.append(arr_tile.pop(0))
    after_tile = "".join(arr_tile)
    print("rotating left", tile, after_tile)
    return after_tile

def solve_tile_pattern(a):
    """
    Solves tile count for current patter set.
    """
    rotate_count = 0
    previous_right_color = None
    left_color = None
    for tile in a:
        if previous_right_color:
            left_color = tile[3]
            print(previous_right_color, left_color)
            if left_color != previous_right_color:
                print(tile)
                index_to_move = tile.index(previous_right_color)
                print(index_to_move)
                if index_to_move == 0:
                    rotate_count += 1
                    tile = rotate_left(tile)
                elif index_to_move == 2:
                    rotate_count += 1
                    tile = rotate_right(tile)
                elif index_to_move == 1:
                    rotate_count += 2
                    tile = rotate_right(tile)
                    tile = rotate_right(tile)
        left_color = tile[3]
        right_color = tile[1]
        print(previous_right_color, left_color)
        previous_right_color = right_color
    return rotate_count

def solution(a):
    """
    Attempts any order of tiles to get the min number of tiles
    """
    if not a: return 0
    tile_count = len(a)
    min_count = float('inf')
    while tile_count > 0:
        cur_count = solve_tile_pattern(a)
        a.insert(0, a.pop())
        min_count = min(min_count, cur_count)
        tile_count -= 1
    return min_count

      

a = ["RGBW", "GBRW"]
a = ['GBRW', 'RBGW', 'BWGR', 'BRGW']
a = ['WBGR', 'WBGR', 'WRGB', 'WRGB', 'RBGW']
a = ["GBRW", "RBGW", "BWGR", "BRGW"]
s = solution(a)
print(
    s
)
