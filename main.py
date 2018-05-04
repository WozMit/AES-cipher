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
	frmPassword = tkinter.Tk();
	frmPassword.title("Choose a password");
	txbPassword = Entry(frmPassword, width=45);
	txbPassword.pack();
	txbConfirm = Entry(frmPassword, width=45);
	txbConfirm.pack();
	btnConfirm = tkinter.Button(frmPassword, text="Confirm");
	btnConfirm.pack();
	btnCancel = tkinter.Button(frmPassword, text="Cancel");
	btnCancel.pack();
	#encriptor.encrypt_location(txbLocation.get());

def decrypt_folder():
	frmPassword = tkinter.Tk();
	frmPassword.title("Enter the password");
	txbPassword = Entry(frmPassword, width=45);
	txbPassword.pack();
	btnOk = tkinter.Button(frmPassword, text="Ok");
	btnOk.pack();
	btnCancel = tkinter.Button(frmPassword, text="Cancel");
	btnCancel.pack();
	#encriptor.decrypt_location(txbLocation.get());

start_time = tm.time();

password = "awesome password";
location = "E:/To do/Super Secret X Files";
encriptor = Encryptor(256, password);
#encriptor.encrypt_location(location);
encriptor.decrypt_location(location);

"""
root = tkinter.Tk();
root.title("AES");
root.geometry('250x200');

btnSearch = tkinter.Button(root, text = "Select folder", command=load_folder);
btnSearch.pack();

txbLocation = Entry(root, width=45);
txbLocation.pack(side=TOP);

btnEncrypt = tkinter.Button(root, text = "Encrypt folder", command=encrypt_folder);
btnEncrypt.pack();

btnDecrypt = tkinter.Button(root, text = "Decrypt folder", command=decrypt_folder);
btnDecrypt.pack();

root.mainloop();
"""

print("\nTotal time = "+str(tm.time()-start_time)+" s");