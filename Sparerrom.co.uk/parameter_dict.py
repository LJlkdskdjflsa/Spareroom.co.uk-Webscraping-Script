
class Parameters:

    def __init__(self,file):
        self.file=file
        self.parameter_dct = {}

        with open(self.file,'r') as open_file:

            for line in open_file:

                line = line.split('=')
                line = [word.strip() for word in line]
                line = [word.replace("'","") for word in line]
                self.parameter_dct[line[0]] = line[1]

    def postcode(self):
        return self.parameter_dct['postcode']


