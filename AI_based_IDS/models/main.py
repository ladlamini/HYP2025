
# NB come back to check thhat the model is correct !!!
import pandas as pd
import numpy as np
import math
import random
from collections import Counter

class OptimizedDecisionTree:
    def __init__(self, max_depth=5, min_samples_split=100):  # Reduced depth, increased min samples
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.tree = None
        
    def _gini(self, y):     
        counts = np.bincount(y)
        probabilities = counts / len(y)
        return 1.0 - np.sum(probabilities ** 2)
    
    def _find_best_split_fast(self, X, y):
        best_gain = -1
        best_feature = None
        best_threshold = None
        
        n_features = X.shape[1]
        
        # 5 features instead of all 78
        feature_indices = random.sample(range(n_features), min(5, n_features))
        
        for feature_idx in feature_indices:
            # 10 random thresholds instead of all of the unique values
            unique_vals = np.unique(X[:, feature_idx])
            if len(unique_vals) > 10:
                thresholds = np.random.choice(unique_vals, 10, replace=False)
            else:
                thresholds = unique_vals
            
            for threshold in thresholds:
                # split 
                left_mask = X[:, feature_idx] <= threshold
                right_mask = ~left_mask
                
                if np.sum(left_mask) < 10 or np.sum(right_mask) < 10:
                    continue
                
                # Gini gain calculation
                n_total = len(y)
                gini_parent = self._gini(y)
                
                gini_left = self._gini(y[left_mask])
                gini_right = self._gini(y[right_mask])
                
                weight_left = np.sum(left_mask) / n_total
                weight_right = np.sum(right_mask) / n_total
                
                gini_gain = gini_parent - (weight_left * gini_left + weight_right * gini_right)
                
                if gini_gain > best_gain:
                    best_gain = gini_gain
                    best_feature = feature_idx
                    best_threshold = threshold
        
        return best_feature, best_threshold, best_gain
    
    def _build_tree(self, X, y, depth=0):
        #tree building
        n_samples = X.shape[0]
        
        # Stopping conditions - more aggressive
        if (depth >= self.max_depth or 
            len(np.unique(y)) == 1 or 
            n_samples < self.min_samples_split):
            return Counter(y).most_common(1)[0][0]  # Majority class
        
        # Find best split
        feature_idx, threshold, gain = self._find_best_split_fast(X, y)
        
        if gain <= 0:  # No positive gain
            return Counter(y).most_common(1)[0][0]
        
        # Split data
        left_mask = X[:, feature_idx] <= threshold
        right_mask = ~left_mask
        
        # incase split is too unbalanced
        if np.sum(left_mask) < 50 or np.sum(right_mask) < 50:
            return Counter(y).most_common(1)[0][0]
        
        # Recursively build subtrees
        left_subtree = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        right_subtree = self._build_tree(X[right_mask], y[right_mask], depth + 1)
        
        return {
            'feature_idx': feature_idx,
            'threshold': threshold,
            'left': left_subtree,
            'right': right_subtree
        }
    #Train the decision tree
    def fit(self, X, y):
  
        self.tree = self._build_tree(X, y)
    #predict a single instance
    def _predict_sample(self, x, tree):
    
        if not isinstance(tree, dict):
            return tree
            
        if x[tree['feature_idx']] <= tree['threshold']:
            return self._predict_sample(x, tree['left'])
        else:
            return self._predict_sample(x, tree['right'])
    
    def predict(self, X):
       #predict for all instances
        return np.array([self._predict_sample(x, self.tree) for x in X])

class FastRandomForest:
    def __init__(self, n_estimators=20, max_depth=5, min_samples_split=100):  # Reduced estimators so its a bit faster
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.trees = []
        self.feature_indices = []
        
        #train random forest now
    def fit(self, X, y):
        self.trees = []
        self.feature_indices = []
        
        n_features = X.shape[1]
        n_features_to_use = int(math.sqrt(n_features))  
        
        print(f"Training {self.n_estimators} trees...")
        
        for i in range(self.n_estimators):
            if i % 5 == 0:
                print(f"  Training tree {i+1}/{self.n_estimators}")
            
            # Bootstrap sample (smaller sample for speed for now)
            n_boot_samples = min(10000, X.shape[0])  
            indices = np.random.choice(X.shape[0], n_boot_samples, replace=True)
            X_boot, y_boot = X[indices], y[indices]
            
            # Random feature selection
            feature_indices = random.sample(range(n_features), n_features_to_use)
            X_boot_subset = X_boot[:, feature_indices]
            
            # Train decision tree
            tree = OptimizedDecisionTree(max_depth=self.max_depth, 
                                       min_samples_split=self.min_samples_split)
            tree.fit(X_boot_subset, y_boot)
            
            self.trees.append(tree)
            self.feature_indices.append(feature_indices)
    
    def predict(self, X):
        #Predict using the random forest algo above
        all_predictions = []
        
        for i, (tree, features) in enumerate(zip(self.trees, self.feature_indices)):
            if i % 5 == 0:
                print(f"  Tree {i+1}/{len(self.trees)} predicting...")
            X_subset = X[:, features]
            predictions = tree.predict(X_subset)
            all_predictions.append(predictions)
        
        # Majority voting
        all_predictions = np.array(all_predictions)
        final_predictions = []
        
        for i in range(X.shape[0]):
            votes = all_predictions[:, i]
            majority_vote = Counter(votes).most_common(1)[0][0]
            final_predictions.append(majority_vote)
        
        return np.array(final_predictions)
    
    def accuracy_score(self, y_true, y_pred):
        #Calculate accuracy score
        return np.mean(y_true == y_pred)

# Main execution time

df = pd.read_csv(r'C:\Users\leedl\OneDrive\Documents\AI_based_IDS\dataset\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')
#Prepare labels
if ' Label' in df.columns:
    df['binary_label'] = (df[' Label'] != 'BENIGN').astype(int)
    y = df['binary_label'].values
    print(f"Labels: BENIGN(0): {(y == 0).sum()}, DDoS(1): {(y == 1).sum()}")
else:
    print("Label column not found!")
    exit()

#Prepare features
feature_columns = [col for col in df.columns if col not in [' Label', 'binary_label', 'Label']]
X = df[feature_columns].select_dtypes(include=[np.number]).values

# Handle missing/infinite values quickly
X = np.nan_to_num(X, nan=np.nanmean(X, axis=0))

print(f"Feature matrix shape: {X.shape}")

#Using smaller subset
SAMPLE_SIZE = 20000  # Start with smaller sample
if X.shape[0] > SAMPLE_SIZE:
    indices = np.random.choice(X.shape[0], SAMPLE_SIZE, replace=False)
    X = X[indices]
    y = y[indices]
    print(f"Using subset of {SAMPLE_SIZE} samples for faster training")

#Split data
np.random.seed(42)
indices = np.random.permutation(len(X))
train_size = int(0.8 * len(X))

train_indices = indices[:train_size]
test_indices = indices[train_size:]

X_train, X_test = X[train_indices], X[test_indices]
y_train, y_test = y[train_indices], y[test_indices]

print(f"Train set: {X_train.shape}, Test set: {X_test.shape}")

#Train Random Forest
rf = FastRandomForest(n_estimators=15, max_depth=4, min_samples_split=200)
rf.fit(X_train, y_train)

#Make predictions
y_pred = rf.predict(X_test)

#Calculate accuracy
accuracy = rf.accuracy_score(y_test, y_pred)
print(f"Random Forest Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# results
correct = (y_test == y_pred).sum()
total = len(y_test)
print(f"Correct: {correct}/{total}")

print("Random Forest completed!")