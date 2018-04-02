from Crypto import Random
import os.path

import os;
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
        encoded = self.encrypt_bits(text, self.key);
        with open(file_name + ".woz", 'wb') as file:
            file.write(encoded);
            file.close();
        os.remove(file_name);

    def decrypt_bits(self, encoded_message, key):
        iv = encoded_message[:AES.block_size];
        cipher = AES.new(key, AES.MODE_CBC, iv);
        text = cipher.decrypt(encoded_message[AES.block_size:]);
        return text.rstrip(b"\0");

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as file:
            encoded = file.read();
            file.close();
        text = self.decrypt_bits(encoded, self.key);
        with open(file_name[:-4], 'wb') as file:
            file.write(text);
            file.close();
        os.remove(file_name);

    def get_file_list(self, location, avoid_files=[]):
        file_list = [];
        for dir_name, sub_dir_list, dir_file_list in os.walk(location):
            if(".git" in sub_dir_list):
                    sub_dir_list.remove(".git");
            for file in dir_file_list:
                if(file not in avoid_files):
                    file_list.append(os.path.join(dir_name, file));
        return file_list;


    def encrypt_location(self, location=os.path.dirname(os.path.realpath(__file__))):
        avoid_files = [__file__, "README.md", "enc-dec.py"];
        file_list = self.get_file_list(location, avoid_files);
        for file in file_list:
            self.encrypt_file(file);

    def decrypt_location(self, location=os.path.dirname(os.path.realpath(__file__))):
        avoid_files = [__file__, "README.md", "enc-dec.py"];
        file_list = self.get_file_list(location, avoid_files);
        for file in file_list:
            self.decrypt_file(file);

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e';
encryptor = Encryptor(key);
#encryptor.encrypt_location();
#encryptor.decrypt_location();

"""
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')

if os.path.isfile('data.txt.enc'):
    while True:
        password = str(input("Enter password: "))
        enc.decrypt_file("data.txt.enc")
        p = ''
        with open("data.txt", "r") as f:
            p = f.readlines()
        if p[0] == password:
            enc.encrypt_file("data.txt")
            break

    while True:
        #clear()
        choice = int(input(
            "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to Encrypt all files in the directory.\n4. Press '4' to decrypt all files in the directory.\n5. Press '5' to exit.\n"))
        #clear()
        if choice == 1:
            enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
        elif choice == 2:
            enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
        elif choice == 3:
            enc.encrypt_all_files()
        elif choice == 4:
            enc.decrypt_all_files()
        elif choice == 5:
            exit()
        else:
            print("Please select a valid option!")

else:
    while True:
        #clear()
        password = str(input("Setting up stuff. Enter a password that will be used for decryption: "))
        repassword = str(input("Confirm password: "))
        if password == repassword:
            break
        else:
            print("Passwords Mismatched!")
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file("data.txt")
    print("Please restart the program to complete the setup")"""