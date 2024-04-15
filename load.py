import subprocess
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import gpt_2_simple as gpt2
from gtts import gTTS
from IPython.display import display, Audio

# Install gpt_2_simple if not already installed
command = "pip install gpt_2_simple"
subprocess.run(command, shell=True)

# Define the model name and your custom checkpoint directory
model_name = "124M"
checkpoint_dir = "models"  # Use the default directory structure

# Reset the TensorFlow graph and session
tf.reset_default_graph()
sess = gpt2.start_tf_sess()

# Load your custom fine-tuned model from the specified checkpoint directory
gpt2.load_gpt2(sess, model_name=model_name, checkpoint_dir=checkpoint_dir)

while True:
    # Accept user input for the prompt
    user_input = input("You: ")

    # Generate a single response based on the user's input
    generated_text = gpt2.generate(
        sess,
        model_name=model_name,
        checkpoint_dir=checkpoint_dir,
        prefix=user_input,
        nsamples=1,
        batch_size=1,
        length=100,
        temperature=0.7,
        return_as_list=True
    )[0]

    # Extract the text up to the first period
    first_period_index = generated_text.find('.')
    if first_period_index != -1:
        generated_text = generated_text[:first_period_index + 1]

    # Print the generated text
    print("AI:", generated_text)

    # Convert the generated text to speech and play it
    tts = gTTS(text=generated_text, lang='en', slow=False)
    tts.save("output.mp3")
    display(Audio("output.mp3", autoplay=True))
