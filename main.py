def main():
    plist = []
    ##################################################
    # Comlete your code here
    ##################################################


    begin = int(input(f'First value greater than 1: '))

    end = int(input(f'Second value greater than 1: '))

    if begin <= 1 or end <= 1:
        print ()
    elif begin >= end:
        print()
    else:
        for num in range (begin, end + 1):
            if num > 1:
                prime = True
                for i in range(2, int(num**0.5)+1):
                    if num % i == 0:
                        prime = False
                if prime:
                    plist.append(num)
        print (' ', begin, ' ', end, ' ', plist)
    



    return plist


if __name__ == '__main__':
    main()
