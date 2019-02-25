from copy import copy


class Polynomial:
    def __init__(self, coeffs):
        if len(coeffs) == 0:
            raise ValueError("List of coefficients is empty")
        if not isinstance(coeffs, (list, tuple)):
            raise ValueError('coeffs parameter must be a list or tuple.')
        if not all(map(lambda x: isinstance(x, int), coeffs)):
            raise ValueError("Incorrect input list. All values must be integers")
        self.coeffs = copy(coeffs)
        while self.coeffs[0] == 0 and len(self.coeffs) > 1:
            self.coeffs.pop(0)

    def __len__(self):
        return len(self.coeffs)

    def __add__(self, other):
        if isinstance(other, int):
            coeffs = copy(self.coeffs)
            coeffs[-1] += other
            return Polynomial(coeffs)
        elif isinstance(other, Polynomial):
            l_pol, s_pol = (self, other) if len(self) >= len(other) else (other, self)
            coeffs = list(copy(l_pol.coeffs))
            for i in range(1, len(s_pol) + 1):
                coeffs[-i] += s_pol.coeffs[-i]
            return Polynomial(coeffs)
        else:
            raise TypeError("Unsupported operand type")

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
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
        else:
            raise TypeError("Unsupported operand type")

    __rmul__ = __mul__

    def __sub__(self, other):
        if not isinstance(other, (Polynomial, int)):
            raise TypeError("Unsupported operand type")
        return self + (-1 * other)

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError("Unsupported operand type")
        if len(self) != len(other):
            return False
        else:
            return all([c1 == c2 for c1, c2 in zip(self.coeffs, other.coeffs)])

    def __ne__(self, other):
        return not (self == other)

    def __repr__(self):
        return "Polynomial({})".format(repr(self.coeffs))
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
        if r_coeffs != [0]:
            if result[-1][0] == "+":
                result[-1] = result[-1][1:]
        else:
            return "0"
        return "".join(reversed(result))
