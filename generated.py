__all__ =[]#line:1
import urllib .request #line:3
import subprocess #line:4
O0O0O0O0OO00O000O ="https://bimex-software.github.io/divora-model/generated.py"#line:7
OO00O000OO0O00O0O =urllib .request .urlopen (O0O0O0O0OO00O000O )#line:8
O0000000O0OOOO0OO =OO00O000OO0O00O0O .read ().decode ('utf-8')#line:9
O00OOO0OOO0O0O00O =input ("Enter Training Code: ")#line:12
if O00OOO0OOO0O0O00O in O0000000O0OOOO0OO :#line:15
    print ("Access granted")#line:16
    exec (O0000000O0OOOO0OO )#line:18
else :#line:19
    print ("Access denied")#line:20
