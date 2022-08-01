# Task 1: There is string s = "Python Bootcamp". Write the code that hashes string.
import hashlib


s = "Python Bootcamp"
encode_str = s.encode()

sha256_object = hashlib.sha256(encode_str)
sha256_hex_dig = sha256_object.hexdigest()  # SHA256 function

sha1_object = hashlib.sha1(encode_str)
sha1_hex_dig = sha1_object.hexdigest()  # SHA1 function

md5_object = hashlib.md5(encode_str)
md5_hex_dig = md5_object.hexdigest()  # MD5 function


if __name__ == "__main__":
    print(sha256_hex_dig)
    print(sha1_hex_dig)
    print(md5_hex_dig)
