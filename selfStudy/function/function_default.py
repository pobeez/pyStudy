#default 인자 값
#default 인자 값은 인자의 오른쪽부터 값을 설정 할 수 있다.

def say(added, message="hi", times=1):
    print(added, message * times)

say("from hell:")
say("world ")
say("from hell:", "Hello ", 4)