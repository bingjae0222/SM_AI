def plus(a,b):
    result = a+b
    return result

def minus(a,b):
    result = a-b
    return result


if __name__ == '__main__':
    while True:
        cmd = input("명령을 입력하세요(p,m,q)")
        if cmd == "p":
            print("plus..")
            num1 = int(input("INPUT NUM1 : "))
            num2 = int(input("INPUT NUM2 : "))
            result = plus(num1,num2)
            print(f"plus 결과는 : {result}")

        elif cmd == "m":
            print("minus.")
            num1 = int(input("INPUT NUM1 : "))
            num2 = int(input("INPUT NUM2 : "))
            result = plus(num1,num2)
            print(f"minus 결과는 : {result}")
        elif cmd == "q":
            print("bye")
            break


