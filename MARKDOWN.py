### 마크다운 예제 만들기
import pandas as pd

df_lap = pd.read_csv('d:/data/laptops.csv', index_col=0)

grouped_df = df_lap.groupby(['os', 'ram', 'p/brand'])['price'].count().unstack(fill_value=0)
grouped_df['total'] = grouped_df.sum(axis=1)

grouped_df = grouped_df.reset_index().set_index(['os', 'ram'])
grouped_df.loc[('total', ''), :] = grouped_df.sum()

grouped_df['total'] = grouped_df.iloc[:, :-1].sum(axis=1)
grouped_df = grouped_df.round(1)

grouped_df