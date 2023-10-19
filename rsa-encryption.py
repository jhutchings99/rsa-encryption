import random
import time 

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
        d = self.modular_inverse(e)

        print("here")
        with open("public.txt", "w") as f:
            f.write(n)

    def encrypt(self):
        pass

    def decrypt(self):
        pass


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
        while self.GCD(r, e) != 1:
            e += 2
        print("gt here")
        return e
    
    def GCD(self, a, b):
        pass
    
def main():
    r = RSA()
    r.generate_keys("thisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykeythisismykey", 
                   "thisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywowthisismyothersupersecretkeywow")

if __name__ == "__main__":
    main()
