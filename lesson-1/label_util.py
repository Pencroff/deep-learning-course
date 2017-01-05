from collections import Counter

map_dict = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', }


def get_char_by_lbl(lbl):
    result = map_dict[str(lbl)]
    return result


def count_labels(label_list):
    counter_dict = {}
    for label in label_list:
        lbl = get_char_by_lbl(label)
        if lbl not in counter_dict:
            counter_dict[lbl] = 0
        counter_dict[lbl] += 1
    return counter_dict

def get_subset(size, data_set_values, data_set_labels):
    cnt = Counter(data_set_labels)
    keys = cnt.keys()
    one_class_size = size / len(keys)
