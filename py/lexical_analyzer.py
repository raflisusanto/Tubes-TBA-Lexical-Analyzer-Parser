import string

outputTemplate = Element("output-template").select(".output", from_content=True)
outputList = Element("list-output-container")

def lexAnalyzer(*args, **kwargs):
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
            outputHTML = outputTemplate.clone("output", to=outputList)
            outputHTML_content = outputHTML.select("p")
            outputHTML_content.element.innerText = "Current token: " + current_token + ", VALID"
            outputList.element.appendChild(outputHTML.element)

            current_token = ''
        if state == 'error':
            outputHTML = outputTemplate.clone("output", to=outputList)
            outputHTML_content = outputHTML.select("p")
            outputHTML_content.element.innerText = "Current token: " + current_token + ", ERROR"
            outputList.element.appendChild(outputHTML.element)

            break
        idx_char = idx_char + 1

    if state == 'accept':
        outputHTML = outputTemplate.clone("output", to=outputList)
        outputHTML_content = outputHTML.select("p")
        outputHTML_content.element.innerText = "Semua token: " + sentence + ", VALID"
        outputList.element.appendChild(outputHTML.element)

def clearInput(*args, **kwargs):
    outputList.clear()