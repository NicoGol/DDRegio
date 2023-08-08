from src.SCT import SCT
import pandas as pd


def partitioning(k,dataset,attributes,sct_method='full_order_CL',W=5,cutoff=60):
    dist_matrix = generate_dist_matrix(dataset,attributes)
    cont_matrix = generate_cont_matrix(dataset)
    sct = SCT(dataset[attributes],contiguity_matrix=cont_matrix,distance_matrix=dist_matrix,method=sct_method)
    h_tot, regions, regions_h, proved_exact, edges_removed, partition_time = sct.partition(k,'mdd',W,cutoff)
    return Regionalization_result(h_tot, regions, regions_h, proved_exact, partition_time)

def generate_dist_matrix(df, cols, dist_deg=2):
    indexes = df.index
    dist_matrix = pd.DataFrame(0, index=indexes, columns=indexes)
    for i in range(len(indexes) - 1):
        index1 = indexes[i]
        for j in range(i + 1, len(indexes)):
            index2 = indexes[j]
            dist = 0
            for col in cols:
                dist += (df.loc[index1, col] - df.loc[index2, col]) ** dist_deg
            dist_matrix.loc[index1, index2] = dist
            dist_matrix.loc[index2, index1] = dist
    return dist_matrix


def generate_cont_matrix(df):
    contiguity_matrix = pd.DataFrame(0, index=df.index, columns=df.index)
    for index, row in df.iterrows():
        for n in row.neighbors:
            contiguity_matrix.loc[index, n] = 1
    return contiguity_matrix


class Regionalization_result:
    def __init__(self, h_tot, regions, regions_h, proved_exact, partition_time):
        self.global_heterogeneity = h_tot
        self.regions = regions
        self.regions_heterogeneity = regions_h
        self.exact_solution = proved_exact
        self.partition_time = partition_time

def regions_to_gdp(self, k, colors):
    if k in self.regions:
        self.df['colors'] = None
        for i, r in enumerate(self.regions[k]):
            for v in r:
                self.df.loc[v, 'colors'] = colors[i]
        return self.df
    else:
        return None

if __name__ == '__main__':
    zones = pd.read_pickle('./example/ecodemo_NUTS1.pkl')
    attributes = ['density', 'gdp_inhabitant', 'median_age', 'rate_migration']
    result = partitioning(5, zones, attributes)
    print(result.global_heterogeneity)
    print(result.regions)

