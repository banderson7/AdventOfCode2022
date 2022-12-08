if __name__ == '__main__':
    forest_file = open('forest.txt')
    forest = []
    for line in forest_file:
        line_text = line.strip()
        forest_row = []
        for tree in line_text:
            forest_row.append(int(tree))
        forest.append(forest_row)
    visible_trees = []
    columns = len(forest[0])
    rows = len(forest)
    for x in range(0, rows):
        for y in range(0, columns):
            current_tree = forest[x][y]
            if x == 0 or x == rows - 1:
                visible_trees.append(current_tree)
                continue
            elif y == 0 or y == columns - 1:
                visible_trees.append(current_tree)
                continue
            else:
                west_trees = forest[x][0:y]
                visible_from_west = True
                for tree in west_trees:
                    if current_tree <= tree:
                        visible_from_west = False
                east_trees = forest[x][y + 1:columns]
                visible_from_east = True
                for tree in east_trees:
                    if current_tree <= tree:
                        visible_from_east = False
                north_trees = []
                for i in range(0, x):
                    north_trees.append(forest[i][y])
                visible_from_north = True
                for tree in north_trees:
                    if current_tree <= tree:
                        visible_from_north = False
                south_trees = []
                for j in range(x + 1, rows):
                    south_trees.append(forest[j][y])
                visible_from_south = True
                for tree in south_trees:
                    if current_tree <= tree:
                        visible_from_south = False
                if visible_from_south or visible_from_north or visible_from_east or visible_from_west:
                    visible_trees.append(current_tree)
    print(len(visible_trees))
