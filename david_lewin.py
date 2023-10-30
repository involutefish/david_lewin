import collections

# 音级字典
pitch_class = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}

# 函数结果
def auto_print(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({', '.join(map(str, args))}): {result}")
        return result
    return wrapper

@auto_print
# cartesian_product，笛卡尔乘积
def cartesian_product(X, Y):
    result = []
    for x in X:
        for y in Y:
            result.append((x, y))
    return result

@auto_print
# interval calculator 音程计算int(x, y)
def interval(x, y):
    if isinstance(x, str):
        x_num = pitch_class[x]
    else:
        x_num = x

    if isinstance(y, str):
        y_num = pitch_class[y]
    else:
        y_num = y

    i = y_num - x_num

    if i < 0:
        i = i + 12
    return i

@auto_print
# IFUNC音程函数
def IFUNC(X, Y, i):
    product = cartesian_product(X, Y)
    intervals = []
    for pair in product:
        intervals.append(interval(pair[0], pair[1]))
    count = intervals.count(i)
    return count

if __name__ == "__main__":
    # 创建包含所有音程的表格
    all_intervals = list(range(12))
    counter = collections.Counter()

    X = input("请输入第一个音级集合，用逗号分隔：").split(",")
    Y = input("请输入第二个音级集合，用逗号分隔：").split(",")
    i = int(input("请输入一个音程："))

    # 输入
    X = [int(x) if x.isdigit() else x for x in X]
    Y = [int(y) if y.isdigit() else y for y in Y]

    IFUNC_result = IFUNC(X, Y, i)

    cartesian_product_result = cartesian_product(X, Y)
    intervals = [interval(pair[0], pair[1]) for pair in cartesian_product_result]

    # 音程计数
    counter.update(intervals)

    print("所有的音程为：")
    print(all_intervals)
    print("所有的音程的计数为：")
    for interval in all_intervals:
        count = counter.get(interval, 0)
        print("%d: %d" % (interval, count))

