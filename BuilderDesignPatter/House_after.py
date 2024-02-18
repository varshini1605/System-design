class House():
  def __init__(self,builder):
    self.stories=builder.stories
    self.door=builder.door
    self.roof=builder.roof



class Housebuilder:
    def __init__(self):
        self.stories=None
        self.door=None
        self.roof=None

    def SetStories(self,stories):
        self.stories=stories
        return self
    
    def Setdoors(self,door):
        self.door=door
        return self

    def Setroof(self,roof):
        self.roof=roof
        return self

    def build():
        return House(self)

class Director:
    def __init__(self,builder):
        self.builder=builder
        
    def housetype1(self,):
        return self.builder.SetStories(1).Setdoors("single").Setroof("pointy")
        
    def housetype2(self):
        return self.builder.SetStories(2).Setdoors("double").Setroof("flat")
        
    
    

Builderhouse=Housebuilder()
director=Director(Builderhouse)

House1=director.housetype1
