import os;
from Crypto.Cipher import AES;
from Crypto.Protocol.KDF import scrypt;
from Crypto.Random import get_random_bytes;

class Encryptor:
	def __init__(self, key_len, password):
		self.key_len = key_len;
		self.password = password;

	def encrypt_bytes(self, plain_text):
		salt = get_random_bytes(8);
		key = scrypt(self.password, salt=salt, key_len=self.key_len//8, N=16384, r=8, p=1);
		nonce = get_random_bytes(16);
		cipher = AES.new(key=key, mode=AES.MODE_GCM, nonce=nonce, mac_len=16);
		cipher.update(b'WozMit');
		ciphertext, tag = cipher.encrypt_and_digest(plain_text);
		return (self.key_len//64).to_bytes(1, byteorder='big') + salt + nonce + tag + ciphertext;

	def encrypt_file(self, file_name):
		with open(file_name, 'rb') as file:
			plain_text = file.read();
			file.close();
		ciphermessage = self.encrypt_bytes(plain_text);
		with open(file_name + ".woz", 'wb') as file:
			file.write(ciphermessage);
			file.close();
		os.remove(file_name);

	def decrypt_bytes(self, ciphermessage):
		key_len = int.from_bytes(ciphermessage[:1], byteorder='big')*64;
		salt = ciphermessage[1:9];
		nonce = ciphermessage[9:25];
		tag = ciphermessage[25:41];
		ciphertext = ciphermessage[41:];
		key = scrypt(self.password, salt=salt, key_len=key_len//8, N=16384, r=8, p=1);
		cipher = AES.new(key=key, mode=AES.MODE_GCM, nonce=nonce, mac_len=16);
		cipher.update(b'WozMit');
		try:
			plain_text = cipher.decrypt_and_verify(ciphertext, tag);
			return plain_text;
		except:
			return False;

	def decrypt_file(self, file_name):
		with open(file_name, 'rb') as file:
			ciphermessage = file.read();
			file.close();
		plain_text = self.decrypt_bytes(ciphermessage);
		if(plain_text == False):
			print("Unable to decrypt "+file_name+". Incorrect password or corrupted file.");
		else:
			with open(file_name[:-4], 'wb') as file:
				file.write(plain_text);
				file.close();
			os.remove(file_name);

	def get_file_list(self, location):
		file_list = [];
		for dir_name, sub_dir_list, dir_file_list in os.walk(location):
			for file in dir_file_list:
				file_list.append(os.path.join(dir_name, file));
		return file_list;

	def encrypt_location(self, location):
		file_list = self.get_file_list(location);
		for file in file_list:
			self.encrypt_file(file);

	def decrypt_location(self, location):
		file_list = self.get_file_list(location);
		for file in file_list:
			self.decrypt_file(file);