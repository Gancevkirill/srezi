#1
def de_none(lst):
    return [x for x in lst if x is not None]
#2
def list_insert(ref_list, start, num, rep):
    return ref_list[:start] + [num] * rep + ref_list[start:] if len(ref_list) >= start else -1
#3
def get_elem(d, k):
    if k in d:
        return d[k]
    else:
        return None