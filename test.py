from nonblocking_itertools import *

if __name__ == "__main__":
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sorted(list(product(*data))) == sorted(list(itertools.product(*data))), "Product failed"

    data = [1, 2, 3, 4, 5, 6]
    r = 3
    assert sorted(list(combinations(data, r))) == sorted(list(itertools.combinations(data, r))), "Combinations failed"

    data = [1, 2, 3, 4, 5, 6]
    r = 3
    assert sorted(list(combinations_with_replacement(data, r))) == sorted(list(itertools.combinations_with_replacement(data, r))), "Combinations with replacement failed"

    data = [1, 2, 3, 4, 5, 6]
    r = 3
    assert sorted(list(permutations(data, r))) == sorted(list(itertools.permutations(data, r))), "Permutations failed"

    data1 = [1, 2, 3, 4, 5, 6]
    data2 = [7, 8, 9, 10, 11, 12]
    assert sorted(list(chain(data1, data2))) == sorted(list(itertools.chain(data1, data2))), "Chain failed"

    import time
    time.sleep(1)