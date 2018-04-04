"""
Solution to: Probability of a Hidden Path Problem
Rosalind Challenge ID: BA10A

DESCRIPTION:
Given: A hidden path π followed by the states States
and transition matrix Transition of an HMM (Σ, States,
Transition, Emission).

Returns: The probability of this path, Pr(π). You may assume that initial probabilities are equal.

Tyler Huntington, April 2018
"""

class solver:

    def __init__(self, input_datafile):
        self.states = []
        self.h_path = ""
        self.p_trans = {}
        self.p_init = {}
        self.input_data = self.parse(input_datafile)
        self.solution = -1
        self.solve()

    def parse(self, input_datafile):
        with open(input_datafile, 'r') as f:
            self.h_path = f.readline().strip()
            next(f)
            self.states = f.readline().strip().split()
            next(f)
            next(f)
            for s in self.states:
                probs = f.readline().strip().split()[1:]
                probs = list(map(lambda x: float(x), probs))
                self.p_trans[s] = {k:v for (k,v) in zip(self.states, probs)}

        init_prob = 1/len(self.states)
        self.p_init = {k:v for (k,v) in [(s, init_prob) for s in self.states]}
        print(self.p_init)

    def solve(self):

        self.solution = self.p_init[self.h_path[0]]
        prev = self.h_path[0]
        for c in self.h_path[1:]:
            self.solution *= self.p_trans[prev][c]
            prev = c

    def __str__(self):
        return (str(self.solution))



def main():
    input_filename = "data.txt"
    solution = solver(input_filename)

    print(solution)

if __name__=='__main__':
    main()
