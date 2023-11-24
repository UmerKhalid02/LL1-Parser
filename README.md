# Requirements

You code must read the CFG from text file. The format of the grammar is as follows:  
o Every production is written separately on a new line.  
  &emsp;▪ E.g. 𝐸 → 𝐸 + 𝑇 / 𝑇(𝑤𝑟𝑜𝑛𝑔)  
  &emsp; 𝐸 → 𝐸 + 𝑇  
  &emsp;  𝐸 → 𝑇 (𝑟𝑖𝑔ℎ𝑡)  
• The data in the file should be tab separated.  
  &emsp;o 𝐸 < 𝑡𝑎𝑏 >→< 𝑡𝑎𝑏 > 𝐸 < 𝑡𝑎𝑏 > +< 𝑡𝑎𝑏 > 𝑇  
• You need to first calculate FIRST() and FOLLOW() sets from the given CFG. NonTerminals should represent the left hand side of the production. Whereas, a combination of terminals and non-terminals can be present on the right hand side of the production.  
• For the ease of parsing, the productions should be in the form of 𝐸 = 𝐸 + 𝑇 where ‘=’ represents the corresponding ‘->’ symbol.  
• ɛ is the symbol representing epsilon. The grammar given below has eight productions and is provided to you as a sample production in the sample.txt file:  
  &emsp;𝐸 = 𝑇 𝐸𝐷  
  &emsp;𝐸𝐷 = + 𝑇 𝐸𝐷  
  &emsp;𝐸𝐷 = ɛ  
  &emsp;𝑇 = 𝐹 𝑇𝐷  
  &emsp;𝑇𝐷 = ∗ 𝐹 𝑇𝐷  
  &emsp;𝑇𝐷 = ɛ  
  &emsp;𝐹 = (𝐸)  
  &emsp;𝐹 = 𝑖𝑑
    
• You code must be generic and it should give correct result on any CFG and on any number of productions.  
• Non-terminal should be represented as capital letters {A-Z}  
• Terminals can contain characters ( ; . ‘ @ ) { * - + etc.) , numbers { 0-9} and small letters {a-z}, excluding ‘=’ since it is used as a reserved symbol.  
&emsp;o {A-Z} = {A-Z} / {a-z} / {0-9} / any character / any bracket  
• The right hand side of the production is restricted to maximum 10 literals.  
• The program should input the string (which is to be parsed) from the user.  
• The program should output error/invalid parse if the input string is rejected by the parser.  
• All input strings have to end with a '$’.  
• Your program should output two text files. The name of the output files should be firstfollow.txt (containing first sets and then follow sets) and parseoutput.txt (containing parsing table).  
• The format of firstfollow.txt file is:o The first item of each line is a non-terminal with its first or follow element separated by a tab.  
o In case of multiple elements of first or follow set. You can write multiple entries against a single non-terminal e.g.  
  &emsp;▪ T <tab> *  
  &emsp;▪ T <tab> $  
  &emsp;▪ T <tab> )  
    
  
# Assumption  
Grammar is not left recursive  
Grammar is not ambiguous  
grammar is left factored  
  
In my code i used 'eps' as 'ɛ'  
