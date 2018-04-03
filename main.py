import tkinter;

root = tkinter.Tk();
root.title("AES 256");
root.geometry('250x200');

btn_folder = tkinter.Button(root, text = "Select folder", command=2);
btn_folder.pack();

btn_encrypt = tkinter.Button(root, text = "Encrypt folder");
btn_encrypt.pack();

btn_decrypt = tkinter.Button(root, text = "Decrypt folder");
btn_decrypt.pack();

root.mainloop();