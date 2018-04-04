from aes_gcm import Encryptor;
import time as tm;
import tkinter;
from tkinter import *;
from tkinter import filedialog;
from tkinter import messagebox;

def load_folder():
	folder = filedialog.askdirectory();
	txbLocation.delete(0, END);
	txbLocation.insert(0, folder);

def encrypt_folder():
	encriptor.encrypt_location(txbLocation.get());

def decrypt_folder():
	encriptor.decrypt_location(txbLocation.get());

start_time = tm.time();

password = "awesome password";
location = "D:\Documentos\Python\AES Cipher\X Files";
encriptor = Encryptor(256, password);
#encriptor.encrypt_location(location);
#encriptor.decrypt_location(location);

root = tkinter.Tk();
root.title("AES");
root.geometry('250x200');

btnSearch = tkinter.Button(root, text = "Select folder", command=load_folder);
btnSearch.pack();

txbLocation = Entry(root, width=25);
txbLocation.pack(side=TOP);

btnEncrypt = tkinter.Button(root, text = "Encrypt folder", command=encrypt_folder);
btnEncrypt.pack();

btnDecrypt = tkinter.Button(root, text = "Decrypt folder", command=decrypt_folder);
btnDecrypt.pack();

root.mainloop();

print("\nTotal time = "+str(tm.time()-start_time)+" s");