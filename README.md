# Theorem-Prover-for-Clause-Logic
Theorem prover for a clause logic using the resolution principle.

Implemented a python program that proves whether a clause is entailed by a knowledge base.

Uses the resolution principle to prove a clause is valid by contradiction.

Negates the clause to be proved and add it to the knowledge base, then deduces new clauses until contradiction or until no new clauses can be generated.

The program takes exactly one argument from the command line:
1. A knowledge base file that contains the initial knowledge base and the clause whose validity we want to test. The
input file contains n lines organized as follows: the first n - 1 lines describe the initial KB,
while line n contains the (original) clause to test. The literals of each clause are separated
by a blank space, negated variables are indicated by the prefix ~.

### To Run

python main3.py demo1.in.txt

