import hashlib

hash_to_crack = "4ab6cffac3b7924dc52286b3bcf04c87f033f9cdac66fb97832ecfd86bb1f93d"

with open("wordlist.txt", "r") as f:
    list_passwords = f.read().split("\n")

for password in list_passwords:
    hash_object = hashlib.sha256(password.encode())
    hex_dig = hash_object.hexdigest()
    if hex_dig == hash_to_crack:
        print("Cracked")
        print("Hash: " + hex_dig)
        print("Password: " + password)
