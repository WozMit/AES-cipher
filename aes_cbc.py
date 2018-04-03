import os;
from Crypto import Random;
from Crypto.Cipher import AES;

class Encryptor:
    def __init__(self, key):
        self.key = key;

    def pad(self, s):
        return s + b"\0" * ( AES.block_size - len(s) % AES.block_size );

    def encrypt_bits(self, message, key):
        message = self.pad(message);
        iv = Random.new().read(AES.block_size);
        cipher = AES.new(key, AES.MODE_CBC, iv);
        return iv + cipher.encrypt(message);

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as file:
            text = file.read();
            file.close();
        ciphertext = self.encrypt_bits(text, self.key);
        with open(file_name + ".woz", 'wb') as file:
            file.write(ciphertext);
            file.close();
        os.remove(file_name);

    def decrypt_bits(self, ciphermessage, key):
        iv = ciphermessage[:AES.block_size];
        cipher = AES.new(key, AES.MODE_CBC, iv);
        text = cipher.decrypt(ciphermessage[AES.block_size:]);
        return text.rstrip(b"\0");

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as file:
            ciphertext = file.read();
            file.close();
        text = self.decrypt_bits(ciphertext, self.key);
        with open(file_name[:-4], 'wb') as file:
            file.write(text);
            file.close();
        os.remove(file_name);

    def get_file_list(self, location, avoid_files=[]):
        file_list = [];
        for dir_name, sub_dir_list, dir_file_list in os.walk(location):
            for file in dir_file_list:
                if(file not in avoid_files):
                    file_list.append(os.path.join(dir_name, file));
        return file_list;


    def encrypt_location(self, location=os.path.dirname(os.path.realpath(__file__))):
        file_list = self.get_file_list(location);
        for file in file_list:
            self.encrypt_file(file);

    def decrypt_location(self, location=os.path.dirname(os.path.realpath(__file__))):
        file_list = self.get_file_list(location);
        for file in file_list:
            self.decrypt_file(file);

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e';
encryptor = Encryptor(key);
#encryptor.encrypt_location("D:\Documentos\Python\AES Cipher\X Files");
#encryptor.decrypt_location("D:\Documentos\Python\AES Cipher\X Files");