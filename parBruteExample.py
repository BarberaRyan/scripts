import multiprocessing
from hashlib import sha256
 
 
def HashFromSerial(serial):
    divisor = 456976
    letters = []
    for i in range(5):
        letter, serial = divmod(serial, divisor)
        letters.append( 97 + int(letter) )
        divisor /= 26
    return (letters, sha256(bytes(letters)).digest())
 
 
def main():
    h1 = bytes().fromhex("1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad")
    h2 = bytes().fromhex("3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b")
    h3 = bytes().fromhex("74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f")
    numpasswords = int(26 ** 5)
    chunksize = int(numpasswords / multiprocessing.cpu_count())
    with multiprocessing.Pool() as p:
        for (letters, digest) in p.imap_unordered(HashFromSerial, range(numpasswords), chunksize):
            if digest == h1 or digest == h2 or digest == h3:
                password = "".join(chr(x) for x in letters)
                print(password + " => " + digest.hex())
 
 
if __name__ == "__main__":
    main()