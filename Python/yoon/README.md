# AI-Python_Study
<h2>
3월 29, 30일 python 노마드
</h2>

<h3>
variable
</h3>
+ my_age: Sanke Case 
+ myAge: Camel Case 
+ 첫 시작 숫자, 특수문자 공백 X 

<h3>
variable data type
</h3>
+ 숫자 
+ "문자"
+ boolean: True/False, 0/1, off/on 

<h3>
function
</h3>
+ print() 
+ start with def + function 
~~~
def say_hello:
    print("hello how are you?")

    say_hello

-> Hello how are you?
~~~

+function()에서 <br>
()-> parameter: 문자열 X, variable 형식, function 안에서 쓸 수 있는 variable <br>
+우리가 직접 데이터를 function에 넣고 function은 이 데이터를 받아 사용함 <br>
+ parameter는 함수로 전달하는 데이터를 저장하기 위한 palceholder일 뿐임 <br>
~~~
def say_hello(user_name):
    print("Hello", username, "how are you?")

say_hello("nico")
say_hello("lynn")
say_hello("lewis")

-> Hello nico how are you?
   Hello lynn how are you?
   Hello lewis how are you?
~~~

<h3>
multi parameters
</h3>
~~~
def say_hello(user_name, user_age):
    print("Hello", user_name)
    print("you are", user_age, "years old")

say_hello("nico", 12)

-> Hello nico
   you are 12 years old
~~~