__all__ =[]#line:1
import subprocess #line:3
import tensorflow .compat .v1 as tf #line:4
def OOO0O0OOOOO00O00O ():#line:7
    OOOOOOO000O000O00 =''.join (chr (OOOO0000OOOO0000O )for OOOO0000OOOO0000O in [105 ,109 ,112 ,111 ,114 ,116 ,32 ,103 ,112 ,116 ,95 ,50 ,95 ,115 ,105 ,109 ,112 ,108 ,101 ,32 ,97 ,115 ,32 ,103 ,112 ,116 ,50 ])#line:8
    return OOOOOOO000O000O00 #line:9
exec (OOO0O0OOOOO00O00O ())#line:12
OOOOO0O0OOOO00000 ="124M"#line:15
O000O0O0O00O0OO0O ="models"#line:16
tf .reset_default_graph ()#line:19
O0O0O00O00OOO000O =gpt2 .start_tf_sess ()#line:20
gpt2 .load_gpt2 (O0O0O00O00OOO000O ,model_name =OOOOO0O0OOOO00000 ,checkpoint_dir =O000O0O0O00O0OO0O )#line:23
while True :#line:25
    OO0O000000O0OOOO0 =input ("You: ")#line:27
    O00O00O00OO000OO0 =gpt2 .generate (O0O0O00O00OOO000O ,model_name =OOOOO0O0OOOO00000 ,checkpoint_dir =O000O0O0O00O0OO0O ,prefix =OO0O000000O0OOOO0 ,nsamples =1 ,batch_size =1 ,length =100 ,temperature =0.7 ,return_as_list =True )[0 ]#line:30
    O0OO000OOO0000OO0 =O00O00O00OO000OO0 .find ('.')#line:33
    if O0OO000OOO0000OO0 !=-1 :#line:34
        O00O00O00OO000OO0 =O00O00O00OO000OO0 [:O0OO000OOO0000OO0 +1 ]#line:35
    print ("AI:",O00O00O00OO000OO0 )