import string

outputTemplate = Element("output-template").select(".output", from_content=True)
outputList = Element("list-output-container")

def printToHTML(text, textStyle="regular"):
    ''' Print Python Outputs to HTML Template '''
    outputHTML = outputTemplate.clone("output", to=outputList)
    outputHTML_content = outputHTML.select("p")
    outputHTML_content.element.innerText = text
    outputList.element.appendChild(outputHTML.element)

    if textStyle == "bold":
        outputHTML_content.element.innerHTML = "<b>" + text + "</b>"

def newLine():
    ''' Make New Line (enter) '''
    outputHTML = outputTemplate.clone("output", to=outputList)
    outputHTML_content = outputHTML.select("p")
    outputHTML_content.element.innerHTML = "<br>"
    outputList.element.appendChild(outputHTML.element)

def lexAnalyzer(*args, **kwargs):
    ''' Lexical Analyzer '''
    sentence = Element("id-kata").value
    input_string = sentence+'#'
    alphabet_list = list(string.ascii_lowercase)
    alphabet_list_upper = list(string.ascii_uppercase)
    state_list = ['q' + str(i) for i in range(42)]

    transition_table = {}

    for state in state_list:
        for i in range(len(alphabet_list)):
            transition_table[(state, alphabet_list[i])] = 'error'
            transition_table[(state, alphabet_list_upper[i])] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    transition_table['q0', ' '] = 'q0'

    # Kamil
    transition_table[('q0', 'K')] = 'q1'
    transition_table[('q1', 'a')] = 'q2'
    transition_table[('q2', 'm')] = 'q3'
    transition_table[('q3', 'i')] = 'q4'
    transition_table[('q4', 'l')] = 'q5'

    # q5 and q6 transition
    transition_table[('q5', ' ')] = 'q6'
    transition_table[('q5', '#')] = 'accept'
    transition_table[('q6', ' ')] = 'q6'
    transition_table[('q6', '#')] = 'accept'

    # Dari q6 ke awal kata
    transition_table[('q6', 'K')] = 'q1'
    transition_table[('q6', 'F')] = 'q7'
    transition_table[('q6', 'R')] = 'q13'
    transition_table[('q6', 'g')] = 'q17'
    transition_table[('q6', 'b')] = 'q20'
    transition_table[('q6', 'p')] = 'q27'
    transition_table[('q6', 'e')] = 'q33'
    transition_table[('q6', 'w')] = 'q35'
    transition_table[('q6', 'r')] = 'q39'

    # Fauzan
    transition_table[('q0', 'F')] = 'q7'
    transition_table[('q7', 'a')] = 'q8'
    transition_table[('q8', 'u')] = 'q9'
    transition_table[('q9', 'z')] = 'q10'
    transition_table[('q10', 'a')] = 'q11'
    transition_table[('q11', 'n')] = 'q5'

    # Rafli
    transition_table[('q0', 'R')] = 'q13'
    transition_table[('q13', 'a')] = 'q14'
    transition_table[('q14', 'f')] = 'q15'
    transition_table[('q15', 'l')] = 'q16'
    transition_table[('q16', 'i')] = 'q5'

    # game
    transition_table[('q0', 'g')] = 'q17'
    transition_table[('q17', 'a')] = 'q18'
    transition_table[('q18', 'm')] = 'q19'
    transition_table[('q19', 'e')] = 'q5'

    # book
    transition_table[('q0', 'b')] = 'q20'
    transition_table[('q20', 'o')] = 'q21'
    transition_table[('q21', 'o')] = 'q22'
    transition_table[('q22', 'k')] = 'q5'

    # burger
    transition_table[('q20', 'u')] = 'q23'
    transition_table[('q23', 'r')] = 'q24'
    transition_table[('q24', 'g')] = 'q25'
    transition_table[('q25', 'e')] = 'q26'
    transition_table[('q26', 'r')] = 'q5'

    # poem
    transition_table[('q0', 'p')] = 'q27'
    transition_table[('q27', 'o')] = 'q28'
    transition_table[('q28', 'e')] = 'q29'
    transition_table[('q29', 'm')] = 'q5'
    
    # plays
    transition_table[('q27', 'l')] = 'q30'
    transition_table[('q30', 'a')] = 'q31'
    transition_table[('q31', 'y')] = 'q32'
    transition_table[('q32', 's')] = 'q5' # s

    # eats
    transition_table[('q0', 'e')] = 'q33'
    transition_table[('q33', 'a')] = 'q34'
    transition_table[('q34', 't')] = 'q32'

    # writes
    transition_table[('q0', 'w')] = 'q35'
    transition_table[('q35', 'r')] = 'q36'
    transition_table[('q36', 'i')] = 'q37'
    transition_table[('q37', 't')] = 'q38'
    transition_table[('q38', 'e')] = 'q32'

    # reads
    transition_table[('q0', 'r')] = 'q39'
    transition_table[('q39', 'e')] = 'q40'
    transition_table[('q40', 'a')] = 'q41'
    transition_table[('q41', 'd')] = 'q32'

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q5':
            printToHTML("Current token: " + current_token + ", VALID")
            current_token = ''
        if state == 'error':
            printToHTML("Current token: " + current_token + ", ERROR")
            break
        idx_char = idx_char + 1

    if state == 'accept':
        printToHTML("Semua token: " + sentence + ", VALID")
        parserEng(sentence)

