def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]),int(t[1]),int(t[2])

def hms2str(h,m,s):
    return ('0'+str(h))[-2:] + ':' + \
        ('0'+str(m))[-2:] + ':' + \
        ('0'+str(s))[-2:]

def to_sec(h,m,s):
    t = (h*60*60)+(m*60)+s
    return t

def to_hms(s):
    h = s // (60*60)
    m = (s - (h * (60*60))) // 60
    s = s - (h * (60*60)) - (m * 60)
    return h,m,s

def diff(h1,m1,s1,h2,m2,s2):
    t1 = to_sec(h1,m1,s1)
    t2 = to_sec(h2,m2,s2)
    tt = t2 - t1
    return to_hms(tt)

def main():
    hms_start = str2hms(input())
    hms_end = str2hms(input())
    
    result = to_sec(hms_end[0],hms_end[1],hms_end[2]) - to_sec(hms_start[0],hms_start[1],hms_start[2])
    x = to_hms(result)
    print(hms2str(x[0],x[1],x[2]))

exec(input()) # DON'T remove this line