

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

    def get_cell_final(self):
        return self.__Cell * self.__MK1 * self.__MK2 * self.__MK3 * self.__MK4 * self.__MK5 * self.__MK6 * self.__MK7 * self.__MK8


class Player:
    def __init__(self):
        self.player = {
            "Level": 0,
            "LP Bar": 0
        }
        self.priorities = {
            "Cells": 1,
            "Mods": 20,
            "Shards": 16,
            "RP": 10,
            "AP": 100,
            "MM": 100,
            "OP": 1000,
            "Cost Reduction": 1,
            "Rank Points": 1
        }
        self.active_play = 24
        self.diamond_shop = {
            "Generator": {
                "MK1": {
                    "Name": "MK1 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 10,
                    "Cost Scaling": 1,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk1=1.01)
                },
                "MK2": {
                    "Name": "MK2 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 20,
                    "Cost Scaling": 2,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk2=1.02)
                },
                "MK3": {
                    "Name": "MK3 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 30,
                    "Cost Scaling": 3,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk3=1.03)
                },
                "MK4": {
                    "Name": "MK4 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 40,
                    "Cost Scaling": 4,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk4=1.04)
                },
                "MK5": {
                    "Name": "MK5 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 50,
                    "Cost Scaling": 5,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk5=1.05)
                },
                "MK6": {
                    "Name": "MK6 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 60,
                    "Cost Scaling": 6,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk6=1.06)
                },
                "MK7": {
                    "Name": "MK7 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 70,
                    "Cost Scaling": 7,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk7=1.07)
                },
                "MK8": {
                    "Name": "MK8 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 80,
                    "Cost Scaling": 8,
                    "Current Level": 0,
                    "Max Level": 100,
                    "Boost": Boost(mk8=1.08)
                },
            },
            "Special": {
                "Tokens": {
                    "Name": "Token Boost",
                    "Unlocked": False,
                    "Base Cost": 100,
                    "Cost Scaling": 200,
                    "Current Level": 0,
                    "Max Level": 9,
                    "Boost": Boost(tokens=999)
                },
                "Cells": {
                    "Name": "Cell Boost",
                    "Unlocked": False,
                    "Base Cost": 200,
                    "Cost Scaling": 1,
                    "Current Level": 0,
                    "Max Level": 1000,
                    "Boost": Boost(cell=1.05)
                },
                "Mods": {
                    "Name": "Mod Point Boost",
                    "Unlocked": False,
                    "Base Cost": 300,
                    "Cost Scaling": 10,
                    "Current Level": 0,
                    "Max Level": 25,
                    "Boost": Boost(mods=1.05)
                },
                "Shards": {
                    "Name": "Shard Boost",
                    "Unlocked": False,
                    "Base Cost": 400,
                    "Cost Scaling": 20,
                    "Current Level": 0,
                    "Max Level": 25,
                    "Boost": Boost(shards=1.05)
                },
                "Research Points": {
                    "Name": "Research Boost",
                    "Unlocked": False,
                    "Base Cost": 500,
                    "Cost Scaling": 25,
                    "Current Level": 0,
                    "Max Level": 25,
                    "Boost": Boost(rp=1.05)
                },
            },
            "One-Time": {
                "Alpha": {
                    "Name": "Alpha Card",
                    "Unlocked": False,
                    "Base Cost": 1000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(cell=1.1, mk1=1.26, mk2=1.18)
                },
                "Beta": {
                    "Name": "Beta Card",
                    "Unlocked": False,
                    "Base Cost": 1000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk1=1.18, mk2=1.18, mk3=1.18)
                },
                "Ceti": {
                    "Name": "Ceti Card",
                    "Unlocked": False,
                    "Base Cost": 1000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(cell=1.12, mk3=1.16, mods=1.08)
                },
                "Delta": {
                    "Name": "Delta Card",
                    "Unlocked": False,
                    "Base Cost": 1500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(cell=1.65, mk2=1.07, mk3=1.07)
                },
                "Epsilon": {
                    "Name": "Epsilon Card",
                    "Unlocked": False,
                    "Base Cost": 1500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk1=1.26, mk2=1.26, mk4=1.22)
                },
                "Fenix": {
                    "Name": "Fenix Card",
                    "Unlocked": False,
                    "Base Cost": 1500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(cell=1.08, mk4=1.5, mods=1.07)
                },
                "Gamma": {
                    "Name": "Gamma Card",
                    "Unlocked": False,
                    "Base Cost": 2000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(cell=1.7, mk3=1.17, mk5=1.17)
                },
                "Helion": {
                    "Name": "Helion Card",
                    "Unlocked": False,
                    "Base Cost": 2000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk1=1.34, mk2=1.34, mods=1.13)
                },
                "Ixion": {
                    "Name": "Ixion Card",
                    "Unlocked": False,
                    "Base Cost": 2000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk4=1.32, mk5=1.26, mods=1.16)
                },
                "Juno": {
                    "Name": "Juno Card",
                    "Unlocked": False,
                    "Base Cost": 2500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(cell=1.6, mods=1.2, shards=1.4)
                },
                "Kappa": {
                    "Name": "Kappa Card",
                    "Unlocked": False,
                    "Base Cost": 2500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk1=1.92, mk6=1.46, mods=1.16)
                },
                "Lyra": {
                    "Name": "Lyra Card",
                    "Unlocked": False,
                    "Base Cost": 2500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk2=1.86, mk5=1.82, shards=1.2)
                },
                "Miko": {
                    "Name": "Miko Card",
                    "Unlocked": False,
                    "Base Cost": 3000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk7=2, mods=1.32, rp=1.34)
                },
                "Nora": {
                    "Name": "Nora Card",
                    "Unlocked": False,
                    "Base Cost": 3000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk6=3, mk7=3, ap=3)
                },
                "Omega": {
                    "Name": "Omega Card",
                    "Unlocked": False,
                    "Base Cost": 3000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mods=3, shards=3, ap=3)
                },
                "Pegasus": {
                    "Name": "Pegasus Card",
                    "Unlocked": False,
                    "Base Cost": 3500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(cell=3, mk8=3, rp=3)
                },
                "Qoru": {
                    "Name": "Qoru Card",
                    "Unlocked": False,
                    "Base Cost": 3500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk6=3, mk7=3, mk8=3)
                },
                "Rigel": {
                    "Name": "Rigel Card",
                    "Unlocked": False,
                    "Base Cost": 3500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(shards=3, rp=3, ap=3)
                },
                "Sigma": {
                    "Name": "Sigma Card",
                    "Unlocked": False,
                    "Base Cost": 4000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk2=2.7, mk7=2.4, mods=1.75)
                },
                "Typhon": {
                    "Name": "Typhon Card",
                    "Unlocked": False,
                    "Base Cost": 4000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk3=3.23, mk6=1.72, rp=2)
                },
                "Utopia": {
                    "Name": "Utopia Card",
                    "Unlocked": False,
                    "Base Cost": 4000,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk4=3, mk5=3, ap=3)
                },
                "Vex": {
                    "Name": "Vex Card",
                    "Unlocked": False,
                    "Base Cost": 4500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk8=3, mods=3, shards=3)
                },
                "Xeno": {
                    "Name": "Xeno Card",
                    "Unlocked": False,
                    "Base Cost": 4500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk8=3, shards=3, rp=3)
                },
                "Zion": {
                    "Name": "Zion Card",
                    "Unlocked": False,
                    "Base Cost": 4500,
                    "Cost Scaling": 0,
                    "Current Level": 0,
                    "Max Level": 1,
                    "Boost": Boost(mk8=3, shards=3, ap=3)
                },
            }
        }
        self.token_shop = {
            "Tier 1": {
                "Token": {
                    "Name": "Token Boost",
                    "Unlocked": False,
                    "Base Cost": 20,
                    "Cost Scaling": 5,
                    "Current Level": 0,
                    "Max Level": 20,
                    "Boost": Boost(tokens=999)
                },
                "Diamond": {
                    "Name": "Diamond Boost",
                    "Unlocked": False,
                    "Base Cost": 200,
                    "Cost Scaling": 300,
                    "Current Level": 0,
                    "Max Level": 2,
                    "Boost": Boost(tokens=999)
                },
                "Cells": {
                    "Name": "Cell Boost",
                    "Unlocked": False,
                    "Base Cost": 1,
                    "Cost Scaling": 0.25,
                    "Current Level": 0,
                    "Max Level": 60,
                    "Boost": Boost(tokens=999)
                },
                "Mods": {
                    "Name": "Mod Points Boost",
                    "Unlocked": False,
                    "Base Cost": 10,
                    "Cost Scaling": 2,
                    "Current Level": 0,
                    "Max Level": 200,
                    "Boost": Boost(mods=1.01)
                },
                "MK1": {
                    "Name": "MK1 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 1,
                    "Cost Scaling": 0.1,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk1=1.01)
                },
                "MK2": {
                    "Name": "MK2 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 2,
                    "Cost Scaling": 0.12,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk2=1.01)
                },
                "MK3": {
                    "Name": "MK3 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 3,
                    "Cost Scaling": 0.13,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk3=1.01)
                },
                "MK4": {
                    "Name": "MK4 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 4,
                    "Cost Scaling": 0.14,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk4=1.01)
                },
                "MK5": {
                    "Name": "MK5 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 15,
                    "Cost Scaling": 0.15,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk5=1.01)
                },
                "MK6": {
                    "Name": "MK6 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 26,
                    "Cost Scaling": 0.16,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk6=1.01)
                },
                "MK7": {
                    "Name": "MK7 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 37,
                    "Cost Scaling": 0.2,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk7=1.01)
                },
                "MK8": {
                    "Name": "MK8 Gen Boost",
                    "Unlocked": False,
                    "Base Cost": 50,
                    "Cost Scaling": 0.22,
                    "Current Level": 0,
                    "Max Level": 5000,
                    "Boost": Boost(mk8=1.01)
                }
            },
            "Tier 2": {},
            "Tier 3": {}
        }
        self.generators = {
            "MK1": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            },
            "MK2": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            },
            "MK3": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            },
            "MK4": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            },
            "MK5": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            },
            "MK6": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            },
            "MK7": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            },
            "MK8": {
                "Unlocked": False,
                "Purchased": 0,
                "Automation": False
            }
        }
        self.ships = {}  # TODO - Will have automation in here
        self.tech = {
            "MK1": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            },
            "MK2": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            },
            "MK3": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            },
            "MK4": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            },
            "MK5": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            },
            "MK6": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            },
            "MK7": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            },
            "MK8": {
                "Hardware": 0,
                "Hardware Automation": False,
                "Software": 0,
                "Software Automation": False,
            }
        }
        self.loop = {
            "Ticks in run": 10000,
            "Completed Loops": 0,
            "Loop Resets": 0,
            "Unlocked Mods": 0
        }
        self.shard = {
            "Operations Expected": 0
        }
        self.research = {
            "Studies Expected": 0,
            "Research Levels": 0,
            "Completed Researches": 0,
            "Scientist Automation": False,
            "Equipment": 0,
            "Equipment Automation": False,
            "Quantum Automation": False
        }
        self.academy = {
            "Missions Expected": 0
        }

    def get_total_power(self, boost):
        tp = pow(boost.get_cell_final(), self.priorities['Cells'])
        tp *= pow(boost.get_boost('Mods', 1), self.priorities['Mods'])
        tp *= pow(boost.get_boost('Shards', 1), self.priorities['Shards'])
        tp *= pow(boost.get_boost('RP', 1), self.priorities['RP'])
        tp *= pow(boost.get_boost('AP', 1), self.priorities['AP'])
        return tp + boost.string_to_var('Token')

    def get_total_hardware(self):
        total = 0
        for key, data in self.tech.items():
            total += data["Hardware"]
        return total

    def get_total_software(self):
        total = 0
        for key, data in self.tech.items():
            total += data["Software"]
        return total

    def calculate_expected(self, time):
        # TODO - Using Time calculate how many Studies, Operations, and Missions you would complete
        return time
