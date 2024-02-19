class kannadaTransalator:
    def __init__(self):
        #self.translator={"Hi":"Namaste","welcome":"swagatha"}
        self.translator = {"Hi": "Namaste", "Welcome": "Swagatha"}

    def localize(self,msg):
        return self.translator.get(msg, msg)

class EnglishTransalator:
  def localize(self, msg):
        return msg

if __name__=="__main__":
    kannada=kannadaTransalator()
    English=EnglishTransalator()

    msg=["Hi","Welcome"]
    for i in msg:
        print(kannada.localize(i))
        print(English.localize(i))
    
