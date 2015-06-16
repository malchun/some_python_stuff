#!/usr/bin/env python3
# Program returns all fractions between entered values
# with denominator less that entered
# by malchun

import fractions

def main():
    """ Just main """
    # Input from command line 
    a = fractions.Fraction(input("Enter first fraction with / (default = 13/16):") or "13/16")
    b = fractions.Fraction(input("Enter second fraction with / (default = 9/11):") or "9/11")
    d = int(input("Enter max denominator (default = 100):") or "100")
    an = a.numerator / a.denominator
    bn = b.numerator / b.denominator
    # I want it work this way
    assert an < bn

    def gen_fractions(a, b, n):
        """ Function that generates fractions 
            that could be good for us
        [in] - from, to, denominator
        [out] - iterator with candidates
        """
        # Because casting to int is magic!
        ad = int(a*n) - 1
        bd = int(b*n) + 1
        for i in range(ad, bd):
            yield i

    # finding all fractions 
    result = set()
    for n in range(1, d+1):
        for res in gen_fractions(an, bn, n):
            if res / n < bn and res / n > an:
                result.add(fractions.Fraction(res, n))

    # and we have result
    for f in result:
        print(f)

if __name__ == "__main__":
    main()
