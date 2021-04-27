string_list = []
stack = []
def digit_to_word(digit):
    cases = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        0: 'Zero',
    }
    return cases.get(digit)

def int_to_string(ls):
    for i in ls:
        if i > 9:
            while i > 9:
                x = i % 10
                print('x',x)
                stack.append(digit_to_word(x))
                i = i // 10
                print('i',i)
            a = digit_to_word(i)
            while (len(stack)>0):
                a += stack.pop()
            string_list.append(a)
        else:
            string_list.append(digit_to_word(i))
    print(string_list)

def main():
    int_to_string([3, 25, 209])
#3 25 209
#10 300 5
if __name__ == "__main__":
    main()
