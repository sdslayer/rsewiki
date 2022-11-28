from github import Github

g = Github("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")
repo = g.get_repo("sdslayer100/rsewiki")
contents = repo.get_contents("section01")
articles = []
for file in contents:
    fname = file.name
    stripname = fname.strip(".html")
    if stripname.isnumeric() == True and stripname.isnumeric() != "404":
        print(f"{stripname}.html")