# *- coding: UTF-8 -*-

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class AESUtil(object):

    def __init__(self, key):
        strKey = key.encode('utf-8').lower()
        self.key = a2b_hex(strKey)
        self.mode = AES.MODE_ECB
        BS = AES.block_size
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        self.unPad = lambda s: s[0:-ord(s[-1])]

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。

    # 进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
    def encrypt(self, text):
        cipher = AES.new(self.key, self.mode)
        encrypted = cipher.encrypt(self.pad(text).encode())
        return b2a_hex(encrypted).upper()

    def decrypt(self, text):
        aes = AES.new(self.key, self.mode)
        try:
            decrypted = aes.decrypt(a2b_hex(text))
            results = self.unPad(decrypted.decode("utf-8"))
        except Exception as e:
            results = str(e)
        return results


if __name__ == '__main__':
    pc = AESUtil('XXXXXXXXXXXXXXXXXXXXXX')  # 初始化密钥
    encryptStr = "XXXXXXXXXXXXXXXXXXXXXX"   # 需要加密的报文
    e = pc.encrypt(encryptStr)  # 加密
    print(e)
    decryptStr = "XXXXXXXXXXXXXXXXXXXXXX"
    d = pc.decrypt(decryptStr)     # 需要解密的报文
    print(d)
