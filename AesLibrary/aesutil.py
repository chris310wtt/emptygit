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
        except Exception:
            results = 'fail'
        return results


# if __name__ == '__main__':
#     pc = AESUtil()  # 初始化密钥
#     keyStr = '52fe1fa986cdb7dfc85799a456ad45af'
#     encryptStr = "{\"busiParams\": {\"serviceNum\": \"010010327881\",\"endTime\": \"2017-08-03\",\"startTime\": \"2017-04-07\"},\"pubInfo\": {\"interfaceId\": \"\",\"transactionId\": \"WEB20170707105545257737\",\"interfaceType\": \"52\",\"opId\": \"9080\",\"countyCode\": \"\",\"orgId\": \"1010001\",\"clientIP\": \"\",\"transactionTime\": \"\",\"regionCode\": \"\"}}"
#     e = pc.encrypt(encryptStr, keyStr)  # 加密
#     print(e)
#     decryptStr = "768CA266D1642825EB882E69BC4402F12C7623A88063AC8ECE7987849FD1EC54ED87276D13B90BADE1FF3EBC99464B5B37029CA551DF0F8D53EB7D83966DFEF23F0016079C0249E424F4337DB57571821A30BD8403F41A6BA9FF9ABE1E0CE6706A11A534440ED85B6C99D68CA91BEFF9"
#     d = pc.decrypt(decryptStr, keyStr)
#     # print(isinstance(d, str)) #看下解密后编码格式
#     # print(type(d))
#     print(d)
