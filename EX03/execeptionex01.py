# 예외는 항상 런타임시에 일어난다.

try:
    print(2/0)
except Exception as e:
    print(e)
finally:
    print("끝")
