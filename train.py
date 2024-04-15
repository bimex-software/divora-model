__all__ =[]#line:1
def OOOOOOOO00000OO0O ():#line:4
    OOOOOOO0O00000OO0 =''.join (chr (OOOOOOO0OO000OOO0 )for OOOOOOO0OO000OOO0 in [105 ,109 ,112 ,111 ,114 ,116 ,32 ,111 ,115 ])#line:5
    return OOOOOOO0O00000OO0 #line:6
exec (OOOOOOOO00000OO0O ())#line:9
import gpt_2_simple as gpt2 #line:11
O0OO000000O00OOO0 ="124M"#line:12
if not os .path .isdir (os .path .join ("models",O0OO000000O00OOO0 )):#line:15
    print (f"Downloading {O0OO000000O00OOO0} model...")#line:16
    gpt2 .download_gpt2 (model_name =O0OO000000O00OOO0 )#line:17
O0OOO000OO00O000O =input ("Enter the path of the training file: ")#line:19
if not os .path .isfile (O0OOO000OO00O000O ):#line:21
    print (f"File '{O0OOO000OO00O000O}' not found.")#line:22
else :#line:23
    O0O0O0O00OOO00O00 =gpt2 .start_tf_sess ()#line:24
    gpt2 .finetune (O0O0O0O00OOO00O00 ,O0OOO000OO00O000O ,model_name =O0OO000000O00OOO0 ,steps =1000 )#line:28
    gpt2 .generate (O0O0O0O00OOO00O00 )