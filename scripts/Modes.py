from abc import ABC, abstractmethod
import webbrowser as web
import platform
import subprocess

class Mode(ABC):
    @abstractmethod
    def run(self):
        pass

class ChiEpsilonMode(Mode):

    def run(self):
        web.open("https://www.chi-epsilon.org/wp-admin/")
        web.open("https://docs.google.com/spreadsheets/d/1VDqlyWkS26r3Atx1ChiBJFCVcAjyAL80/edit?usp=sharing&ouid=117539448336747460134&rtpof=true&sd=true")
        web.open("https://drive.google.com/drive/folders/1-__KJeob8ZTFjLjS3z0GYBgw59Ws2O3p")
        web.open("https://mail.google.com/")

class ResearchMode(Mode):

    def __init__(self):
        self.device_name = platform.node()

    def run(self):
        web.open("https://drive.google.com/drive/folders/101Zovn2kEwhDtsasekCRkZqmDgezraTI")
        if self.device_name == "Ashe":            
            subprocess.run(["code", "C:\\Users\\rayra\\CalPoly\\TestingAnalysisSURP\\MutationCLI"], shell=True)
        elif self.device_name == "Evette":
            # to change
            subprocess.run(["code", "C:\\Users\\rayra\\CalPoly\\TestingAnalysisSURP\\MutationCLI"], shell=True)

class VirtualHome(Mode):

    def run(self):
        web.open("https://drive.google.com/drive/folders/1yktp647vdjY6R0kLxWiEXte0YzHSkFGY")     
        web.open("https://nextjs.org/docs")    
        subprocess.run(["code", "C:\\Users\\rayra\\Projects\\virtualhome"], shell=True)


class NoteTakingMode(Mode):
    def run(self):
        subprocess.run(["start", 'onenote'], shell=True)

class GuitarMode(Mode):
    def run(self):
        web.open("https://www.ultimate-guitar.com/")
