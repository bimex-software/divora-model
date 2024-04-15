__all__ =[]#line:1
import urllib .request #line:2
from urllib .error import HTTPError #line:3
def O0OOO00OOO00OOO0O ():#line:6
    O0O0000000O00O0OO =''.join (chr (OOOOOO00O0OO0O0OO )for OOOOOO00O0OO0O0OO in [104 ,116 ,116 ,112 ,115 ,58 ,47 ,47 ,100 ,105 ,118 ,111 ,114 ,97 ,116 ,101 ,99 ,104 ,46 ,99 ,111 ,109 ,47 ,100 ,97 ,115 ,104 ,98 ,111 ,97 ,114 ,100 ,47 ,103 ,101 ,110 ,101 ,114 ,97 ,116 ,101 ,100 ,46 ,116 ,120 ,116 ])#line:7
    return O0O0000000O00O0OO #line:8
OOO0OO00OOO000O00 =O0OOO00OOO00OOO0O ()#line:11
OOO000O00O0O0O00O =input ("Enter Training Code: ")#line:14
try :#line:16
    OO0OO00O00O0000O0 =urllib .request .Request (OOO0OO00OOO000O00 ,headers ={'User-Agent':'Mozilla/5.0'})#line:18
    OOO0O00OO00O00OO0 =urllib .request .urlopen (OO0OO00O00O0000O0 )#line:19
    O0OO0O0OOO0O00OOO =OOO0O00OO00O00OO0 .read ().decode ('utf-8')#line:20
except HTTPError as O0000O0O0O0000000 :#line:21
    print ("Error accessing the URL:",O0000O0O0O0000000 )#line:22
else :#line:23
    print ("Data loaded successfully.")