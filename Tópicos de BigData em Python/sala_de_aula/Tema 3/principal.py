from mrjob.job import MRJob
import re

palavra_regex: re.Pattern[str] = re.compile(r'\w+')


class QuantidadePalavras(MRJob):
    def mapper(self, _, line: str):
        for p in palavra_regex.findall(line):
            yield (p.lower(), 1)
            
    def reducer(self, p: str, qtd: int):
        yield (p, sum(qtd))
        

if __name__ == '__main__':
    QuantidadePalavras.run()