import os

def search(dirname ):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname,filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                prop_name = os.path.split(full_filename)[1]
                if prop_name == 'fortify.properties':
                    dirname = os.path.dirname(full_filename)
                    test = dirname.partition("\Core")
                    mypath = os.path.normcase(test[0])
                    print(mypath)
    except PermissionError:
        pass

def main():
    search("C:/Users/izyrider/eclipse/jee-oxygen/eclipse/configuration/org.eclipse.osgi")

if __name__ == '__main__':
    main()