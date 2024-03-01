__all__ =[]#line:1
import subprocess #line:2
import tensorflow .compat .v1 as tf #line:3
tf .disable_v2_behavior ()#line:4
import gpt_2_simple as gpt2 #line:5
O0OOOO0O00O000O00 ="pip install gpt_2_simple"#line:8
subprocess .run (O0OOOO0O00O000O00 ,shell =True )#line:9
OO00O0O000000OO0O ="124M"#line:12
O0000OO000O000OO0 ="models"#line:13
tf .reset_default_graph ()#line:16
O0OOOO00000O000OO =gpt2 .start_tf_sess ()#line:17
gpt2 .load_gpt2 (O0OOOO00000O000OO ,model_name =OO00O0O000000OO0O ,checkpoint_dir =O0000OO000O000OO0 )#line:20
while True :#line:22
    OOOOO0O00OO0O000O =input ("You: ")#line:24
    O000OOO00O0OO0OOO =gpt2 .generate (O0OOOO00000O000OO ,model_name =OO00O0O000000OO0O ,checkpoint_dir =O0000OO000O000OO0 ,prefix =OOOOO0O00OO0O000O ,nsamples =1 ,batch_size =1 ,length =100 ,temperature =0.7 ,return_as_list =True )[0 ]#line:27
    O00O000OO000O0OOO =O000OOO00O0OO0OOO .find ('.')#line:30
    if O00O000OO000O0OOO !=-1 :#line:31
        O000OOO00O0OO0OOO =O000OOO00O0OO0OOO [:O00O000OO000O0OOO +1 ]#line:32
    print ("AI:",O000OOO00O0OO0OOO )