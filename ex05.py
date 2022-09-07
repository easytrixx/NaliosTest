import array as table

def ex05(array):
    if len(array)==0:
        return 0;
    return array[0]+ex05(array[1:len(array)])


def test_unit():
    a = table.array('d', [3, 4, 5, 4, 8])
    assert ex05(a)==24
    assert ex05(a)!=21


if __name__ == "__main__":
    a=table.array('d',[3,4,5,4,4])
    print(ex05(a))