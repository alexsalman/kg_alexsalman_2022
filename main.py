# Candidate for Kargo 2021 Summer Software Engineer Intern: Alex Salman
# Graduate student at UCSC, email: aalsalma@ucsc.edu
# 4/26/2021
import sys
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
    for number in ls:
        if number > 9:
            while number > 9:
                # get the first digit from the right
                x = number % 10
                # stack to store the words of digits per list number
                stack.append(digit_to_word(x))
                # remove a digit from the right
                number = number // 10
            # store the first digit of the number in variable a
            a = digit_to_word(number)
            # iterate through the stake to empty it's content and make a string
            while (len(stack)>0):
                a += stack.pop()
            string_list.append(a)
        else:
            # case of one digit number
            string_list.append(digit_to_word(number))
    # print format as requested in the question
    print(*string_list, sep = ", ")

def main():
    # to read args from terminal at the same line of running the algorithm
    # ex: python main.py 3 25 209
    # remove the first arg, main.py
    sys.argv.pop(0)
    ls = list(map(int,sys.argv))
    int_to_string(ls)
#3 25 209
#10 300 5
if __name__ == "__main__":
    main()
