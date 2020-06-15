# -*- coding: utf-8 -*-
"""
# Protocol
- 프로토콜 파싱, 핸들링을 담당하는 클래스
- 서버에 연결될 때 초기화되며, 연결이 끝나면 소멸

# Factory
- 환경 설정이 저장되는 클래스
- 기본 Factory 클래스는 Protocol 클래스 객체를 생성하여, 해당 객체의 factory 변수가 그 Factory 클래스를 가리키도록 한다.
- Protocol 클래스에 접근하고, 환경 설정을 할 수 있게 된다.
"""

import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 1234))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

        print('Received', data.decode())


if __name__ == "__main__":
    main()
