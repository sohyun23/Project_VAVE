import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from importlib import reload
import convert_data_transform_to_pca_vector as pca
import tsne as ts
import visualization as vi
import raw_to_fourier as fr
import data_window_size as cut

import argparse
parser = argparse.ArgumentParser(
    description='raw data를 입력시 푸리에변환을 거친 PCA와 t-sne 결과를 보여주는 모듈')
parser.add_argument('raw_data_path', help='raw data path(.csv)')


args = parser.parse_args()
data = pd.read_csv(args.raw_data_path)
df = data.dropna()
