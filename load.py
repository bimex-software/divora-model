__all__ =[]#line:1
import subprocess #line:3
import tensorflow .compat .v1 as tf #line:4
tf .disable_v2_behavior ()#line:5
import gpt_2_simple as gpt2 #line:6
O0O0O000OOO0000O0 ="pip install gpt_2_simple"#line:9
subprocess .run (O0O0O000OOO0000O0 ,shell =True )#line:10
O00OO0000O0000O00 ="124M"#line:13
O0O00000OOO00000O ="models"#line:14
tf .reset_default_graph ()#line:17
OOOO00OOOO00OO000 =gpt2 .start_tf_sess ()#line:18
gpt2 .load_gpt2 (OOOO00OOOO00OO000 ,model_name =O00OO0000O0000O00 ,checkpoint_dir =O0O00000OOO00000O )#line:21
while True :#line:23
    OO0O0000O000OO000 =input ("You: ")#line:25
    O000000O0O0OO0O00 =gpt2 .generate (OOOO00OOOO00OO000 ,model_name =O00OO0000O0000O00 ,checkpoint_dir =O0O00000OOO00000O ,prefix =OO0O0000O000OO000 ,nsamples =1 ,batch_size =1 ,length =100 ,temperature =0.7 ,return_as_list =True )[0 ]#line:28
    OO000O00O0O000OOO =O000000O0O0OO0O00 .find ('.')#line:31
    if OO000O00O0O000OOO !=-1 :#line:32
        O000000O0O0OO0O00 =O000000O0O0OO0O00 [:OO000O00O0O000OOO +1 ]#line:33
    print ("AI:",O000000O0O0OO0O00 )#line:36
