class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables  # list of variable names (e.g., ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T'])
        self.domains = domains      # dictionary mapping variable to its domain (e.g., {'WA': ['red', 'green', 'blue'], ...})
        self.constraints = constraints  # list of tuples (variable1, variable2) representing constraints (e.g., [('WA', 'NT'), ...])
        self.assignment = {}  # current assignment of variables to colors

    def is_consistent(self, variable, color, assignment):
        for neighbor in self.variables:
            if (variable, neighbor) in self.constraints and neighbor in assignment:
                if assignment[neighbor] == color:
                    return False
        return True

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned = [var for var in self.variables if var not in assignment]

        var = unassigned[0]
        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtrack(assignment)
                if result:
                    return result
                assignment.pop(var)
        return None

    def solve(self):
        assignment = self.backtrack(self.assignment)
        if assignment:
            return assignment
        else:
            return "No solution found."

# Example usage:
variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
domains = {
    'WA': ['red', 'green', 'blue'],
    'NT': ['red', 'green', 'blue'],
    'Q': ['red', 'green', 'blue'],
    'NSW': ['red', 'green', 'blue'],
    'V': ['red', 'green', 'blue'],
    'SA': ['red', 'green', 'blue'],
    'T': ['red', 'green', 'blue']
}
constraints = [('WA', 'NT'), ('WA', 'SA'), ('NT', 'SA'), ('NT', 'Q'), ('SA', 'Q'), ('SA', 'NSW'), ('SA', 'V'), ('NSW', 'Q'), ('V', 'NSW')]

map_csp = MapColoringCSP(variables, domains, constraints)
solution = map_csp.solve()
print("Solution found:", solution)
