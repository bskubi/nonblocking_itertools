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
    import itertools
    import nonblocking_itertools

    def laggy_generator(iterable):
        for i in iterable:
            time.sleep(1)
            yield i

    # print("Testing itertools.combinations")
    # start = time.time()
    # data = laggy_generator(range(4))
    # for combo in itertools.combinations(data, 2):
    #     print("Seconds from start:", int(time.time() - start), "Combination:", combo)

    # print("Testing nonblocking_itertools.combinations")
    # start = time.time()
    # data = laggy_generator(range(4))
    # for combo in nonblocking_itertools.combinations(data, 2):
    #     print("Seconds from start:", int(time.time() - start), "Combination:", combo)

    print("Testing itertools.chain")
    start = time.time()
    data1 = laggy_generator(range(2))
    data2 = laggy_generator(range(2, 4))
    for element in itertools.chain(data1, data2):
        print("Seconds from start:", int(time.time() - start), "Element:", element)

    print("Testing nonblocking_itertools.chain")
    start = time.time()
    data1 = laggy_generator(range(2))
    data2 = laggy_generator(range(2, 4))
    for element in nonblocking_itertools.chain(data1, data2):
        print("Seconds from start:", int(time.time() - start), "Element:", element)
