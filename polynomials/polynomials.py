class Polynomial:
    def __init__(self, coefs):
        self.coefficients = coefs
    
    def degree(self):

        return len(self.coefficients) - 1

    def __str__(self):

        coefs = self.coefficients
        terms = []

        # Degree 0 and 1 terms conventionally have different representation.
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")

        # Remaining terms look like cx^d, though factors of 1 are dropped.
        terms += [f"{'' if c ==1 else c}x^{d}"
                    for d, c in enumerate(coefs[2:], start=2) if c>0]

         # Sum polynomial terms from high to low exponent.
        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):

        return self.__class__.__name__  + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
            self.coefficients == other.coefficients





        
