# AI-Python_Study
3월 29, 30일 python 노마드

*variable*
    my_age: Sanke Case
    myAge: Camel Case
    첫 시작 숫자, 특수문자 공백 X

*variable data type*
    숫자
    "문자"
    boolean: True/False, 0/1, off/on

*function*
    print()
    start with def + function
    (ex)
    <pre>
    <code>
    {
        def say_hello:
            print("hello how are you?")

        say_hello

    -> Hello how are you?
    }
    </code>
    </pre>

    function()에서
    ()-> parameter: 문자열 X, variable 형식, function 안에서 쓸 수 있는 variable
    우리가 직접 데이터를 function에 넣고 function은 이 데이터를 받아 사용
    parameter는 함수로 전달하는 데이터를 저장하기 위한 palceholder일 뿐

    (ex)
    <pre>
    <code>
    {
        def say_hello(user_name):
            print("Hello", username, "how are you?")

        say_hello("nico")
        say_hello("lynn")
        say_hello("lewis")

    ->  Hello nico how are you?
        Hello lynn how are you?
        Hello lewis how are you?
    }
    </code>
    </pre>

*multi parameters*
    (ex)
    <pre>
    <code>
    {
        def say_hello(user_name, user_age):
            print("Hello", user_name)
            print("you are", user_age, "years old")

        say_hello("nico", 12)

    -> Hello nico
       you are 12 years old
    }
    </code>
    </pre>
