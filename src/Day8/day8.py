from src.Day8.Forest import Forest

if __name__ == '__main__':
    forest_file = open('forest.txt')
    forest = Forest(forest_file)
    visible_trees = []
    tree_scenic_scores = []
    for x in range(0, forest.rows):
        for y in range(0, forest.columns):
            current_tree = forest.get_tree_at_position(x, y)
            if x == 0 or x == forest.rows - 1:
                visible_trees.append(current_tree)
                continue
            elif y == 0 or y == forest.columns - 1:
                visible_trees.append(current_tree)
                continue
            else:
                west_trees = forest.get_trees_west_of_tree(current_tree)
                east_trees = forest.get_trees_east_of_tree(current_tree)
                north_trees = forest.get_trees_north_of_tree(current_tree)
                south_trees = forest.get_trees_south_of_tree(current_tree)
                visible_from_west = True
                visible_distance_west = 0
                for tree in west_trees:
                    if current_tree.height <= tree:
                        visible_from_west = False
                    if current_tree.height > tree:
                        visible_distance_west += 1
                    else:
                        visible_distance_west += 1
                        break
                visible_from_east = True
                visible_distance_east = 0
                for tree in east_trees:
                    if current_tree.height <= tree:
                        visible_from_east = False
                    if current_tree.height > tree:
                        visible_distance_east += 1
                    else:
                        visible_distance_east += 1
                        break
                visible_from_north = True
                visible_distance_north = 0
                for tree in north_trees:
                    if current_tree.height <= tree:
                        visible_from_north = False
                    if current_tree.height > tree:
                        visible_distance_north += 1
                    else:
                        visible_distance_north += 1
                        break
                visible_from_south = True
                visible_distance_south = 0
                for tree in south_trees:
                    if current_tree.height <= tree:
                        visible_from_south = False
                    if current_tree.height > tree:
                        visible_distance_south += 1
                    else:
                        visible_distance_south += 1
                        break
                if visible_from_south or visible_from_north or visible_from_east or visible_from_west:
                    visible_trees.append(current_tree)
                tree_scenic_scores.append([visible_distance_east, visible_distance_west, visible_distance_south,
                                           visible_distance_north])
    # Part 1 answer
    print(len(visible_trees))

    # Part 2 answer
    highest_scenic_score = 0
    for score in tree_scenic_scores:
        score_total = score[0] * score[1] * score[2] * score[3]
        if score_total > highest_scenic_score:
            highest_scenic_score = score_total
    print(highest_scenic_score)
