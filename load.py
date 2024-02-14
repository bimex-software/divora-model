import subprocess
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import gpt_2_simple as gpt2
import wikipedia

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

    # Search for relevant Wikipedia information based on the user's input
    try:
        wikipedia_response = wikipedia.summary(user_input, sentences=3)
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple options, choose the first one
        wikipedia_response = wikipedia.summary(e.options[0], sentences=3)
    except wikipedia.exceptions.PageError:
        # If no page matches the query, return a generic response
        wikipedia_response = "I couldn't find relevant information on Wikipedia."

    # Generate a response based on the combined input of user query and Wikipedia information
    combined_input = user_input + " " + wikipedia_response
    generated_text = gpt2.generate(
        sess,
        model_name=model_name,
        checkpoint_dir=checkpoint_dir,
        prefix=combined_input,
        nsamples=1,
        batch_size=1,
        length=150,
        temperature=0.7,
        return_as_list=True
    )[0]

    # Print the generated response
    print("AI:", generated_text)


