import os
import gpt_2_simple as gpt2
model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)

file_path = input("Enter the path of the training file: ")

if not os.path.isfile(file_path):
    print(f"File '{file_path}' not found.")
else:
    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess,
                  file_path,
                  model_name=model_name,
                  steps=1000)
    gpt2.generate(sess)


