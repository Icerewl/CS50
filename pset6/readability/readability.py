import sys
while True:
    text = input("Text: ")

    words = 0
    letters = 0
    sentences = 0

    for i,v in enumerate(text):
        if str(v).isalpha() == True:
            letters += 1
        if v == ' ':
            words += 1
        if v == '.' or v == '!' or v == '?':
            sentences += 1

    words += 1

    L = (float(letters) / float(words)) * 100
    S = (float(sentences) / float(words)) * 100
    final = round(0.0588 * float(L) - 0.296 * float(S) - 15.8)
    #print(final)

    if final < 1:
        print("Before Grade 1")
    elif final >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {int(final)}")

    sys.exit(0)
