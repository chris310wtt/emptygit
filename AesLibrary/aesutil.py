# *- coding: UTF-8 -*-

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class AESUtil(object):

    # def __init__(self):
        # key = '52fe1fa986cdb7dfc85799a456ad45af'
        # self.key =
        # strKey = key.encode('utf-8').lower()
        # # a2b_hex(strKey)
        # self.key = a2b_hex(strKey)
        # self.mode = AES.MODE_ECB
        # BS = AES.block_size
        # self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。

    # 进行加密算法，模式ECB模式，把叠加完16位的秘钥传进来
    def encrypt(self, text,key):
        # key = '52fe1fa986cdb7dfc85799a456ad45af'
        # self.key =
        strKey = key.encode('utf-8').lower()
        # a2b_hex(strKey)
        self.key = a2b_hex(strKey)
        self.mode = AES.MODE_ECB
        BS = AES.block_size
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        cipher = AES.new(self.key,self.mode)
        encrypted = cipher.encrypt(self.pad(text).encode())
        return b2a_hex(encrypted).upper()


    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text,key):
        # key = '52fe1fa986cdb7dfc85799a456ad45af'
        # self.key =
        strKey = key.encode('utf-8').lower()
        # a2b_hex(strKey)
        self.key = a2b_hex(strKey)
        self.mode = AES.MODE_ECB
        BS = AES.block_size
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        cryptor = AES.new(self.key, self.mode)
        plain_text = cryptor.decrypt(a2b_hex(text))
        response = bytes.decode(plain_text).strip('\0')
        return response.strip('')


# if __name__ == '__main__':
#     pc = AESUtil()  # 初始化密钥
#     keyStr = '52fe1fa986cdb7dfc85799a456ad45af'
#     encryptStr = "{\"busiParams\": {\"serviceNum\": \"010010327881\",\"endTime\": \"2017-08-03\",\"startTime\": \"2017-04-07\"},\"pubInfo\": {\"interfaceId\": \"\",\"transactionId\": \"WEB20170707105545257737\",\"interfaceType\": \"52\",\"opId\": \"9080\",\"countyCode\": \"\",\"orgId\": \"1010001\",\"clientIP\": \"\",\"transactionTime\": \"\",\"regionCode\": \"\"}}"
#     e = pc.encrypt(encryptStr,keyStr)  # 加密
#     print(e)
#     d = pc.decrypt(e)  # 解密
#     print("解密:", d)
