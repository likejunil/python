"""
Contextlib 란 자원(resource)를 안정적으로 할당하고 반환하기 위해서 사용하는 방식이다.
with .. as .. 구문으로 사용한다.

1. 사용하는 방식은 크게 클래스 구현과
    __enter__ 와 __exit__ 구현
2. 함수 작성이 있다.
    @contextlib.contextmanager 데코레이터와 yield 사용
"""

