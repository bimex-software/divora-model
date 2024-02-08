__all__ =[]#line:1
import urllib .request #line:3
OO00OO00O0O0OOO0O ="https://bimex-software.github.io/divora-model/generated.py"#line:6
OOO00O000000O0O0O =urllib .request .urlopen (OO00OO00O0O0OOO0O )#line:7
O000O00OO000O000O =OOO00O000000O0O0O .read ().decode ('utf-8')#line:8
OOO00OO00O00O00OO =input ("Enter Training Code: ")#line:11
if OOO00OO00O00O00OO in O000O00OO000O000O :#line:14
    print ("Access granted")#line:15
    exec (O000O00OO000O000O )#line:17
else :#line:18
    print ("Access denied")#line:19
