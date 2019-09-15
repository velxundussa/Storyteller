import pprint
import re


def get_empty_charm(section):
    return {
        'section': section,
        'description': '',
        'whole_string': '',
    }

def clean_charm(charm):
    # For common rules appearing often.
    rules = {
        'Refl exive': 'Reflexive',
        '\xe2\x80\x99': "'"
    }

    for k, v in charm.items():
        cvalue = v
        for search, replace in rules.items():
            cvalue = cvalue.replace(search, replace)

        cvalue = cvalue.rstrip()
        charm[k] = cleanup_line(cvalue)

    return charm

def cleanup_line(line):
    try:
        last_char = None
        last_last_char = None
        new_line = ''
        for c in line:
            if not (c == ' ' and (last_last_char in (' ', '-', '(', ')', '\n') or last_last_char is None )):
                if c in ('-', "’", ')', '+'):
                    if new_line[-1:] == ' ':
                        new_line = new_line[:-1]

                new_line += c
                if c in (')',):
                    new_line += ' '

                last_last_char = last_char
                last_char = c

        return new_line
    except:
        pass

def read_2e_charms_from_string(read_string):
    previous_line_type = 'description'
    current_charm = get_empty_charm('')
    current_section = ''
    charms = []
    for line in read_string:
        # If all uppercase, we're dealing with either a title, or a section
        is_upper = (not any(c.islower() for c in line)) and (not line[0].isdigit())

        if is_upper:
            if previous_line_type == 'title':
                current_charm['section'] = current_charm['title']
                current_section = current_charm['title']
            else:
                charms.append(clean_charm(current_charm))
                current_charm = get_empty_charm(current_section)

            current_charm['title'] = line
            previous_line_type = 'title'
        elif previous_line_type == 'title':
            current_charm['prerequisites'] = line
            previous_line_type = 'prerequisites'
        elif 'Type: ' in line:
            current_charm['charm_type'] = line
        elif 'Keywords: ' in line:
            current_charm['keywords'] = line
        elif 'Duration: ' in line:
            current_charm['duration'] = line
        else:
            current_charm['description'] += line
            previous_line_type = 'description'

        current_charm['whole_string'] += line

    charms.append(clean_charm(current_charm))

    return charms

if __name__ == '__main__':
    f = open('data/lunar_charms.txt', 'r')
    charms = read_2e_charms_from_string(f)

    pp = pprint.PrettyPrinter()
    pp.pprint(charms)
