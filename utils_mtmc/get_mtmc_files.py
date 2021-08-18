import pandas as pd
import numpy as np
from pathlib import Path


folder_path_2005 = ''
folder_path_2010 = Path('mtmc2010/data/source/')
folder_path_2015 = Path('mtmc2015/data/source/')


def get_zp(year, selected_columns=None):
    if year == 2010:
        with open(folder_path_2010 + 'zielpersonen.csv', 'r') as zielpersonen_file:
            if selected_columns is None:
                df_zp = pd.read_csv(zielpersonen_file,
                                    delimiter=';',
                                    dtype={'HHNR': int,
                                           'ZIELPNR': int,
                                           'WP': np.longdouble,
                                           'gesl': int,
                                           'nation': int})
            else:
                df_zp = pd.read_csv(zielpersonen_file,
                                    delimiter=';',
                                    dtype={'HHNR': int,
                                           'ZIELPNR': int,
                                           'WP': np.longdouble,
                                           'gesl': int,
                                           'nation': int},
                                    usecols=selected_columns)
    elif year == 2015:
        with open(folder_path_2015 + 'zielpersonen.csv', 'r') as zielpersonen_file:
            if selected_columns is None:
                df_zp = pd.read_csv(zielpersonen_file)
            else:
                df_zp = pd.read_csv(zielpersonen_file,
                                    dtype={'HHNR': int},
                                    usecols=selected_columns)
    elif year == 2005:
        with open(folder_path_2005 + 'zielpersonen.dat', 'r') as zielpersonen_file:
            if selected_columns is None:
                df_zp = pd.read_csv(zielpersonen_file,
                                    sep='\t')
            else:
                df_zp = pd.read_csv(zielpersonen_file,
                                    dtype={'HHNR': int},
                                    usecols=selected_columns,
                                    sep='\t')
    return df_zp


def get_hh(year, selected_columns=None):
    if year == 2015:
        with open(folder_path_2015 + 'haushalte.csv', 'r') as haushalte_file:
            df_hh = pd.read_csv(haushalte_file,
                                dtype={'HHNR': int},
                                usecols=selected_columns)
    elif year == 2010:
        with open(folder_path_2010 + 'haushalte.csv', 'r') as haushalte_file:
            df_hh = pd.read_csv(haushalte_file,
                                sep=';',
                                dtype={'HHNR': int},
                                usecols=selected_columns)
    elif year == 2005:
        with open(folder_path_2005 + 'Haushalte.dat', 'r') as haushalte_file:
            df_hh = pd.read_csv(haushalte_file,
                                sep='\t',
                                dtype={'HHNR': int},
                                usecols=selected_columns)
    return df_hh


def get_etappen(year, selected_columns=None):
    if year == 2015:
        with open(folder_path_2015 / 'etappen.csv', 'r', encoding='iso-8859-1') as etappen_file:
            df_etappen = pd.read_csv(etappen_file,
                                     dtype={'HHNR': int,
                                            'W_AGGLO_GROESSE2012': int},
                                     usecols=selected_columns)
    elif year == 2010:
        with open(folder_path_2010 / 'etappen.csv', 'r', encoding='latin1') as etappen_file:
            df_etappen = pd.read_csv(etappen_file,
                                     sep=';',
                                     dtype={'HHNR': int},
                                     usecols=selected_columns)
    elif year == 2005:
        with open(folder_path_2005 + 'etappen.dat', 'r') as etappen_file:
            df_etappen = pd.read_csv(etappen_file,
                                     sep='\t',
                                     na_values=' ',
                                     dtype={'HHNR': int,
                                            'ZIELPNR': int,
                                            'E_AUSLAND': int,
                                            'PSEUDO': int,
                                            'F510': int,
                                            'rdist': float},
                                     usecols=selected_columns)
    return df_etappen


def get_hhp(year, selected_columns=None):
    if year == 2010:
        with open(folder_path_2010 + 'haushaltspersonen.csv', 'r') as haushaltspersonen_file:
            df_hhp = pd.read_csv(haushaltspersonen_file,
                                 delimiter=';',
                                 usecols=selected_columns,
                                 na_values=[-99])
    elif year == 2015:
        with open(folder_path_2015 + 'haushaltspersonen.csv', 'r') as haushaltspersonen_file:
            df_hhp = pd.read_csv(haushaltspersonen_file,
                                 delimiter=',',
                                 usecols=selected_columns,
                                 na_values=[-99])
    else:
        raise Exception('Year not well defined')
    return df_hhp

