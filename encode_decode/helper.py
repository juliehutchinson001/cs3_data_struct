


#division structure: x / y = a leftover z:
#    x = dividend
#    y = divisor
#    a = quotient
#    z = coefficient
def dec_to_binary(dec_num):
    #ending binary number
    binary_num = ''
    #my division ends when my dec_num is == 0
    while dec_num // 2 != 0:
        #my coefficient (aka binary_num) is found by doing dec_num % 2
        binary_num += str(dec_num % 2)
        #dec_num becomes my new quotient that is now going to be divided by 2
        dec_num = dec_num // 2
    
    final_binary_num = str(dec_num) + binary_num
    return final_binary_num


def main():
    print(dec_to_binary(93))

if __name__ == "__main__":
    main()