import os
import configparser
import shutil
import glob

g_RULESPATH = ''

def rulefile_copy(dest, src):
    for file in glob.glob(src):
        print(file)
        shutil.copy(file, dest)

def search(dirname ):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                prop_name = os.path.split(full_filename)[1]
                if prop_name == 'fortify.properties':
                    dirname = os.path.dirname(full_filename)
                    global g_RULESPATH
                    g_RULESPATH = os.path.normcase(dirname.partition("\Core")[0])
    except PermissionError:
        pass

def get_path_info():
    config = configparser.ConfigParser()
    config.read('FortifyAssistance.properties')
    eclipse_path = config.get('PATH_INFO', 'eclipse_path')
    rulefile_path = config.get('PATH_INFO', 'rulefile_path')
    return (eclipse_path, rulefile_path)

def main():
    (eclipse_path, rulefile_path) = get_path_info()
    search(eclipse_path)
    rulefile_path = rulefile_path + '/*.bin'
    rulefile_copy(g_RULESPATH, rulefile_path)

if __name__ == '__main__':
    main()