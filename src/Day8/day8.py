if __name__ == '__main__':
    forest_file = open('forest.txt')
    forest = []
    for line in forest_file:
        line_text = line.strip()
        forest_row = []
        for tree in line_text:
            forest_row.append(tree)
        forest.append(forest_row)
    visible_trees = []
    columns = len(forest[0])
    rows = len(forest)
    for x in range(0, columns):
        for y in range(0, rows):
            current_tree = forest[x][y]
            if x == 0 or x == columns - 1:
                visible_trees.append(current_tree)
                continue
            elif y == 0 or y == rows - 1:
                visible_trees.append(current_tree)
                continue
            else:
                west_trees = forest[y][0:x]
                east_trees = forest[y][x + 1:columns]
                north_trees = []
                for i in range(y):
                    north_trees.append(forest[i][x])
                south_trees = []
                for j in range(y + 1, rows):
                    south_trees.append(forest[j][x])
                # TODO: Compare current tree to the above arrays. Add to visible_trees if higher
    print(len(visible_trees))
