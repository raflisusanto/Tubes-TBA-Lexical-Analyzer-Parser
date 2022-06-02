import string

outputTemplate = Element("output-template").select(".output", from_content=True)
outputList = Element("list-output-container")

def lexAnalyzer(*args, **kwargs):
    sentence = Element("id-kata").value
    input_string = sentence.lower()+'#'
    alphabet_list = list(string.ascii_lowercase)
    state_list = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8']

    transition_table = {}

    for state in state_list:
        for alphabet in alphabet_list:
            transition_table[(state, alphabet)] = 'error'
        transition_table[(state, '#')] = 'error'
        transition_table[(state, ' ')] = 'error'

    transition_table['q0', ' '] = 'q0'

    transition_table[('q0', 'k')] = 'q1'
    transition_table[('q1', 'a')] = 'q2'
    transition_table[('q2', 'k')] = 'q3'
    transition_table[('q3', 'a')] = 'q4'
    transition_table[('q4', 'k')] = 'q7'
    transition_table[('q7', ' ')] = 'q8'
    transition_table[('q7', '#')] = 'accept'
    transition_table[('q8', ' ')] = 'q8'
    transition_table[('q8', '#')] = 'accept'

    transition_table[('q8', 'k')] = 'q1'
    transition_table[('q8', 'a')] = 'q5'

    transition_table[('q0', 'a')] = 'q5'
    transition_table[('q5', 'd')] = 'q6'
    transition_table[('q6', 'i')] = 'q4'
    transition_table[('q4', 'k')] = 'q7'

    idx_char = 0
    state = 'q0'
    current_token = ''
    while state != 'accept':
        current_char = input_string[idx_char]
        current_token += current_char
        state = transition_table[(state, current_char)]
        if state == 'q7':
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