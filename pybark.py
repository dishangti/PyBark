import requests
from Crypto.Cipher import AES
import base64
import json

class Bark:
    def __init__(self, device_dir, encryption=False):
        """
        device_dir: Directory of device key, server link, AES key and IV
        encryption: Encryption method
        """

        with open(f"{device_dir}/server.txt", 'r') as f:
            self.server = f.readline()
        with open(f"{device_dir}/device.txt", 'r') as f:
            self.device = f.readline()
        
        self.encryption = encryption
        if encryption:
            with open(f"{device_dir}/aes.txt", 'r') as f:
                self.key = bytes(f.readline().strip('\n'), encoding = "utf8")
                self.iv = bytes(f.readline().strip('\n'), encoding = "utf8")
            self.cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

    def __pad(self, s: bytes):
        block_size = 16
        size_of_last_block = len(s) % block_size
        padding_amount = block_size - size_of_last_block
        pad_bytes = bytes([padding_amount] * padding_amount)
        return s + pad_bytes

    def __aes_encrypt(self, content: bytes):
        """
        content: bytes type
        return: Base64 type
        """
        encrypted = self.cipher.encrypt(self.__pad(content))
        return base64.b64encode(encrypted)

    def send(self, body, title:str="PyBark", level:str='active', sound:str=None, group:str=None, icon:str=None, url:str=None, count:int=None):
        """
        All parameter illustration can be found in Bark App. 
        """
        data = {"body": body, "title":title, level:"level"}
        if sound is not None:
            data["sound"] = sound
        if group is not None:
            data["group"] = group
        if icon is not None:
            data['icon'] = icon
        if url is not None:
            data['url'] = url
        if count is not None:
            data['badge'] = str(count)

        if self.encryption:
            cipher_text = self.__aes_encrypt(bytes(json.dumps(data),encoding = "utf8"))
            data = {"ciphertext": cipher_text}
        res = requests.post(f"{self.server}/{self.device}", data)
        return res