class kannadaTransalator:
    def __init__(self):
        #self.translator={"Hi":"Namaste","welcome":"swagatha"}
        self.translator = {"Hi": "Namaste", "Welcome": "Swagatha"}

    def localize(self,msg):
        return self.translator.get(msg, msg)

class EnglishTransalator:
  def localize(self, msg):
        return msg
        
def Factory(language="English"):
    localizers={
        "kannada":kannadaTransalator,
        "English":EnglishTransalator,
    }
    #will have a return 
    return localizers[language]()
if __name__=="__main__":
    kannada=Factory("kannada")
    English=Factory("English")

    msg=["Hi","Welcome"]
    for i in msg:
        print(kannada.localize(i))
        print(English.localize(i))
