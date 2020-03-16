import sys
import copy


class Solver():
    def __init__(self, nbvar, nbclauses, assignment, formula):
        self.nbvar =nbvar
        self.nbclauses = nbclauses
        self.assignment = assignment
        self.formula = formula
    
      
    # check consistency of given formula. return True if satisfiable, return False if not yet decided
    def check_con(self):
       
        check = [None]*self.nbvar
        
      
        for i in range(len(self.formula)):
            l = len(self.formula[i])
           
            for j in range(l):
                literal = self.formula[i][j]
                absolute = abs(literal)
                value = (literal == absolute)
                
                if check[absolute-1] is None:
                    check[absolute-1] = value
                else:
                    if (check[absolute-1] == value):
                        continue
                    else: 
                        return False
        

        
        return True
    
    # check whether there is empty clause. return True if there's a empty clause(unsat), return False if not.
    def check_clause(self):
       
        for i in range(len(self.formula)):
            l = len(self.formula[i])
            if (l == 0):
                return True
        return False
    
    # assign a literal in the clause that has only one literal. if the formula has literals of opposite sign, return False.
    # if return False, it should hold original formula
    def unit_propagate(self):
       
        assignment = []
        
        
        for i in range(len(self.formula)):
            if len(self.formula[i]) == 1:
                literal = self.formula[i][0]
                
                if (-literal in assignment):
                   
                    return False
                elif (literal not in assignment):
                    assignment.append(literal)
        
                                  
        i = 0
        count = len(self.formula)
        while (i < count):
            clause = self.formula[i]
            
            for lit in assignment:
                if (lit in clause):
                    del self.formula[i]
                    count -= 1
                    i -= 1
                    break
                elif (-lit in clause):
                    self.formula[i].remove(-lit)            
                  
            i += 1  
                    
            
        for a in assignment:
            self.assignment[abs(a)-1] = (abs(a) == a)
            
        
     
        if self.check_clause():
            return False
        
        return True
    
    # search pure literal in formula and assign it a truth value
    def pure_assign(self):
    
        truth = [None]*self.nbvar
        
        
        pure = [True]*self.nbvar
      
        for i in range(len(self.assignment)):
            if self.assignment[i] is not None:
                pure[i] = False
        
    
        for j in range(len(self.formula)):
            for k in range(len(self.formula[j])):
                literal = self.formula[j][k]
                
                a = abs(literal) -1
                
                if truth[a] is None:
                    truth[a] = literal
                elif truth[a] != literal:
                    pure[a] = False
           

        for i in range(len(pure)):
            if self.assignment[i] is None and truth[i] is not None:
                if pure[i]:
                    
                    self.assign(truth[i])
      
        
            
                    
                   
                   
    # assign true to the literal
    def assign(self, literal):
        count=0
        length = len(self.formula)
        while (count < length):
            if literal in self.formula[count]:
                del self.formula[count]
                length -= 1
            elif -literal in self.formula[count]:
                self.formula[count].remove(-literal)
                count += 1
            else:
                count += 1

                
        self.assignment[abs(literal)-1] = (literal == abs(literal))
        
        

    # return unassigned literal
        
    def choose_literal(self):
        for i in range(self.nbvar):
            if self.assignment[i] is None:
                return i+1


    # check whether all variables are assigned. Return True if all assigned
    
    def check_assign(self):
        for i in range(self.nbvar):
            if self.assignment[i] is None:
                return False
        return True

    # decide satisfiability of given cnf-formula and return True if sat.
    def solve(self):
        
        if (self.check_clause()):
          
            return False
        
        
        elif (self.check_con()):
            sys.stdout.write('s SATISFIABLE')
            
            self.partial_assign()
            return True
        
        elif (self.check_assign()):
            sys.stdout.write('s SATISFIABLE')
            self.partial_assign()
            return True
        
        
        elif (not self.unit_propagate()):
          
            return False
        
        if (self.check_assign()):
            sys.stdout.write('s SATISFIABLE')
            self.partial_assign()
            return True
        
        
        self.pure_assign()
        
        if (self.check_assign()):
            sys.stdout.write('s SATISFIABLE')
            self.partial_assign()
            return True
        
        literal = self.choose_literal()
      
      
        nbvar = self.nbvar
        nbclauses = self.nbclauses
        assignment = copy.deepcopy(self.assignment)
        formula = copy.deepcopy(self.formula)
        
        assignment2 = copy.deepcopy(self.assignment)
        formula2 = copy.deepcopy(self.formula)     
        
        solver1 = Solver(nbvar,nbclauses,assignment,formula)
        solver1.assign(literal)
       
      
        if (solver1.solve()):
         
            return True
        else:
            
            solver2 = Solver(nbvar,nbclauses,assignment2,formula2)
               
            solver2.assign(-literal)             
          

            return solver2.solve()
            
       
     
    
    def partial_assign(self):
        
        result = []
       
        
        for i in range(self.nbvar):
            if (self.assignment[i] == True):
                result.append(i+1)
            elif (self.assignment[i] == False):
                result.append(-(i+1))
            else:
                continue
                
        sys.stdout.write('\nv ')
    
        for i in result:
            sys.stdout.write(str(i)+' ')
        sys.stdout.write('0 \n')
            
            
def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    
    
    f = open(filename,'r')
    while True:
        line = f.readline()
        if not line: break
        if (line[0] == 'c'): 
            continue
        elif (line[0] == 'p'):
            splited = line.split()
            assert splited[1] == 'cnf'
            nbvar = int(splited[2])
            nbclauses = int(splited[3])
            
            assignment = [None]*nbvar
            formula = [None]*nbclauses
            count = 0
         
            
        else:
            splited = line.split()
            if (len(splited) < 2 or splited[-1] != '0'):
                break
            
  
            
            clause = list(map(int, splited))[:-1]
          
            
          
            formula[count] = clause
            count += 1
            
    f.close()     
    
    solver = Solver(nbvar, nbclauses, assignment, formula)
    
   
    
    if solver.solve():
        return
     
        
    else:
        sys.stdout.write('s UNSATISFIABLE \n')
            
        
    
    
    
main()
