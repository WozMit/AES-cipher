from Crypto.Cipher import AES;
from Crypto.Random import get_random_bytes;

#key = b'\x1d\x89x~ NX\x0b\xdc\x96M\xf1%q\x95\x9a';
#key = b'8\xa9\xe8\xf2\x07\x07\x83F\xef\xb1\xe6p"<\xc7C\xff\xa3kd\xb0\xd76S';
key = b'l\xdd2\xdf\xe5\xc7\x7f\xc8\xe3\xfbE\xffgt\x1fc\x11\xbb\xfe\xc9\x08\xf2>Zsf\x10\x1eS\xedDA';

plain_text = b'Some important text';

nonce = get_random_bytes(16);
aad = b'WozMit';
cipher = AES.new(key=key, mode=AES.MODE_GCM, nonce=nonce, mac_len=16);
cipher.update(aad);
ciphertext, tag = cipher.encrypt_and_digest(plain_text);
print("Original text:", plain_text);
print("Ciphertext:", ciphertext);
print("Tag:", tag);
print("=============================================");

r_key = b'l\xdd2\xdf\xe5\xc7\x7f\xc8\xe3\xfbE\xffgt\x1fc\x11\xbb\xfe\xc9\x08\xf2>Zsf\x10\x1eS\xedDA';
r_nonce = nonce;
r_aad = aad;
r_ciphertext = ciphertext;


cipher = AES.new(key=r_key, mode=AES.MODE_GCM, nonce=r_nonce, mac_len=16);
cipher.update(r_aad);
try:
    plain_text = cipher.decrypt_and_verify(r_ciphertext, tag);
    print("MAC validated: Data was encrypted by someone with the shared secret passphrase");
    print("Decrypted succesfully:", plain_text);
except:
    print("MAC validation failed during decryption. No authentication gurantees on this ciphertext");