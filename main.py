from aes_gcm import Encryptor;
import time as tm;
#import tkinter;

start_time = tm.time();

#root = tkinter.Tk();
#root.title("AES 256");
#root.geometry('250x200');

#btn_folder = tkinter.Button(root, text = "Select folder", command=2);
#btn_folder.pack();

#btn_encrypt = tkinter.Button(root, text = "Encrypt folder");
#btn_encrypt.pack();

#btn_decrypt = tkinter.Button(root, text = "Decrypt folder");
#btn_decrypt.pack();

#root.mainloop();

encriptor = Encryptor(256, "awesome password");
#encriptor.encrypt_location("D:\Documentos\Python\AES Cipher\X Files");
#encriptor.decrypt_location("D:\Documentos\Python\AES Cipher\X Files");

print("\nTotal time = "+str(tm.time()-start_time)+" s");