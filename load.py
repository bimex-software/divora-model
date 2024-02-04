__all__ =[]#line:1
import subprocess #line:2
import tensorflow .compat .v1 as tf #line:3
tf .disable_v2_behavior ()#line:4
import gpt_2_simple as gpt2 #line:5
O000O00OO0OO000OO ="pip install gpt_2_simple"#line:8
subprocess .run (O000O00OO0OO000OO ,shell =True )#line:9
O000OO0OOO0O0OO00 ="124M"#line:12
O0OO0O00OO000OO00 ="models"#line:13
tf .reset_default_graph ()#line:16
O0000OOO0OO0O0OOO =gpt2 .start_tf_sess ()#line:17
gpt2 .load_gpt2 (O0000OOO0OO0O0OOO ,model_name =O000OO0OOO0O0OO00 ,checkpoint_dir =O0OO0O00OO000OO00 )#line:20
while True :#line:22
    O0OO0O000OO0O0OO0 =input ("You: ")#line:24
    O0OO0O0O00O0OO000 =gpt2 .generate (O0000OOO0OO0O0OOO ,model_name =O000OO0OOO0O0OO00 ,checkpoint_dir =O0OO0O00OO000OO00 ,prefix =O0OO0O000OO0O0OO0 ,nsamples =1 ,batch_size =1 ,length =50 ,temperature =0.7 ,return_as_list =True )[0 ]#line:27
    OOOOO0O00000OO00O =O0OO0O0O00O0OO000 .find ('.')#line:30
    if OOOOO0O00000OO00O !=-1 :#line:31
        O0OO0O0O00O0OO000 =O0OO0O0O00O0OO000 [:OOOOO0O00000OO00O +1 ]#line:32
    print ("AI:",O0OO0O0O00O0OO000 )



