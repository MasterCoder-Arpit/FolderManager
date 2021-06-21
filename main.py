import os


def createifnotexists(folder, ext):  # To create a folder if it does not exists
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):  # To move all contents to respected folder
    for file in files:
        os.replace(file, f"{foldername}/{file}")


files = os.listdir()
files.remove("main.py")
print("Contents In our file are: ", files)


imgext = [".png", ".jpg", "jpeg", "ico"]
images = [file for file in files if os.path.splitext(file)[
    1].lower() in imgext]


docext = [".docx", ".pdf", ".doc", ".txt", ".ppt", ".xls"]
docs = [file for file in files if os.path.splitext(file)[
    1].lower() in docext]


mediaext = [".mp3", ".mp4", ".wav"]
media = [file for file in files if os.path.splitext(file)[
    1].lower() in mediaext]


styleext = [".css", ".scss"]
style = [file for file in files if os.path.splitext(file)[
    1].lower() in styleext]


jsext = [".js"]
js = [file for file in files if os.path.splitext(file)[
    1].lower() in jsext]


others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgext) and (ext not in docext) and (ext not in mediaext) and (ext not in styleext) and (ext not in jsext) and os.path.isfile(file):
        others.append(file)


# Creates Directory if it Does not Exists
createifnotexists('Images', imgext)
createifnotexists('Docs', docext)
createifnotexists('Media', mediaext)
createifnotexists('Css', styleext)
createifnotexists('Js', jsext)
createifnotexists('Others', others)

# Moves the files
move("Images", images)
move("Docs", docs)
move("Media", media)
move("Css", style)
move("Js", js)
move("Others", others)
