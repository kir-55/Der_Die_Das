from tika import parser
import pymysql
from config import host, user, password, db_name



class PDF_words_to_db:
    global text
    #text = ""
    def PDF_text_processing(self, words_to_remove, raw):
        text = raw['content']
        text = text.replace("  ", " ")
        text = text.lower()
        def write_to_db(word):
            try:
                #connect to sqlite
                pass
            except Exception as ex:
                print("failed: ")
                print(ex)

        for word in words_to_remove:
            text = text.replace(word, "")
            text = text.replace("  ", " ")
            text = text.replace(word, "")
            text = text.replace("  ", " ")
            text = text.replace(word, "")

        words = text.split()


        write_to_db(word)
         
        text = " ".join(words)
        

def main():
    words_to_remove =["}", "{", "]", "[", "+", "=", "`", "'", "&", "\\", "|",  ";", "?", "<", ">", "/", "$", "*", "%", " – ", ",", "!", "?", "", "\n", ".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "zadanie", ":", "• ", "(", ")", "ojap", "\t", " -", "czysto", "--", "__", "<", ">", "^", "#", "więcej arkuszy znajdziesz na stronie arkuszepl", "brudnopis nie podlega ocenie", ",", "strona z", " . ", "_", "- ", "– ", "\""]
    raw = parser.from_file('Encyclopedia Of Mathematics (Science Encyclopedia) [8 MB].pdf ( PDFDrive ).pdf')

    egz = PDF_words_to_db()
    egz.PDF_text_processing(words_to_remove, raw)

if __name__ == "__main__":
    main()

