import random


class RSA:


    def generate_keys(self, base26_first, base26_second):
        base10_first = int(base26_first, 26)
        base10_second = int(base26_second, 26)

        mod_size = 10**200

        if base10_first < mod_size:
            print("Warning, first input was smaller than 10^200")
        if base10_second < mod_size:
            print("Warning, second input was smaller than 10^200")

        base10_first_correct_size = base10_first % mod_size
        base10_second_correct_size = base10_second % mod_size

        base_10_first_odd = self.make_odd(base10_first_correct_size)
        base_10_second_odd = self.make_odd(base10_second_correct_size)

        while not self.is_prime_miller(base_10_first_odd):
            base_10_first_odd += 2

        while not self.is_prime_miller(base_10_second_odd):
            base_10_second_odd += 2

        p = base_10_first_odd
        q = base_10_second_odd

        n = p*q
        r = (p-1)*(q-1)


        #e = 
        #d = self.euclidean_inverse(e, r)


    def encrypy(self):
        pass


    def decrypt(self):
        pass


    def make_odd(self, number):
        if number % 2 == 0:
            number += 1
        return number
    

    def euclidean_inverse(self, e, r):
        for i in range(1, r):
            if (((e % r) * (i % r)) % r == 1):
                return i
        return -1
    

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


def main():
    r = RSA()
    r.generate_keys("79797979797979797979797979797979797979797979797979797979797979797979797797979797979797997979797979797979797979797979797979797979797979797979797979", 
                    "68686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868686868")


if __name__ == "__main__":
    main()
