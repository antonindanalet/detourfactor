from utils_mtmc.get_mtmc_files import *
from pathlib import Path


def compute_detour_factor_2015():
    year = 2015
    selected_columns = ['pseudo', 'rdist', 'ldist', 'f51300', 'WP']
    df_etappen = get_etappen(year, selected_columns=selected_columns)
    # Removing pseudo trip legs
    df_etappen = df_etappen[df_etappen['pseudo'] == 1]
    del df_etappen['pseudo']
    # Rename columns
    df_etappen = df_etappen.rename(columns={'rdist': 'routed_distance_in_km'})
    df_etappen = df_etappen.rename(columns={'ldist': 'crowflies_distance_in_km'})
    df_etappen = df_etappen.rename(columns={'f51300': 'transport_mode'})
    # Aggregate transport modes into 4 categories
    dict_detailed_mode2main_mode_2015 = {1: 'Walking',  # Zu Fuss
                                         2: 'Cycling',  # Velo -> LV
                                         3: 'Cars and motorbikes',  # Mofa, Motorfahrrad
                                         4: 'Cars and motorbikes',  # Kleinmotorrad
                                         5: 'Cars and motorbikes',  # Motorrad als Fahrer
                                         6: 'Cars and motorbikes',  # Motorrad als Mitfahrer
                                         7: 'Cars and motorbikes',  # Auto als Fahrer
                                         8: 'Cars and motorbikes',  # Auto als Mitfahrer
                                         9: 'Public transport',  # Bahn/Zug
                                         10: 'Public transport',  # Postauto
                                         11: 'Public transport',  # Bus/Schulbus
                                         12: 'Public transport',  # Tram/Metro
                                         13: 'Other',  # Taxi
                                         14: 'Other',  # Reisecar
                                         15: 'Other',  # Lastwagen
                                         16: 'Other',  # Schiff, Boot
                                         17: 'Other',  # Flugzeug / Luftfahrzeug
                                         18: 'Other',  # Zahnradbahn, Standseilbahn, Seilbahn, Sessellift, Skilift
                                         19: 'Other',  # Fahrzeugaehnliche Geraete
                                         20: 'Other',  # E-Bikes (langsam)
                                         21: 'Other',  # E-Bikes (schnell)
                                         -99: 'Other'}  # Pseudoetappe
    df_etappen['main_transport_mode'] = df_etappen['transport_mode'].map(dict_detailed_mode2main_mode_2015)
    del df_etappen['transport_mode']
    # Remove legs where no crow flies distance is available (i.e., quality of start of end point are not good enough)
    df_etappen = df_etappen[df_etappen['crowflies_distance_in_km'] > 0.5]
    # Remove trip legs without routing
    # Remove legs with distance smaller than 500 meters (according to routing)
    df_etappen = df_etappen[df_etappen['routed_distance_in_km'] >= 0.5]
    # Compute the ratio
    df_etappen['Detour factor'] = df_etappen['routed_distance_in_km'] / df_etappen['crowflies_distance_in_km']
    print('Global correction factor (weighted average):', np.average(df_etappen['Detour factor'], weights=df_etappen['WP']))
    df_etappen_car_only = df_etappen[df_etappen['main_transport_mode'] == 'Cars and motorbikes']
    print('Correction factor for cars and motorbikes (weighted average):',
          np.average(df_etappen_car_only['Detour factor'], weights=df_etappen_car_only['WP']))
    df_etappen_PT_only = df_etappen[df_etappen['main_transport_mode'] == 'Public transport']
    print('Correction factor for public transport (weighted average):',
          np.average(df_etappen_PT_only['Detour factor'], weights=df_etappen_PT_only['WP']))
    df_etappen_biking_only = df_etappen[df_etappen['main_transport_mode'] == 'Cycling']
    print('Correction factor for biking (weighted average):',
          np.average(df_etappen_biking_only['Detour factor'], weights=df_etappen_biking_only['WP']))
    df_etappen_walking_only = df_etappen[df_etappen['main_transport_mode'] == 'Walking']
    print('Correction factor for walking (weighted average):',
          np.average(df_etappen_walking_only['Detour factor'], weights=df_etappen_walking_only['WP']))
    bins = [0, 5, 10, 25, 50, 75, 100, np.inf]
    names = ['Between 0.5 and 5 km',
             'Between 5 and 10 km',
             'Between 10 and 25 km',
             'Between 25 and 50 km',
             'Between 50 and 75 km',
             'Between 75 and 100 km',
             'More than 100 km']
    df_etappen['distance_categories'] = pd.cut(df_etappen['routed_distance_in_km'], bins, labels=names)
    grouped_df_by_mode_and_distance_category = df_etappen.groupby(['main_transport_mode', 'distance_categories'])
    folder_for_results = Path('mtmc' + str(year) + '/data/results/')
    ''' Results: weighted average '''
    weigthed_average_by_group = grouped_df_by_mode_and_distance_category.apply(
        lambda x: (x['Detour factor'] * x['WP']).sum() / x['WP'].sum())
    print('Correction factor by transport mode and distance categories (weighted average):', weigthed_average_by_group)
    weigthed_average_by_group.to_csv(folder_for_results / 'detour_factor_weighted_avg.csv', header='Detour factor')
    ''' Results: median '''
    median_by_group = grouped_df_by_mode_and_distance_category['Detour factor'].median()
    print('Correction factor by transport mode and distance categories (median):', median_by_group)
    median_by_group.to_csv(folder_for_results / 'detour_factor_median.csv', header='Detour factor')
    ''' Results: 10th percentile '''
    percentile_by_group = grouped_df_by_mode_and_distance_category['Detour factor'].quantile(q=0.9)
    print('Correction factor by transport mode and distance categories (10th percentile):', percentile_by_group)
    percentile_by_group.to_csv(folder_for_results / 'detour_factor_10thpercentile.csv', header='Detour factor')


if __name__ == '__main__':
    compute_detour_factor_2015()