def clearOutput(*args, **kwargs):
    ''' Clear output when button is clicked '''
    outputList.clear()

def parserEng(sentence):
    ''' Parser for sentence, start if lexAnalyzer output sentence is valid '''
    newLine()
    printToHTML("== Sentence Valid, Starting Parser ==", "bold")
    tokens = sentence.split()
    tokens.append("EOS")

    # Symbols
    non_terminals = ["S", "NN", "VB"]
    terminals = ["Kamil", "Rafli", "Fauzan", "game", "book", "burger", "poem", "plays", "eats", "writes", "reads"]

    # Parse Table
    parse_table = {}

    parse_table[("S", "Kamil")] = ["NN", "VB", "NN"]
    parse_table[("S", "Rafli")] = ["NN", "VB", "NN"]
    parse_table[("S", "Fauzan")] = ["NN", "VB", "NN"]
    parse_table[("S", "game")] = ["NN", "VB", "NN"]
    parse_table[("S", "book")] = ["NN", "VB", "NN"]
    parse_table[("S", "burger")] = ["NN", "VB", "NN"]
    parse_table[("S", "poem")] = ["NN", "VB", "NN"]
    parse_table[("S", "plays")] = ["error"]
    parse_table[("S", "eats")] = ["error"]
    parse_table[("S", "writes")] = ["error"]
    parse_table[("S", "reads")] = ["error"]
    parse_table[("S", "EOS")] = ["error"]

    parse_table[("NN", "Kamil")] = ["Kamil"]
    parse_table[("NN", "Rafli")] = ["Rafli"]
    parse_table[("NN", "Fauzan")] = ["Fauzan"]
    parse_table[("NN", "game")] = ["game"]
    parse_table[("NN", "book")] = ["book"]
    parse_table[("NN", "burger")] = ["burger"]
    parse_table[("NN", "poem")] = ["poem"]
    parse_table[("NN", "plays")] = ["error"]
    parse_table[("NN", "eats")] = ["error"]
    parse_table[("NN", "writes")] = ["error"]
    parse_table[("NN", "reads")] = ["error"]
    parse_table[("NN", "EOS")] = ["error"]

    parse_table[("VB", "Kamil")] = ["error"]
    parse_table[("VB", "Rafli")] = ["error"]
    parse_table[("VB", "Fauzan")] = ["error"]
    parse_table[("VB", "game")] = ["error"]
    parse_table[("VB", "book")] = ["error"]
    parse_table[("VB", "burger")] = ["error"]
    parse_table[("VB", "poem")] = ["error"]
    parse_table[("VB", "plays")] = ["plays"]
    parse_table[("VB", "eats")] = ["eats"]
    parse_table[("VB", "writes")] = ["writes"]
    parse_table[("VB", "reads")] = ["reads"]
    parse_table[("VB", "EOS")] = ["error"]

    # Stack init
    stack = []
    stack.append("%")
    stack.append("S")

    # Input reading init
    idx_token = 0
    symbol = tokens[idx_token]

    # Parse
    while (len(stack) > 0):
        top = stack[len(stack)-1]
        printToHTML("Top = " + top, "bold")
        printToHTML("Symbol = " + symbol, "bold")
        if top in terminals:
            printToHTML("Top adalah simbol terminal")
            if top == symbol:
                stack.pop()
                idx_token = idx_token + 1
                symbol = tokens[idx_token]
                if symbol == "EOS":
                    printToHTML("Isi stack: " + " ".join([str(sym) for sym in stack]))
                    stack.pop()
            else:
                printToHTML("ERROR")
                break
        elif top in non_terminals:
            printToHTML("Top adalah simbol Non Terminal")
            if parse_table[(top, symbol)][0] != "error":
                stack.pop()
                symbols_to_be_pushed = parse_table[(top, symbol)]
                for i in range(len(symbols_to_be_pushed)-1, -1, -1):
                    stack.append(symbols_to_be_pushed[i])
            else:
                printToHTML("ERROR", "bold")
                break
        else:
            printToHTML("ERROR", "bold")
            break
        printToHTML("Isi stack: " + " ".join([str(sym) for sym in stack]))
        newLine()
    
    # Conclusion
    newLine()
    if symbol == "EOS" and len(stack) == 0:
        printToHTML("Input string: " + "'" + sentence + "'", "bold")
        printToHTML("DITERIMA", "bold")
        printToHTML("SESUAI GRAMMAR", "bold")
    else:
        printToHTML("Error, Input string: " + "'" + sentence + "'", "bold")
        printToHTML("TIDAK DITERIMA", "bold")
        printToHTML("TIDAK SESUAI GRAMMAR", "bold")