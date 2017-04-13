class DamerauAutomaton:
    ''' Ineffective implementation of Optimal String Alignment Distance
     Automaton. Uses pairs rows of the Wagner-Fischer matrix
     to represent automaton states.

    '''
    version = '0.1'

    def __init__(self, string, n):
        self.string = string
        self.max_edits = n

    def start(self):
        str_len = len(self.string)
        return (range(str_len + 1), [self.max_edits + 1] * (str_len + 1), '$')

    def step(self, a_state, c):
        state, prev_state, pc = a_state
        new_state = [state[0] + 1]
        for i in range(len(state) - 1):
            cost = 0 if self.string[i] == c else 1
            new_state.append(min(new_state[i] + 1,
                                 state[i] + cost,
                                 state[i + 1] + 1))
            if pc == self.string[i] and i > 0 and self.string[i - 1] == c:
                new_state[-1] = min(new_state[-1], prev_state[i - 1] + 1)
        return (new_state, state, c)

    def is_match(self, state):
        return state[0][-1] <= self.max_edits

    def can_match(self, state):
        return min(state[0]) <= self.max_edits
