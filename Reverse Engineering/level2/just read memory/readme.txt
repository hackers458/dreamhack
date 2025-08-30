해당 문제는 내가 입력한 값을 변조시켜서 플래그를 만드는것이 아닌 기존 값으로 만든다
우선 값은
67
b44
13093
201fe8
3635ddf
5b7ae6ec
a5f65b4b
이렇게 변화를 하며
총 8바이트를 갖고 한다 -> 앞의 부분은 지워버린다.
공식은
a= (num+5)*3-7으로 num은 0부터 시작하며
b = a<<3
num = a+b+1f
이며
인덱스는 0~63이며
인덱스에 저장되는 값 = num % 0x4a + 0x+30
으로 된다.





하지만 import gdb

gdb.execute("file ./main")

gdb.Breakpoint("*0x5555555552d3")
gdb.execute("r")

flag = ""

for i in range(64):
	eax = int(gdb.parse_and_eval("$eax"))
	gdb.execute(f"set $edx={hex(eax)}")
	flag += chr(eax)
	gdb.execute("c")

print(flag)

이런 자동화 코드도 있기에 나중에 파이썬 gdb를 공부해야 할 것 같다.
