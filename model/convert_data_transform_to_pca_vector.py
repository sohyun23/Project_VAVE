from sklearn.decomposition import PCA
import numpy as np
import pandas as pd


def pca(data, components=2):
    pca = PCA(n_components=components)  # 주성분을 몇개로 할지 결정
    principalComponents = pca.fit_transform(data)
    principalDf = pd.DataFrame(data=principalComponents, columns=[
                               "component" + str(i+1) for i in range(components)])

    return principalDf
