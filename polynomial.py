from copy import copy


class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = copy(coeffs)
        assert len(coeffs) != 0
        while self.coeffs[0] == 0 and len(self.coeffs) > 1:
            self.coeffs.pop(0)

    def __len__(self):
        return len(self.coeffs)

    def __add__(self, other):
        assert isinstance(other, (Polynomial, int))
        if isinstance(other, int):
            coeffs = copy(self.coeffs)
            coeffs[-1] += other
            return Polynomial(coeffs)
        else:
            l_pol, s_pol = (self, other) if len(self) >= len(other) else (other, self)
            coeffs = list(copy(l_pol.coeffs))
            for i in range(1, len(s_pol) + 1):
                coeffs[-i] += s_pol.coeffs[-i]
            return Polynomial(coeffs)

    def __mul__(self, other):
        assert isinstance(other, (Polynomial, int))
        coeffs = []
        if isinstance(other, int):
            assert other != 0
            for i in range(len(self)):
                coeffs.append(self.coeffs[i] * other)
            return Polynomial(coeffs)
        elif isinstance(other, Polynomial):
            coeffs = [0] * (len(self) + len(other) - 1)
            for i, x1 in enumerate(self.coeffs):
                for j, x2 in enumerate(other.coeffs):
                    coeffs[i + j] += x1 * x2
            return Polynomial(coeffs)

    __rmul__ = __mul__

    def __sub__(self, other):
        assert isinstance(other, (Polynomial, int))
        return self + (-1 * other)

    def __eq__(self, other):
        assert isinstance(other, Polynomial)
        if len(self) != len(other):
            return False
        else:
            return all([c1 == c2 for c1, c2 in zip(self.coeffs, other.coeffs)])

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        result = []
        r_coeffs = self.coeffs[::-1]
        for i, c in enumerate(r_coeffs):
            if c != 0:
                if i == 0:
                    result.append(str("{:+d}".format(c)))
                elif i == 1:
                    result.append(("+" if c > 0 else "-") + (str(abs(c)) if (abs(c) != 1) else "") + "x")
                else:
                    result.append(("+" if c > 0 else "-") + (
                        str(abs(c)) if (abs(c) != 1) else "") + "x^" + str(i))
        if result[-1][0] == "+":
            result[-1] = result[-1][1:]
        return "".join(reversed(result))
