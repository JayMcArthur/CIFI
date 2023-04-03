
class Boost:
    def __init__(self, cell=1.0, mk1=1.0, mk2=1.0, mk3=1.0, mk4=1.0, mk5=1.0, mk6=1.0, mk7=1.0, mk8=1.0, mods=1.0, shards=1.0, rp=1.0, ap=1.0, tokens=0.0):
        self.__Cell = cell
        self.__MK1 = mk1
        self.__MK2 = mk2
        self.__MK3 = mk3
        self.__MK4 = mk4
        self.__MK5 = mk5
        self.__MK6 = mk6
        self.__MK7 = mk7
        self.__MK8 = mk8
        self.__Mods = mods
        self.__Shards = shards
        self.__ResearchPoints = rp
        self.__AcademyPoints = ap
        self.__Tokens = tokens

    def get_boost(self, type, level):
        return pow(self.string_to_var(type), level)

    def string_to_var(self, string):
        if string == 'MK1':
            return self.__MK1
        elif string == 'MK2':
            return self.__MK2
        elif string == 'MK3':
            return self.__MK3
        elif string == 'MK4':
            return self.__MK4
        elif string == 'MK5':
            return self.__MK5
        elif string == 'MK6':
            return self.__MK6
        elif string == 'MK7':
            return self.__MK7
        elif string == 'MK8':
            return self.__MK8
        elif string == 'Mods':
            return self.__Mods
        elif string == 'Shards':
            return self.__Shards
        elif string == 'RP':
            return self.__ResearchPoints
        elif string == 'AP':
            return self.__AcademyPoints
        elif string == 'Tokens':
            return self.__Tokens

# Old Useful functions

#    def get_cell_final(self):
#        return self.__Cell * self.__MK1 * self.__MK2 * self.__MK3 * self.__MK4 * self.__MK5 * self.__MK6 * self.__MK7 * self.__MK8

#   def get_total_power(self, boost):
#       tp = pow(boost.get_cell_final(), self.priorities['Cells'])
#       tp *= pow(boost.get_boost('Mods', 1), self.priorities['Mods'])
#       tp *= pow(boost.get_boost('Shards', 1), self.priorities['Shards'])
#       tp *= pow(boost.get_boost('RP', 1), self.priorities['RP'])
#       tp *= pow(boost.get_boost('AP', 1), self.priorities['AP'])
#       return tp + boost.string_to_var('Token')

#   def get_total_hardware(self):
#       total = 0
#       for key, data in self.tech.items():
#           total += data["Hardware"]
#       return total

#   def get_total_software(self):
#       total = 0
#       for key, data in self.tech.items():
#           total += data["Software"]
#       return total

#  def calculate_expected(self, time):
# TODO - Using Time calculate how many Studies, Operations, and Missions you would complete
#      return time
