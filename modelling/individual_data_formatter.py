import pandas as pd
import copy


def to_number(value):
    if not isinstance(value, (int, float)):
        return None
    return float(value)


def generate_formatted_children_under_five():
    individual_recode = pd.read_csv('../data/generate/individual_house_hold_recode.csv')
    # Deleting columns in which the age of the household member was not recorded
    individual_recode.dropna(subset=['HV105$01 Age of household members'], inplace=True)
    children_under_5 = copy.deepcopy(individual_recode)
    # Convert the column to numeric, treating non-convertible values as NaN
    children_under_5['HV105$01 Age of household members'] = pd.to_numeric(
        children_under_5['HV105$01 Age of household members'], errors='coerce')
    # getting children age under 5
    children_under_5 = children_under_5[children_under_5['HV105$01 Age of household members'].apply(to_number) <= 59]
    children_under_5.dropna(subset=['HML32$01 Final result of malaria from blood smear test'], inplace=True)
    children_under_5.drop('row_key', axis=1, inplace=True)
    _cols_num_str = ['HV220    Age of head of household','HV238    Number of households sharing toilet','HV245    Hectares of agricultural land (1 decimal)', 'HV246A   Owns cattle', 'HV246B   Owns cows bulls', 'HV246C   Owns horses donkeys mules','HV246D   Owns goats','HV246E   Owns sheep', 'HV246F   Owns chickenspoultry', 'HV246G   Owns pigs', 'HV246H   Owns camels']
    for col in _cols_num_str:
        children_under_5[col] = children_under_5[col].apply(to_number)
    return children_under_5
