

def main():
    with open("books/frankenstein.txt") as f:
        teksts = f.read()
        lowertxt = teksts.lower()
    chardict = {}
    for char in lowertxt:
        if char not in chardict:
            tel = lowertxt.count(char)
            chardict.update({char:tel})
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for key in alpha:
        print(f"The '{key}' character was found {chardict[key]} times")
main()