# Requirements

You code must read the CFG from text file. The format of the grammar is as follows:\n
o Every production is written separately on a new line.\n
  \t\t▪ E.g. 𝐸 → 𝐸 + 𝑇 / 𝑇(𝑤𝑟𝑜𝑛𝑔)\n
  \t\t▪ 𝐸 → 𝐸 + 𝑇\n
  \t\t  𝐸 → 𝑇 (𝑟𝑖𝑔ℎ𝑡)\n
• The data in the file should be tab separated.\n
  \t\to 𝐸 < 𝑡𝑎𝑏 >→< 𝑡𝑎𝑏 > 𝐸 < 𝑡𝑎𝑏 > +< 𝑡𝑎𝑏 > 𝑇\n
• You need to first calculate FIRST() and FOLLOW() sets from the given CFG. NonTerminals should represent the left hand side of the production. Whereas, a combination of terminals and non-terminals can be present on the right hand side of the production.\n
• For the ease of parsing, the productions should be in the form of 𝐸 = 𝐸 + 𝑇 where ‘=’ represents the corresponding ‘->’ symbol.\n
• ɛ is the symbol representing epsilon. The grammar given below has eight productions and is provided to you as a sample production in the sample.txt file:\n
  \t\t𝐸 = 𝑇 𝐸𝐷\n
  \t\t𝐸𝐷 = + 𝑇 𝐸𝐷\n
  \t\t𝐸𝐷 = ɛ\n
  \t\t𝑇 = 𝐹 𝑇𝐷\n
  \t\t𝑇𝐷 = ∗ 𝐹 𝑇𝐷\n
  \t\t𝑇𝐷 = ɛ\n
  \t\t𝐹 = (𝐸)\n
  \t\t𝐹 = 𝑖𝑑\n
• You code must be generic and it should give correct result on any CFG and on any number of productions.\n
• Non-terminal should be represented as capital letters {A-Z}\n
• Terminals can contain characters ( ; . ‘ @ ) { * - + etc.) , numbers { 0-9} and small letters {a-z}, excluding ‘=’ since it is used as a reserved symbol.\n
o {A-Z} = {A-Z} / {a-z} / {0-9} / any character / any bracket\n
• The right hand side of the production is restricted to maximum 10 literals.\n
• The program should input the string (which is to be parsed) from the user.\n
• The program should output error/invalid parse if the input string is rejected by the parser.\n
• All input strings have to end with a '$’.\n
• Your program should output two text files. The name of the output files should be firstfollow.txt (containing first sets and then follow sets) and parseoutput.txt (containing parsing table).\n
• The format of firstfollow.txt file is:o The first item of each line is a non-terminal with its first or follow element separated by a tab.\n
o In case of multiple elements of first or follow set. You can write multiple entries against a single non-terminal e.g.\n
  \t\t▪ T <tab> *\n
  \t\t▪ T <tab> $\n
  \t\t▪ T <tab> )\n
• The format of parseoutput.txt file is:\n

Enter the input string: id+id*id$
======================================
Stack         Input             Action
======================================
$E           id+id*id$          E=T ED
Etc.
======================================
YOUR STRING HAS BEEN ACCEPTED/REJECTED 
======================================
\n\n\n
# Assumption\n
Grammar is not left recursive\n
Grammar is not ambiguous\n
grammar is left factored\n
\n
In my code i used 'eps' as 'ɛ'
