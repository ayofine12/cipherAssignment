import socket
from Crypto.Random import get_random_bytes
import rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import hmac
import hashlib

class Client:
    def __init__(self, nickname, host = '127.0.0.1', port = 3030, position = 'initiater'):
        self.nickname = nickname
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.position = position
        self.aes_encoder = None
        self.aes_decoder = None
        self.mac_key = None

    def setting(self):
        count = 0
        while count < 2:
            message = self.client.recv(1024).decode('utf-8')
            if message == 'NICK':
                s = self.nickname + ',' + 'c1'
                self.client.send(s.encode('utf-8'))
            else:
                print(message)
                print()
            count+=1

    def receive_nicks(self):
        count = 0
        while count < 2:
            nick = self.client.recv(1024).decode('utf-8')
            if nick != self.nickname:
                print("nickname of oppoent is: ", nick)
                self.opponent = nick
            count +=1 

    # client2에 암호화된 aes_key, iv, mac_key를 보내는 함수이다.
    def send_encrypted_con(self):
        # client2의 공개키를 불러온 다음 pubkey2 변수에 담아준다
        with open('pubkey2.pem', 'rb') as f:
            pubkey2 = rsa.PublicKey.load_pkcs1(f.read())
        
        # 위 코드 수정하지 마세요
        '''----------------------------------------------------------------------------------'''

        # Step1: aes_key, iv, mac_key를 만들어준다
        # aes_key: 16 bytes
        # iv: 16 bytes
        # mac_key: 32 bytes

        # Step2: Step1에서 구한 값을 토대로 aes 인코더와 디코더를 각각 만든다
        # 그리고 클래스의 전역 변수인 self.aes_encoder, self.aes_decoder, self.mac_key에 
        # 각각 aes 인코더, aes 디코더, mac_key를 넣어준다

        # Step3: 위에서 만든 aes_key, iv, mac_key를 합친 다음
        # client2의 공개키로 rsa 암호화한다
        # 암호화된 값을 encrypted_con 변수에 넣어준다(변수 이름 중요)

        '''----------------------------------------------------------------------------------'''
        # 아래 코드 수정하지 마세요

        # encrypted_con 변수에 담긴 값을 client2에 보내준다
        self.client.send(encrypted_con)

    # 평문을 암호화하여 client2에 보내는 함수이다.
    def send_message(self):
        plaintext = input("you: ")
        print()
        padded_plaintext = pad(plaintext.encode(), AES.block_size)

        # 위 코드 수정하지 마세요
        '''----------------------------------------------------------------------------------'''

        # Step1: self.aes_encoder를 사용하여 입력한 평문을 암호화한다.
        # 암호화된 문장을 ciphertext 변수에 넣어준다. (변수 이름 중요)

        # Step2: self.mac_key와 ciphertext를 이용하여 mac값을 만들어준다
        # 만들어진 mac 값을 sender_mac 변수에 넣어준다. (변수 이름 중요)

        '''----------------------------------------------------------------------------------'''
        # 아래 코드 수정하지 마세요

        t = sender_mac.hexdigest()
        t_bytes = bytes.fromhex(t)
        self.client.send(t_bytes+ciphertext)

    # client2로부터 mac값과 암호문을 받아 평문으로 복호화하는 함수이다.
    def recv_message(self):
        # client2로부터 받은 값을 mac값(t_)와 암호문(ciphertext)으로 분리한다.
        mac_cipher = self.client.recv(1024)
        t_bytes = mac_cipher[:32]
        t_ = t_bytes.hex()
        ciphertext = mac_cipher[32:]

         # 위 코드 수정하지 마세요
        '''----------------------------------------------------------------------------------'''

        # Step1: self.mac_key와 ciphertext를 이용하여 mac값을 만들어준다
        # 만들어진 mac 값을 receiver_mac 변수에 넣어준다. (변수 이름 중요)

        '''----------------------------------------------------------------------------------'''
        # 아래 코드 수정하지 마세요

        t = receiver_mac.hexdigest()

        if t != t_:
            print("something went wrong")
        else:
            # 위 코드 수정하지 마세요
            '''----------------------------------------------------------------------------------'''

            # Step2: self.aes_decoder를 사용하여 암호문을 복호화한다.
            # 복호화된 문장을 data 변수에 넣어준다. (변수 이름 중요)
            
            '''----------------------------------------------------------------------------------'''
            # 아래 코드 수정하지 마세요
            print("friend:", data)
            print()

    def run(self):
        count = 0
        while count < 5:
            self.send_message()
            self.recv_message()
            count += 1

if __name__ == "__main__":
    client1 = Client(nickname=input("Choose your nickname: "))
    client1.setting()

    client1.receive_nicks()

    client1.position = client1.client.recv(1024).decode('utf-8')

    print('your position is: ', client1.position)

    client1.send_encrypted_con()

    client1.run()

    client1.client.close()




