import re


# TODO: 兩個字的case

class lyric:
    def __init__(self,file):
        with open(file,'r') as f:
            self.text = f.read()
        self.seq = self._parse(self.text)



    def get_lyric(self):
        return

    def _parse(self,text):
        """

        :param text:
        :return: list
                    a list of tuple(start_time(ms),duration(ms),char)
                    ex.[(1329, 1700, '小'), (3029, 601, '幸'), (3630, 1003, '運')]

        """

        lines = text.splitlines()
        seq = []
        time_offset = 0

        pat_string = re.compile("\[.+,.+\]")
        pat_char = re.compile("<\d+,\d+,\d+>.")

        for line in lines:
            try:
                time_string = re.findall(pat_string, line)[0]
                time_string = time_string.replace('[','').replace(']','')
                start, end = time_string.split(',')
                start = int(start)
                end = int(start)
                # print(start,end)
                time_offset = start
            except IndexError:
                pass

            try:
                time_char = re.findall(pat_char, line)
                for char in time_char:
                    char = char.replace('<','').replace('>',',')
                    start2, duration, track, char = char.split(',')
                    start2 = int(start2)+time_offset
                    duration = int(duration)
                    # time_offset += duration
                    seq.append((start2, duration, char))


            except IndexError:
                pass


        return seq

    def get_time_before_vocal(self):
        return self.seq[23][0]



l = lyric("test_data/lyric.txt")