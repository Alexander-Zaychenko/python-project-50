import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Package which comparison to files')
    parser.add_argument('first_file', type=int, help='first name of file to comparison')
    parser.add_argument('second_file', type=int, help='second name of file to comparison')
    parser.add_argument('-f', '--format', metavar='FORMAT', default='!CHANGE THIS!', choices=['!CHANGE THIS!'], help='set format of output')
    return parser.parse_args()


only_first = "only_first"
only_second = 'only_second'
same_values = "same_values"
diff_values = "diff_values"


# def get_data(path1: str, path2: str) -> tuple:
#     dict_1 = open_file(path1)
#     dict_2 = open_file(path2)
#     return (dict_1, dict_2)
get_data = lambda x: json.loads(x)


def open_file(path: str) -> dict:
    with open(file=path, mode="r", encoding="utf8") as file:
        return json.load(file)


def make_format(data:dict) -> str:
    formated_data = 'abigus'

    return formated_data


def make_compare(data1:dict, data2:dict) -> dict:
    difference = {}
    keys1 = data1.keys()
    keys2 = data2.keys()
    all_keys = tuple(set(keys1) | set(keys2))
    # только ключи которые есть в первом словаре
    # только во втором
    # в обоих, значения разные
    # в обоих, значения одинаковые
    for key in all_keys:
        if key not in keys2:
            difference[key] = {'status': only_first, 'value': keys1[key]}
        elif key not in keys1:
            difference[key] = {'status': only_second, 'value': keys2[key]}
        elif data1[key] == data2[key]:
            difference[key] = {'status': same_values, 'value': keys1[key]}
        else:
            difference[key] = {'status': diff_values, 'value': [keys1[key], keys2[key]]}
    return difference



def gendiff(file_1:str, file_2:str) -> str:

    get_data(file_1)
    get_data(file_2)
    make_compare()
    return result


def test_gendiff() -> None:
    assert gendiff(fixture_1, fixture_2) == expected_result
