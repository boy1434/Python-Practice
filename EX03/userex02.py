
class User:
    username = ""
    password = ""

    # 생성자의 self는 객체 생성시 자동 주입된다.
    # __init__ 이 함수가 생성자 (언더바 2개)init(언더바 2개)
    def __init__(self, username, password="1234"):
        self.username = username
        self.password = password
        

u = User("ssar", "1234")        
u1 = User("cos")
print(u.username)

# 생성자가 있어야 가능( 클래스를 딕셔너리로 변환해줌 )
print(u.__dict__)