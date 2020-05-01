# Tema6 - 30% din nota finala
# Creati o clasa care se intantiaza cu o lista de cai de fisiere
# Clasa va avea o metoda create_ordered_log ce va sorta fiecare linie din fisiere pe baza primului cuvant
# Primul cuvant reprezinta data scrisa in formatul UNIX si este un numar
# Fisierele se gasesc in repo.

import os
import sys
import datetime

class LogSorter():

    def __init__(self, files: list):
        self.files = []
        self.logs = []

        for file in files:
            file += '.log'
            sys.path.append(os.path.abspath(file))
            path = os.path.join(os.path.dirname(__file__), file)
            self.files.append(path)

            file = open(file, 'rt', encoding='utf-8')
            for log in file.readlines():
                if '\n' in log:
                    log = log[0:-1]
                self.logs.append(log)
            file.close()
    def getTime(self , date ):
        result = datetime.datetime.fromtimestamp(int(date[0:10])).strftime('%Y-%m-%d %H:%M:%S')
        return result

    def create_ordered_log(self, output_file: str):
        orderedlog = []

        for log in self.logs:
            time = self.getTime(log)
            contor = 0

            while contor != len(self.logs):
                try:
                    if self.getTime(orderedlog[contor]) >= time:
                        orderedlog.insert(contor,log)
                        break
                except IndexError:
                    orderedlog.append(log)
                    contor-=1
                    break
                contor += 1

        output = open(output_file, 'wt')
        for line in orderedlog:
            output.write(line)
            output.write('\n')
        output.close()

        return output


log_sorter = LogSorter(['log1', 'log2'])
log_sorter.create_ordered_log('sortate.log')