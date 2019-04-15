from mtmc2010.src.compute_detour_factor_2010 import compute_detour_factor_2010
from mtmc2015.src.compute_detour_factor_2015 import compute_detour_factor_2015


def run_detourfactor():
    compute_detour_factor_2010()
    compute_detour_factor_2015()


if __name__ == '__main__':
    compute_detour_factor_2010()
