import pandas as pd
from sklearn.preprocessing import scale
from sklearn.preprocessing import LabelEncoder
from DataUnderstanding import DataUnderstanding


class DataPreparetion(DataUnderstanding):
    def removendo_nulos(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return dataframe.dropna()

    def removing_outliers_zscore(self, dataframe: pd.DataFrame, zscore: int=3):
        outlier_rows = dataframe.abs().gt(zscore).any(axis=1)
        amount_of_outliers = outlier_rows.sum()
        print(f'Amount of outliers: {amount_of_outliers}')
        return dataframe[~outlier_rows], outlier_rows

    def removendo_colunas(self, dataframe: pd.DataFrame, colunas=[]) -> pd.DataFrame:
        return dataframe.drop(colunas, axis=1)

    def renomeando_colunas(self, dataframe: pd.DataFrame, novo_nome_e_velho_nome: dict):
        return dataframe.rename(columns=novo_nome_e_velho_nome)

    def substituindo_valores(self, dataframe: pd.DataFrame, colunas, valores) -> pd.DataFrame:
        return dataframe[colunas].replace(valores)

    def convertendo_colunas(self, dataframe: pd.DataFrame, colunas: list, tipo: str) -> pd.DataFrame:
        return dataframe[colunas].astype(tipo)

    def dummy(self, dataframe: pd.DataFrame, colunas=[]):
        dataframe = pd.get_dummies(dataframe[colunas])
        colunas = dataframe.columns
        return dataframe, colunas

    def label_endcode(self, dataframe: pd.DataFrame):
        training = LabelEncoder().fit(dataframe)
        dataframe = training.transform(dataframe)
        return dataframe

    def normalizando_os_dados(self, dataframe: pd.DataFrame):
        return scale(dataframe)


if __name__ == '__main__':
    data_preparetion = DataPreparetion()
