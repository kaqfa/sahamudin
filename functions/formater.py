import math

def millify(n):
    millnames = ['',' R',' J',' M',' T']
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.3f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def periode(laporan):
    if laporan.periodType == '12M':
        return laporan.asOfDate.strftime('%Y')
    else:
        return 'TTM'