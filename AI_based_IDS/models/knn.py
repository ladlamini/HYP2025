import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, accuracy_score
import sys

def main():
    try:
        print("Starting K-Means clustering...")
        
        # dataset used to train
        df = pd.read_csv(r'C:\Users\leedl\OneDrive\Documents\AI_based_IDS\dataset\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')

        # Data Preprocessing
        # print("Dataset shape:", df.shape)
        # print("Columns:", df.columns.tolist())

        if ' Label' in df.columns: 
            labels = df[' Label']
            print(f"Label values: {labels.unique()}")
            # Create binary labels for evaluation (0 = BENIGN, 1 = Attack)
            binary_labels = (labels != 'BENIGN').astype(int)
            print(f"Binary labels - BENIGN: {(binary_labels == 0).sum()}, Attacks: {(binary_labels == 1).sum()}")
        else:
            print("No Label column found")
            labels = None
            binary_labels = None

        # Drop non-numeric columns incl the Label column
        columns_to_drop = [' Label'] if ' Label' in df.columns else []
        numeric_df = df.drop(columns=columns_to_drop).select_dtypes(include=[np.number])

        print(f"Using {numeric_df.shape[1]} numeric features for clustering")

        # Handle infinite + large values + Replace infinite values with NaN
        numeric_df = numeric_df.replace([np.inf, -np.inf], np.nan)

        # Fill NaN values with column means
        numeric_df = numeric_df.fillna(numeric_df.mean())

        # Cap very large values
        for column in numeric_df.columns:
            q99 = numeric_df[column].quantile(0.999)
            if q99 > 1e6:  # If 99.9th percentile is very large
                numeric_df[column] = np.where(numeric_df[column] > q99, q99, numeric_df[column])

        # Standardize data
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(numeric_df)

        # Check for remaining issues
        print(f"Scaled data shape: {scaled_data.shape}")
        print(f"Scaled data range: [{scaled_data.min():.2f}, {scaled_data.max():.2f}]")

        # Apply K-Means with 2 clusters (normal vs bad)
        kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(scaled_data)

        # Add cluster labels to dataframe
        df['Cluster'] = clusters

        # Analyze clusters
        cluster_counts = df['Cluster'].value_counts()
        print("Cluster distribution:")
        print(cluster_counts)

        # Identify anomalies (small cluster is anomalous)
        if cluster_counts.iloc[0] < cluster_counts.iloc[1]:
            anomalous_cluster = cluster_counts.index[0]
        else:
            anomalous_cluster = cluster_counts.index[1]

        # print(f"Anomalous cluster identified: {anomalous_cluster}")
        # print(f"Number of potential anomalies: {cluster_counts[anomalous_cluster]}")
        # print(f"Number of normal instances: {cluster_counts[anomalous_cluster ^ 1]}") 

        # Calculate silhouette score for clustering quality
        # silhouette_avg = silhouette_score(scaled_data, clusters)
        # print(f"Silhouette Score: {silhouette_avg:.3f}")
        # print("(Values closer to 1 indicate better-defined clusters)")

        # Calculate accuracy if we have true labels
        if binary_labels is not None:
            # Map clusters to binary labels (cluster with more BENIGN is normal)
            benign_counts = []
            for cluster_id in [0, 1]:
                cluster_mask = (clusters == cluster_id)
                if cluster_mask.sum() > 0:
                    benign_ratio = (binary_labels[cluster_mask] == 0).mean()
                    benign_counts.append((cluster_id, benign_ratio))
            
            # Sort by benign ratio to identify which cluster is normal
            benign_counts.sort(key=lambda x: x[1], reverse=True)
            normal_cluster = benign_counts[0][0]
            
            # Create predictions
            predictions = (clusters != normal_cluster).astype(int)
            
            # Calculate accuracy
            accuracy = accuracy_score(binary_labels, predictions)
            print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
            
            # Additional metrics
            from sklearn.metrics import classification_report
            print("Classification Report:")
            print(classification_report(binary_labels, predictions, 
                                      target_names=['BENIGN', 'ATTACK']))

        # accuracy results
        df['Is_Anomaly'] = (df['Cluster'] == anomalous_cluster).astype(int)
        print(f"Anomaly detection completed! Found {df['Is_Anomaly'].sum()} potential anomalies.")

        # Stats
        # print("Basic statistics of anomalies vs normal:")
        # if 'Is_Anomaly' in df.columns and binary_labels is not None:
        #     anomaly_stats = df.groupby('Is_Anomaly').agg({
        #         col: 'mean' for col in numeric_df.columns[:5]  # First 5 numeric columns
        #     })
        #     print(anomaly_stats)
            
        return True
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
# Total connections
#total = 97718 + 128027  # = 225,745

# # Cluster 0 = Attacks, Cluster 1 = Normal
# predicted_normal = 193088
# predicted_attacks = 32657

# more actual attacks (128,027) than predicted attacks (32,657),
# most attacks were misclassified as normal

 # Calculate correct predictions
# correct_predictions = min(predicted_attacks, 128027) + min(predicted_normal, 97718)

# #Accuracy = correct predictions / total
# accuracy = correct_predictions / total
# print(f"Accuracy: {accuracy:.3f}")  # arounf 58/59%