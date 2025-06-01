#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
回调加解密函数
如果需要使用此类，需要先安装pycryptodomex或者pycryptodome，版本 >=3.9.8
企业内部应用：https://open.welink.huaweicloud.com/docs/#/990hh0/whokyc/u80kqy
第三方企业应用：https://open.welink.huaweicloud.com/docs/#/qdmtm8/uug541/u80kqy
@author: wecode@huawei.com
"""
import hashlib
import base64
import json
import time

PYCRYPTODOMEX_INSTALLED = True
try:
    print("Try to import pycryptodomex")
    from Cryptodome.Cipher import AES
    from Cryptodome.Random import get_random_bytes
except ImportError:
    try:
        print("Can't find pycryptodomex, and try to import pycryptodome")
        from Crypto.Cipher import AES
        from Crypto.Random import get_random_bytes
    except ImportError:
        PYCRYPTODOMEX_INSTALLED = False


class CallBackV1(object):
    """回调加解密函数"""

    def __init__(self, key):
        if not PYCRYPTODOMEX_INSTALLED:
            raise ImportError(
                "if you want to use CallBackV1, please install pycryptodomex or pycryptodome >= 3.9.8"
            )
        self.algorithm = "AES"
        self.key_gcm_aes = "AES/GCM/NoPadding"
        self.aes_key_size = 128
        self.iv_base64_length = 24
        self.iv_length = 16
        self.tag_length = 16
        self.key = self.init_key(key)

    def encrypt(self, data):
        iv = get_random_bytes(self.iv_length)
        cipher = AES.new(self.key, mode=AES.MODE_GCM, nonce=iv)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode("utf-8"))
        return self.encodeToBase64(iv) + self.encodeToBase64(ciphertext + tag)

    def decrypt(self, ciphertext):
        if len(ciphertext) < self.iv_base64_length:
            raise Exception("invalid request body")
        iv = self.decodeFromBase64(ciphertext[: self.iv_base64_length])
        ciphertext = self.decodeFromBase64(ciphertext[self.iv_base64_length :])
        cipher = AES.new(self.key, mode=AES.MODE_GCM, nonce=iv)
        plaintext = cipher.decrypt_and_verify(
            ciphertext[: -self.tag_length], ciphertext[-self.tag_length :]
        )
        return str(plaintext, encoding="utf-8")

    def decrypt_request(self, request_body):
        """解析WeLink传来的回调body"""
        ciphertext = json.loads(request_body).get("encrypt")
        return json.loads(self.decrypt(ciphertext))

    def encrypt_response(self):
        """生成返回WeLink的response body"""
        plain = {"msg": "success", "timestamp": str(int(time.time()))}
        plaintext = json.dumps(plain)
        return {"encrypt": str(self.encrypt(plaintext), encoding="utf-8")}

    def encodeToBase64(self, data):
        return base64.b64encode(data)

    def decodeFromBase64(self, data):
        return base64.b64decode(data)

    def init_key(self, key):
        signature = hashlib.sha1(key.encode()).digest()
        signature = hashlib.sha1(signature).digest()
        return signature[:-4]
