import os
def indexer():
    path = os.getcwd()
    for dir, subdir, file in os.walk(path):
        os.chdir(dir)
        for x in os.listdir():
            if x.endswith(".md"):
                directory = os.getcwd().split('\\')[-1]
                if x.split('.')[0] == directory:
                    os.rename(x, "_index.md")
indexer()