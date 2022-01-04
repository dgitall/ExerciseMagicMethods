import csv

## Part 2
class Astronaut:
    """Astronaut Class"""
    
    def __init__(self, name, status, flighthrs, year=None, group=None, BirthDate=None, BirthPlace=None, Gender=None, 
                 almamater=None, undergradmajor=None, gradmajor=None, militaryrank=None, 
                 militarybranch=None, spacefight=None, spacewalks=None, spacewalkhrs=None, 
                 missions=None, deathdate=None, deathmission=None):
        self.__Name = name
        self.__Year = year
        self.__Group = group
        self.__Status = status
        self.__BirthDate = BirthDate
        self.__BirthPlace = BirthPlace
        self.__Gender = Gender
        self.__AlmaMater = almamater
        self.__UndergraduateMajor = undergradmajor
        self.__GraduateMajor = gradmajor
        self.__MilitaryRank = militaryrank
        self.__MilitaryBranch = militarybranch
        self.__SpaceFlights = spacefight
        self.__SpaceFlightHrs = flighthrs
        self.__SpaceWalks = spacewalks
        self.__SpaceWalkHrs = spacewalkhrs
        self.__Missions = missions
        self.__DeathDate = deathdate
        self.__DeathMission = deathmission

        
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name):
        self.__Name = Name
        
    @property
    def SpaceFlightHrs(self):
        return self.__SpaceFlightHrs
    @SpaceFlightHrs.setter
    def SpaceFlightHrs(self, flighthrs):
        self.__SpaceFlightHrs = flighthrs
    
    @property
    def Year(self):
        return self.__Year

    @Year.setter
    def Year(self, Year):
        self.__Year = Year
        
    @property
    def Group(self):
        return self.__Group
    @Group.setter
    def Group(self, Groupv):
        self.__Group = Group

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, Status):
        self.__Status = Status

    @property
    def BirthDate(self):
        return self.__BirthDate
    @BirthDate.setter
    def BirthDate(self, BirthDate):
        self.__BirthDate = BirthDate
 
    @property
    def BirthPlace(self):
        return self.__BirthPlace

    @BirthPlace.setter
    def BirthPlace(self, BirthPlace):
        self.__BirthPlace = BirthPlace
     
    @property
    def Gender(self):
        return self.__Gender

    @Gender.setter
    def Gender(self, Gender):
        self.__Gender = Gender
        
    @property
    def AlmaMater(self):
        return self.__AlmaMater
    @AlmaMater.setter
    def AlmaMater(self, AlmaMater):
        self.__AlmaMater = AlmaMater

    @property
    def UndergraduateMajor(self):
        return self.__UndergraduateMajor

    @UndergraduateMajor.setter
    def UndergraduateMajor(self, UndergraduateMajor):
        self.__UndergraduateMajor = UndergraduateMajor
            
    @property
    def GraduateMajor(self):
        return self.__GraduateMajor

    @GraduateMajor.setter
    def GraduateMajor(self, GraduateMajor):
        self.__GraduateMajor = GraduateMajor
            
    @property
    def MilitaryRank(self):
        return self.__MilitaryRank

    @MilitaryRank.setter
    def MilitaryRank(self, MilitaryRank):
        self.__MilitaryRank = MilitaryRank
            
    @property
    def MilitaryBranch(self):
        return self.__MilitaryBranch

    @MilitaryBranch.setter
    def MilitaryBranch(self, MilitaryBranch):
        self.__MilitaryBranch = MilitaryBranch
            
    @property
    def SpaceFlights(self):
        return self.__SpaceFlights

    @SpaceFlights.setter
    def SpaceFlights(self, SpaceFlights):
        self.__SpaceFlights = SpaceFlights
            
    @property
    def SpaceWalks(self):
        return self.__SpaceWalks

    @SpaceWalks.setter
    def SpaceWalks(self, SpaceWalks):
        self.__SpaceWalks = SpaceWalks
            
    @property
    def SpaceWalkHrs(self):
        return self.__SpaceWalkHrs

    @SpaceWalkHrs.setter
    def SpaceWalkHrs(self, SpaceWalkHrs):
        self.__SpaceWalkHrs = SpaceWalkHrs
            
    @property
    def Missions(self):
        return self.__Missions

    @Missions.setter
    def Missions(self, Missions):
        self.__Missions = Missions
            
    @property
    def DeathDate(self):
        return self.__DeathDate

    @DeathDate.setter
    def DeathDate(self, DeathDate):
        self.__DeathDate = DeathDate
            
    @property
    def DeathMission(self):
        return self.__DeathMission

    @DeathMission.setter
    def DeathMission(self, DeathMission):
        self.__DeathMission = DeathMission
    
    def __gt__(self, other):
        return self.__SpaceFlightHrs > other.__SpaceFlightHrs

    def __ge__(self, other):
        return self.__SpaceFlightHrs >= other.__SpaceFlightHrs
    
    def __eq__(self, other):
        return self.__SpaceFlightHrs == other.__SpaceFlightHrs
            
    def __str__(self):
        return self.__Name + ", " + self.Status

## Part 3
# create a function to find an astronaut in the list by Name
def findAstronaut(data, name):
    for astronaut in data:
        if astronaut.Name == name:
            return astronaut
        
 
# Read in the file and pass in just the required values to create a list of astronauts
data = list()
with open("astronauts.csv", "r", newline='', encoding="utf-8") as csvfile:
    for line in csv.DictReader(csvfile):
        astronaut = Astronaut(line['Name'], line['Status'], line['Space Flight (hr)'])
        data.append(astronaut)

## Test the comparison and __str__ functions
astronaut1 = findAstronaut(data, 'Joseph M. Acaba')
astronaut2 = findAstronaut(data, 'Loren W. Acton')
print(f"{astronaut1} > {astronaut2} : {astronaut1 > astronaut2}")

## Print out all of the astronauts in the list
for astronaut in data:
    print(astronaut)