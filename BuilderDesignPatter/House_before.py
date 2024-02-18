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

Builderhouse=Housebuilder()
House1=Builderhouse.SetStories(1)
House1.Setdoors("single").Setroof("pointy")
