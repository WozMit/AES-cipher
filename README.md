# AES Cipher
A python script for Authenticated Encryption [AE](https://en.wikipedia.org/wiki/Authenticated_encryption) with [AES](https://es.wikipedia.org/wiki/Advanced_Encryption_Standard) (i.e., 128, 192 and 256) in [GCM](https://en.wikipedia.org/wiki/Galois/Counter_Mode) mode of operation for data authenticity (integrity) and confidentiality. The Keys are obtained using the [scrypt](https://en.wikipedia.org/wiki/Scrypt) [KDF](https://en.wikipedia.org/wiki/Key_derivation_function) introduced in Percival's paper ["Stronger key derivation via sequential memory-hard functions"](http://www.tarsnap.com/scrypt/scrypt.pdf).

### Dependencies
* Python 3.6.4
* PyCryptodome 3.5.1 [official site](http://pycryptodome.readthedocs.io/en/latest/src/introduction.html), [PyPI](https://pypi.python.org/pypi/pycryptodome), [Source Repo (GitHub)](https://github.com/Legrandin/pycryptodome). Available via `pip install pycryptodome`

### Documentation
* [PyCryptodome’s documentation](https://www.pycryptodome.org/en/latest/)
* [PyCryptodome API documentation](http://pycryptodome.readthedocs.io/en/latest/src/api.html)
* [How to choose AE mode](https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/)

### Author
WozMit