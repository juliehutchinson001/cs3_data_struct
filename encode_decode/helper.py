


#division structure: x / y = a leftover z:
#    x = dividend
#    y = divisor
#    a = quotient
#    z = coefficient

#conversion from 10 base to binary
def dec_to_binary(dec_num):
    #ending binary number
    binary_num = ''
    #my division ends when my dec_num is == 0
    while dec_num // 2 != 0:
        #my coefficient (aka binary_num) is found by doing dec_num % 2
        binary_num += str(dec_num % 2)
        #dec_num becomes my new quotient that is now going to be divided by 2
        dec_num = dec_num // 2
    #my final result is the last dec_num gotten from the loop + concatenation of the
    #other coefficients from binary_num:
    final_binary_num = binary_num + str(dec_num)
    return int(final_binary_num)

    #conversion from 10-base to any base (numerical)
def n_base_to_change(decimal_num, base):
    #ending base number converted
    conversion = ''
    # my division ends when the dividend is 0
    while decimal_num // base != 0:
        #concatenate the coefficient, which is calculated by applying mod to my
        #decimal number with my base as divisor
        conversion += str(decimal_num % base)
        #divide decimal_num in base to get quotient
        decimal_num = decimal_num // base

    #concatenate last coefficient to already gotten coefficients to return result in new base
    final_base_num = conversion + str(decimal_num)
    return int(final_base_num)

    #conversion from 10 base to hexadecimal


#decoding binary to decimal
def decimal_decode(bin_num):
    #decimal is my final number
    final_decimal = 0
    #counter
    ctr = 0

    #create a list with my binary numbers
    bin_nums_list = list(str(bin_num))
    print("---------------{}------------------".format(bin_nums_list))

    #iterating through each of the binary bits [1101110]
    for index_bit_num in bin_nums_list:
        #main operation where the binary is converted to decimal
        final_decimal += (int(index_bit_num)) * (2 ** ctr)
        ctr += 1
        print("----------------{}-----------------".format(index_bit_num))
        print("*****************{}****************".format(final_decimal))
        
    print("---------------{}------------------".format(final_decimal))

    return final_decimal



def main():
    decimal_number = int(input("What's the number to be changed?: "))
    base = int(input("What's the base to be changed to?: "))
    print(n_base_to_change(decimal_number, base))

    gimme_a_binary = dec_to_binary(decimal_number)
    print(gimme_a_binary)
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_" + str(decimal_decode(gimme_a_binary)) + "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

if __name__ == "__main__":
    main()