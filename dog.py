print("왈왈! (만나서 반가워요!)")
현재이름 = "쿠키"

def 짖기():
    print("으르릉... 컹컹!")
    print("'" + 현재이름 + "'은(는) 짖어댔다.")
    
def 헐떡대기():
    print("헥헥헥...")
    print("'" + 현재이름 + "'은(는) 헐떡댔다.")
    

def 먹기(대상 = ""):
    if 대상 == "":
        대상 = input("'" + 현재이름 + "'에게 뭘 줄까? ")
    print("냠냠냠...")
    print("'" + 현재이름 + "'은(는) '" + 대상 + "'을(를) 맛있게 먹었다.")

def 인사():
    print("왈왈왈! (안녕! 저는 '" + 현재이름 + "'에요!)")
    

    
def 이름바꾸기(새이름=""):
    global 현재이름
    if 새이름 == "":
        새이름 = input("왈? (제 새 이름은 뭔가요?) ")
    현재이름 = 새이름
    print("컹컹, 왈왈! (이름을 지어줘서 고마워요!)")

def 크게짖기():
    print("왈왈왈! (원주율은 약 3.141592653589793238462643383279502884197169399375105820974944592307816406286입니다.)")
    print("'" + 현재이름 + "'은(는) 굉장히 똑똑한 것 같다.")