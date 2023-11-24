import pandas as pd

epsilon = 'eps'

def ReadGrammar(filename):
    grammar = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                if line:
                    left, right = line.split('=')
                    left = left.strip()  # Non-terminal
                    right = right.strip()  # Productions

                    if left not in grammar:
                        grammar[left] = []

                    right = right.replace('\t', ' ')
                    grammar[left].append(right)

        return grammar

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading grammar: {e}")
        return None


# utility function to find epsilon productions    
def EpsilonProductions(grammar):
    eps = set()
    for non_terminal in grammar:
        for production in grammar[non_terminal]:
            if production == epsilon:
                eps.add(non_terminal)

    return eps

def First(grammar, symbol, epsilon_productions):
    first = set()

    if symbol not in grammar:
        first.add(symbol)
        return first

    for production in grammar[symbol]:
        prod = production.split()
        if len(prod) == 0:
            first.add(epsilon)
        else:
            i = 0
            while i < len(prod):
                if prod[i] != symbol:
                    first.update(First(grammar, prod[i], epsilon_productions))
                    if epsilon not in First(grammar, prod[i], epsilon_productions):
                        break
                i += 1
            else:
                first.add(epsilon)

    return first


def Follow(grammar, symbol, epsilon_productions):
    follow = set()

    if symbol not in grammar:
        return follow

    if symbol == list(grammar)[0]:  # Starting symbol
        follow.add('$')  # Add end marker to FOLLOW of the start symbol

    for key in grammar:
        for production in grammar[key]:
            prod = production.split()

            if symbol in prod:
                index = prod.index(symbol)

                # Case 1: A -> αBβ (where B is the symbol)
                if index < len(prod) - 1:
                    rest = prod[index + 1:]

                    # Add FIRST(β) - 'eps' to FOLLOW(B)
                    follow.update(First(grammar, rest[0], epsilon_productions) - {epsilon})

                    # If 'eps' is in FIRST(β), add FOLLOW(A) to FOLLOW(B)
                    if epsilon in First(grammar, rest[0], epsilon_productions):
                        i = 0
                        while epsilon in First(grammar, rest[0], epsilon_productions):
                            rest = rest[1:]
                            if len(rest) == 0:
                                follow.update(Follow(grammar, key, epsilon_productions))
                                break
                            follow.update(First(grammar, rest[i], epsilon_productions) - {epsilon})
                            i += 1

                # Case 2: A -> αB or A -> αBβ where β =>* 'eps'
                elif key != symbol:
                    follow.update(Follow(grammar, key, epsilon_productions))

    return follow


def CreateFirstFollowFile(first_sets, follow_sets, filename):

    with open(filename, 'w') as file:
        # Writing FIRST sets to the file
        file.write("FIRST\n")
        for non_terminal, first in first_sets.items():
            file.write(f"{non_terminal}\t")
            file.write('\t'.join(sorted(first)))  # Writing first set elements separated by tabs
            file.write('\n')

        # Writing FOLLOW sets to the file
        file.write("\nFOLLOW\n")
        for non_terminal, follow in follow_sets.items():
            file.write(f"{non_terminal}\t")
            file.write('\t'.join(sorted(follow)))  # Writing follow set elements separated by tabs
            file.write('\n')


def GenerateParseDictionary(grammar, eps_productions):
    parse_table = {}

    for non_terminal in grammar:
        for production in grammar[non_terminal]:
            prod = production.split()

            # Case 1: A -> α
            if prod[0] != epsilon:
                for terminal in First(grammar, prod[0], eps_productions):
                    if terminal != epsilon:
                        parse_table[(non_terminal, terminal)] = production

            # Case 2: A -> αBβ
            else:
                for terminal in Follow(grammar, non_terminal, eps_productions):
                    parse_table[(non_terminal, terminal)] = production

    return parse_table


def CreateParseTable(parse_dict):
    non_terminals = sorted({key[0] for key in parse_dict.keys()})
    terminals = sorted({key[1] for key in parse_dict.keys()})

    table_data = {terminal: {non_term: '' for non_term in non_terminals} for terminal in terminals}

    for key, value in parse_dict.items():
        table_data[key[1]][key[0]] = value

    df = pd.DataFrame(table_data).fillna('')
    return df


def ParseInputString(input_string, parse_dict, grammar):
    stack_top = list(grammar)[0]
    
    stack = ['$']
    stack.append(stack_top)

    if input_string[-1] != '$':
        input_string += ' $'

    input_string = input_string.split(' ')
    action = []
    
    with open('parseoutput.txt', 'w') as file:

        file.write('Stack\t\t\tInput\t\t\tAction\n')
        file.write(f'{" ".join(stack):<15}\t{" ".join(input_string):<15}\t{" ".join(action)}\n')

        while True:
            top = stack[-1]
            symbol = input_string[0]

            if top == '$' and symbol == '$':
                action.append('ACCEPT')
                file.write(f'{" ".join(stack):<15}\t{" ".join(input_string):<15}\t{action[-1]}\n')
                break

            if top == symbol:
                stack.pop()
                input_string = input_string[1:]
                action.append(f'MATCH {symbol}')
                file.write(f'{" ".join(stack):<15}\t{" ".join(input_string):<15}\t{action[-1]}\n')
            else:
                if (top, symbol) in parse_dict:
                    production = parse_dict[(top, symbol)]
                    stack.pop()
                    if production != epsilon:
                        stack += production.split()[::-1]
                    action.append(f'{top}->{production}')
                    file.write(f'{" ".join(stack):<15}\t{" ".join(input_string):<15}\t{action[-1]}\n')
                else:
                    action.append('REJECT')
                    file.write(f'{" ".join(stack):<15}\t{" ".join(input_string):<15}\t{action[-1]}\n')
                    break

        file.write("==============================\n")
        file.write(f"YOUR STRING HAS BEEN {action[-1].upper()}!\n")
        file.write("==============================")



def main():
    grammar = ReadGrammar('grammar6.txt')
    eps_productions = EpsilonProductions(grammar)

    first_sets = {}
    follow_sets = {}

    for non_terminal in grammar:
        first_sets[non_terminal] = First(grammar, non_terminal, eps_productions)
        follow_sets[non_terminal] = Follow(grammar, non_terminal, eps_productions)

    CreateFirstFollowFile(first_sets, follow_sets, 'firstfollow.txt')

    parse_dict = GenerateParseDictionary(grammar, eps_productions)
    
    table = CreateParseTable(parse_dict)
    #print(table)

    #table.to_csv('parse_table.csv')

    input_string = "a c d b"
    #input_string = input("Enter input string each terminal separated by space (id + id * id): ")
    ParseInputString(input_string, parse_dict, grammar)


if __name__ == '__main__':
    main()
