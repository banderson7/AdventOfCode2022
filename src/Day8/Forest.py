from src.Day8.Tree import Tree


class Forest:
    def __init__(self, tree_heights):
        self.trees = []
        for line in tree_heights:
            line_text = line.strip()
            forest_row = []
            for tree_size in line_text:
                forest_row.append(tree_size)
            self.trees.append(forest_row)
        self.rows = len(self.trees)
        self.columns = len(self.trees)

    def get_tree_at_position(self, row, column):
        tree = Tree(row, column, self.trees[row][column])
        return tree

    def get_trees_west_of_tree(self, tree: Tree):
        return self.trees[tree.row][0:tree.column][::-1]

    def get_trees_east_of_tree(self, tree: Tree):
        return self.trees[tree.row][tree.column + 1:self.columns]

    def get_trees_north_of_tree(self, tree: Tree):
        north_trees = []
        for i in range(0, tree.row):
            north_trees.append(self.trees[i][tree.column])
        north_trees = north_trees[::-1]
        return north_trees

    def get_trees_south_of_tree(self, tree: Tree):
        south_trees = []
        for j in range(tree.row + 1, self.rows):
            south_trees.append(self.trees[j][tree.column])
        return south_trees
