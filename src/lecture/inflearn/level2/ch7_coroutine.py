"""
co-routine 이란?
. co-routine 은 single-thread 기반이다.
. yield, send 키워드를 활용하여 양방향 통신을 하는 single-thread 기반의 기술이다.
. multi-thread 를 사용할 수 없는 상황에서도 single-thread 만으로 여러가지 작업을 병행할 수 있다.

co-routine 의 장점
. single-thread 이기 때문에 context-switch 관련한 overhead 를 줄일 수 있다.
. 공유 자원에 대한 경쟁이 발생하지 않으므로 관리가 용이하다.

co-routine 은 상태값을 갖는다. (from inspect import getgeneratorstate, getgeneratorstate(제너레이터))
. GEN_CREATED
. GEN_RUNNING
. GEN_SUSPENDED
. GEN_CLOSED

python ver 3.5 이상에서는 다음과 같이 키워드를 치환하여 사용할 수 있다.
. def -> async,
. yield -> await


"""
