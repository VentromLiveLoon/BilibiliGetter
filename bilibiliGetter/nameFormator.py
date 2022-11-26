

def nameFormator(name):
    name=name.replace(' ','');
    name=name.replace(':', '');
    name=name.replace('\\', '');
    name=name.replace('/', '');
    name=name.replace('~', '');
    name=name.replace('.', '');
    name=name.replace('*', '');
    name=name.replace('/', '');
    name=name.replace('$', '');
    name=name.replace('^', '');
    name=name.replace('&', '');
    name=name.replace(')', '');
    name=name.replace('(', '');
    name=name.replace('[', '');
    name=name.replace(']', '');
    name=name.replace('{', '');
    name=name.replace('}', '');
    name=name.replace('|', '');
    name=name.replace('\'', '');
    name=name.replace('\"', '');

    return name;
