# DPLL SAT solver

2019 spring KAIST CS402 course programming assingment

Language : Python3

Type of program : Command line interface

** If you want to know about the theoritical aspects used in this program, please refer to the "DPLL SAT solver description" pdf file.

---

### How to use?

On the command line, type the command like following example format.

*ex) $ python3 [solvepy3.py](http://solvepy3.py) "test.cnf"*

[**solvepy3.py**](http://solvepy3.py) is python source file and **"test.cnf"** is arbitrary cnf format file that you want to test. 

---

### Output

1. If the program finds satisfiable partial assignment, it returns the result on the standard output.

> s SATISFIABLE
v 2 5 -7 0

positive numbers(2, 5) means true assignment to 2, 5 variables and negative numbers (-7) means false assignment to variable 7. 
0 indicates the end of partial assignment.


2. If it results unsatisfiable, it returns "Unsatisfiable" 

> s UNSATISFIABLE
