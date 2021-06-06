def prime(num):
    if num > 1:
    # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"Составное число")
                break
        else:
            print(num,"Простое число")
    else:
        print(num,"Составное число")

prime(int(input()))