import os


def save_names(name_files):
    with open('name_files.txt', 'w') as fichero:
        for name in name_files:
            fichero.write('{0}\n'.format(name))

def search_names(name_files):
    
    for root, dirs, files in os.walk(".", topdown=False):
        
        for name in files:
            text = name.split('.')
            print(name)
            if 'txt' in name:
                name_files.append(name)

    return name_files

        
