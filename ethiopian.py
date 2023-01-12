def hello():
    print('Good luck !!')

def ethiopian():
    a= int(input("input multi num1> "))
    b= int(input("input multi num2> "))
    sum = 0
    
    while(a!=1):
        a = a//2
        if a%2 == 1:
            sum += b*2
    print(sum)

if __name__ == '__main__':
    hello()
    ethiopian()
