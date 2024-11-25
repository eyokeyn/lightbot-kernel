def trial_lightbot(move_list, x_dimension, y_dimension):
    global grid
    
    import numpy as np
    
    #   @ sw light
    #   < turn l
    #   > turn r
    #   * jump

    ### GRID
    grid = np.zeros((x_dimension,y_dimension), dtype = int)

    ### STARTING POSITION AND DIRECTİON
    x = 0
    y = 0
    x_dir, y_dir = 0, 0

    x_list = 100*[1, 0, -1, 0]
    y_list = 100*[0, 1, 0, -1]   

    # CHECKING LIST
    for key in move_list:
        direction = [x_list[x_dir], y_list[y_dir]]
        if key == "^":
            x += direction[0]
            y += direction[1]
        elif key == "@":
            if grid[9-y][0+x] == 0:
                grid[9-y][0+x] = 1
            else:
                grid[9-y][0+x] = 0
        elif key == "<":
            x_dir += 1
            y_dir += 1
        elif key == ">":
            x_dir -= 1
            y_dir -= 1
        elif key == "*":
            pass
