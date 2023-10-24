import random
import math

class RSA:
    def generate_keys(self, base26_first, base26_second):
        base10_first = self.to_base_ten(base26_first, "abcdefghijklmnopqrstuvwxyz")
        base10_second = self.to_base_ten(base26_second, "abcdefghijklmnopqrstuvwxyz")

        if base10_first < 10**200:
            print("Warning, first string was smaller than 10**200")
        if base10_second < 10**200:
            print("Warning, second string was smaller than 10**200")

        base10_first = base10_first % 10**200
        base10_second = base10_second % 10**200

        base10_first = self.make_odd(base10_first)
        base10_second = self.make_odd(base10_second)

        while not self.is_prime_miller(base10_first):
            base10_first += 2

        while not self.is_prime_miller(base10_second):
            base10_second += 2

        p = base10_first
        q = base10_second

        n = p*q
        r = (p-1)*(q-1)

        e = self.get_e(r)
        d = self.modular_inverse(e, r)

        with open("public.txt", "w") as f:
            f.write(str(n) + "\n" + str(e) + "\n")

        with open("private.txt", "w") as f:
            f.write(str(n) + "\n" + str(d) + "\n")

    def encrypt(self, input, output):
        alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            
        fin = open(input,"rb")
        plain_text_binary = fin.read()
        plain_text = plain_text_binary.decode("utf-8")
        fin.close()

        n, e = 0, 0
        with open("public.txt", "r") as f:
            n = int(f.readline().strip())
            e = int(f.readline().strip())

        max_bytes = math.log(n, 70)
        plain_text_length = len(plain_text)
        blocks_needed = math.ceil(plain_text_length/max_bytes)
        num_bytes_per_block = math.ceil(plain_text_length / blocks_needed)

        fout = open(output,"wb")
        for i in range(blocks_needed):
            plain_text_block = plain_text[i*num_bytes_per_block:(i+1)*num_bytes_per_block]
            plain_number = self.to_base_ten(plain_text_block, alphabet)
            encrypted_number = pow(plain_number, e, n)
            encrypted_text = self.from_base_ten(encrypted_number, alphabet)
            encrypted_text += "$"
            fout.write(encrypted_text.encode("utf-8"))
        fout.close()

    def decrypt(self, input, output):
        alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        fin = open(input,"rb")
        encrypted_text_binary = fin.read()
        encrypted_text = encrypted_text_binary.decode("utf-8")
        fin.close()

        n, d = 0, 0
        with open("private.txt", "r") as f:
            n = int(f.readline().strip())
            d = int(f.readline().strip())

        encrypted_text_blocks = encrypted_text.split("$")

        fout = open(output,"wb")
        for encrypted_text_block in encrypted_text_blocks:
            if encrypted_text_block != "":
                decrypted_number = self.to_base_ten(encrypted_text_block, alphabet)
                decrypted_number = pow(decrypted_number, d, n)
                decrypted_text = self.from_base_ten(decrypted_number, alphabet)
                fout.write(decrypted_text.encode("utf-8"))
        fout.close()

    def make_odd(self, number):
        if number % 2 == 0:
            number += 1
        return number
    
    def modular_inverse(self, e, r):
        return pow(e, -1, r)

    def is_prime_miller(self, n):
        if n == 0: return False
        if n == 1: return False
        if n == 2: return True
        for i in range(20):
            b = random.randrange(2, n)
            ok = self.miller_test(n, b)
            if not ok:
                return False
        return True

    def miller_test(self, n, b):
        new_n = n - 1
        s = 0
        t = 0

        while new_n % 2 == 0:
            new_n //= 2
            s += 1

        t = new_n

        if pow(b, t, n) == 1:
            return True

        for j in range(s):
            if pow(b, t, n) == n-1:
                return True
            t *= 2
        return False

    def from_base_ten(self, x, alphabet):
        base = len(alphabet)
        answer = ""
        while x != 0:
            r = x % base
            answer += alphabet[r]
            x //= base
        return answer[::-1]
    
    def to_base_ten(self, s, alphabet):
        x = 0
        base = len(alphabet)
        for c in s:
            pos = alphabet.find(c)
            x *= base
            x += pos
        return x
    
    def get_e(self, r):
        e = 10**398 + 1
        while math.gcd(r, e) != 1:
            e += 2
        return e
    
def main():
    r = RSA()
    r.generate_keys("thisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykey", 
                  "thisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywow")
    r.encrypt("message.txt", "encrypted_message.txt")
    r.decrypt("encrypted_message.txt", "decrypted_message.txt")

if __name__ == "__main__":
    main()
