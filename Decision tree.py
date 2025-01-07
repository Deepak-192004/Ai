import math

# Define a class for the decision tree
class DecisionTree:
    def __init__(self):
        self.tree = None

    # Method to calculate entropy of a dataset
    def entropy(self, data):
        label_counts = {}
        for row in data:
            label = row[-1]
            if label not in label_counts:
                label_counts[label] = 0
            label_counts[label] += 1

        entropy_value = 0
        total = len(data)
        for count in label_counts.values():
            probability = count / total
            entropy_value -= probability * math.log2(probability)
        return entropy_value

    # Method to calculate information gain
    def information_gain(self, data, feature_index):
        # Split data based on feature values
        left_split = [row for row in data if row[feature_index] == 0]
        right_split = [row for row in data if row[feature_index] == 1]

        # Calculate entropy before and after the split
        entropy_before = self.entropy(data)
        entropy_after = (len(left_split) / len(data)) * self.entropy(left_split) + \
                        (len(right_split) / len(data)) * self.entropy(right_split)
        return entropy_before - entropy_after

    # Method to find the best feature to split on
    def best_feature(self, data):
        best_gain = 0
        best_feature_index = None
        for feature_index in range(len(data[0]) - 1):
            gain = self.information_gain(data, feature_index)
            if gain > best_gain:
                best_gain = gain
                best_feature_index = feature_index
        return best_feature_index

    # Method to build the decision tree recursively
    def build_tree(self, data):
        # Base case: If all labels are the same
        labels = [row[-1] for row in data]
        if len(set(labels)) == 1:
            return labels[0]

        # Base case: If no more features to split on
        if len(data[0]) == 1:
            return max(set(labels), key=labels.count)

        # Find the best feature to split on
        best_feature_index = self.best_feature(data)
        left_split = [row for row in data if row[best_feature_index] == 0]
        right_split = [row for row in data if row[best_feature_index] == 1]

        # Recursively build the left and right subtrees
        left_tree = self.build_tree(left_split)
        right_tree = self.build_tree(right_split)

        # Return a node with the best feature and its subtrees
        return {best_feature_index: {'left': left_tree, 'right': right_tree}}

    # Method to fit the tree on training data
    def fit(self, data):
        self.tree = self.build_tree(data)

    # Method to predict the class label of a new instance
    def predict(self, instance):
        tree = self.tree
        while isinstance(tree, dict):
            feature_index = list(tree.keys())[0]
            if instance[feature_index] == 0:
                tree = tree[feature_index]['left']
            else:
                tree = tree[feature_index]['right']
        return tree

# Sample training data: [Feature1, Feature2, ..., FeatureN, Label]
# In this example, 0 indicates 'no' and 1 indicates 'yes'
training_data = [
    [0, 0, 'No'],
    [0, 1, 'No'],
    [1, 0, 'Yes'],
    [1, 1, 'Yes'],
]

# Initialize and train the Decision Tree
dt = DecisionTree()
dt.fit(training_data)

# Predict the class label for a new instance
test_instance = [1, 1]  # Example input
predicted_label = dt.predict(test_instance)

# Output the result
print(f"Predicted label for {test_instance}: {predicted_label}")
