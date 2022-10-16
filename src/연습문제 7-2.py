#연습문제 7-2

def main():
    input_num = input("숫자를 입력하시오:")
    
    if input_num.isdigit():
        print(eval(input_num)**2)
    else:
        print("정수가 아닙니다.")

main()
