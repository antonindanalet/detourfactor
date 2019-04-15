# Detour factors from the Mobility and Transport Microcensus 2010 and 2015
This code computes the detour factor for public transport and cars and motorbikes, by distance categories. To know more about the detour factor, check e.g.:

Chalasani, V. Saikumar, O. Engebretsen, et K. W. Axhausen. <a href="https://www.bts.gov/archive/publications/journal_of_transportation_and_statistics/volume_08_number_02/paper_01/index">Precision of Geocoded Locations and Network Distance Estimates</a>. Journal of Transportation and Statistics 8, nᵒ 2 (2005): 15.

This code uses data from the Mobility and Transport Microcensus (<a href="www.are.admin.ch/mtmc">MTMC</a>) 2010 and 2015. The results are available as CSV-files.

## Results 

### Results 2010

Global correction factor (weighted average): 1.51

Correction factor for cars and motorbikes (weighted average): 1.54

Correction factor for public transport (weighted average): 1.34

Correction factor by transport mode and distance categories (average, weighted average, median & 20th percentile), see CSV-files:
- <a href="https://github.com/antonindanalet/detourfactor/blob/master/mtmc2010/data/results/detour_factor_weighted_avg.csv">detour_factor_weighted_avg.csv</a>
- <a href="https://github.com/antonindanalet/detourfactor/blob/master/mtmc2010/data/results/detour_factor_median.csv">detour_factor_median.csv</a>
- <a href="https://github.com/antonindanalet/detourfactor/blob/master/mtmc2010/data/results/detour_factor_20thpercentile.csv">detour_factor_20thpercentile.csv</a>

### Results 2015

Global correction factor (weighted average): 1.45

Correction factor for cars and motorbikes (weighted average): 1.47

Correction factor for public transport (weighted average): 1.33

Correction factor by transport mode and distance categories (average, weighted average, median & 20th percentile), see CSV-files:
- <a href="https://github.com/antonindanalet/detourfactor/blob/master/mtmc2015/data/results/detour_factor_weighted_avg.csv">detour_factor_weighted_avg.csv</a>
- <a href="https://github.com/antonindanalet/detourfactor/blob/master/mtmc2015/data/results/detour_factor_median.csv">detour_factor_median.csv</a>
- <a href="https://github.com/antonindanalet/detourfactor/blob/master/mtmc2015/data/results/detour_factor_20thpercentile.csv">detour_factor_20thpercentile.csv</a>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for reproducing the result and understanding how it has been generated.

### Prerequisites

To run the code itself, you need python 3, pandas and numpy.

For it to produce the results, you also need the raw data of the Transport and Mobility Microcensus 2010 and 2015, not included on GitHub. These data are individual data and therefore not open. You can however get them by asking the Swiss Federal Statistical Office (FSO), after signing a data protection contract. Please ask mobilita2015@bfs.admin.ch, phone number 058 463 64 68. The cost of the data is available in the document "<a href="https://www.are.admin.ch/are/de/home/medien-und-publikationen/publikationen/grundlagen/mikrozensus-mobilitat-und-verkehr-2015-mogliche-zusatzauswertung.html">Mikrozensus Mobilität und Verkehr 2015: Mögliche Zusatzauswertungen</a>"/"<a href="https://www.are.admin.ch/are/fr/home/media-et-publications/publications/bases/mikrozensus-mobilitat-und-verkehr-2015-mogliche-zusatzauswertung.html">Microrecensement mobilité et transports 2015: Analyses supplémentaires possibles</a>".

### Run the code

Please copy the files <em>etappen.csv</em> from 2010 and <em>etappen.csv</em> from 2015 that you receive from FSO in the folders "mtmc2010/data/source" and "mtmc2015/data/source" respectively. Then run <em>run_detourfactor.py</em>. 

DO NOT commit or share in any way these two CSV-files! These are personal data.

## Contact

Please don't hesitate to contact me if you have questions or comments about this code: antonin.danalet@are.admin.ch
