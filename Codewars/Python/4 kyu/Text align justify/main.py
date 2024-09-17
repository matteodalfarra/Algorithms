def justify(text, width):
    if len(text) <= width:
        return text
    words = text.split(" ")
    lines = ""
    line = ""
    for word in words:
        if len(line) + len(word) <= width:
            line += word + " "
        else:
            line = line.strip()
            if len(line) == width:
                lines += line + "\n"
            else:
                manc = width - len(line)
                spaces_count = len(line.split(" ")) - 1
                if spaces_count != 0:
                    space_word = manc // spaces_count
                    extra_spaces = manc % spaces_count

                    i = 0
                    for l in line:
                        if l == ' ':
                            line = line[0:i] + " "*space_word + line[i:]
                            i+=space_word
                            if extra_spaces > 0:
                                line = line[0:i] + " " + line[i:]
                                i+=1
                                extra_spaces-=1

                        i+=1
                lines += line + "\n"
            
            # new line
            line = word + " "
    else:
        lines += line.strip()
    return lines