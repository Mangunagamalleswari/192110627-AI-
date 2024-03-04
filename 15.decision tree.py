class Node:
    def __init__(self, feature=None, threshold=None, value=None, left=None, right=None):
        self.feature = feature        # Feature index to split on
        self.threshold = threshold    # Threshold value for the split
        self.value = value            # Value for leaf nodes
        self.left = left              # Left subtree
        self.right = right            # Right subtree

def predict(node, sample):
    if node.value is not None:
        return node.value

    if sample[node.feature] <= node.threshold:
        return predict(node.left, sample)
    else:
        return predict(node.right, sample)

def decision_tree(X, y, max_depth=float('inf')):
    if max_depth == 0 or len(set(y)) == 1:
        return Node(value=max(set(y)))

    num_features = len(X[0])
    best_feature, best_threshold = None, None
    best_gini = float('inf')

    for feature in range(num_features):
        thresholds = set(X[:, feature])
        for threshold in thresholds:
            left_indices = X[:, feature] <= threshold
            right_indices = ~left_indices

            gini_left = gini_index(y[left_indices])
            gini_right = gini_index(y[right_indices])

            weighted_gini = (len(y[left_indices]) * gini_left + len(y[right_indices]) * gini_right) / len(y)

            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_feature = feature
                best_threshold = threshold

    left_indices = X[:, best_feature] <= best_threshold
    right_indices = ~left_indices

    left_subtree = decision_tree(X[left_indices], y[left_indices], max_depth - 1)
    right_subtree = decision_tree(X[right_indices], y[right_indices], max_depth - 1)

    return Node(feature=best_feature, threshold=best_threshold, left=left_subtree, right=right_subtree)

def gini_index(labels):
    classes, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    gini = 1 - np.sum(probabilities ** 2)
    return gini

# Example usage:
import numpy as np

# Create a simple dataset
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 0, 1, 1])

# Build a decision tree
tree = decision_tree(X, y)

# Make predictions
sample = np.array([2.5, 3.5])
prediction = predict(tree, sample)
print("Prediction:", prediction)
