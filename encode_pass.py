def encode_pass(input_sentence):
    input_sentence = input_sentence.lower()
    output_code = ""
    for letter in input_sentence:
        if letter == "0":
            output_code = output_code + "q"
        elif letter == "1":
            output_code = output_code + "d"
        elif letter == "2":
            output_code = output_code + "h"
        elif letter == "3":
            output_code = output_code + "u"
        elif letter == "4":
            output_code = output_code + "l"
        elif letter == "5":
            output_code = output_code + "v"
        elif letter == "6":
            output_code = output_code + "y"
        elif letter == "7":
            output_code = output_code + "z"
        elif letter == "8":
            output_code = output_code + "e"
        elif letter == "9":
            output_code = output_code + "r"
    return output_code