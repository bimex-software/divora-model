import subprocess
import tensorflow.compat.v1 as tf
import gpt_2_simple as gpt2
import wikipedia

# Install gpt_2_simple and wikipedia if not already installed
subprocess.run("pip install gpt_2_simple wikipedia", shell=True)

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
    user_input = input("You: ").lower()

    # Remove specific question words
    question_words = ["who is", "where was", "why was", "what does", "what is", "what"]
    for word in question_words:
        user_input = user_input.replace(word, "").strip()

    # Check if the user input is empty after removing question words
    if not user_input:
        print("AI: Please provide a valid input.")
        continue

    # Try to get Wikipedia summary based on user input
    try:
        wikipedia_summary = wikipedia.summary(user_input, sentences=1)
        generated_text = "According to Wikipedia, " + wikipedia_summary

        # Generate a single response based on the Wikipedia summary
        generated_text = gpt2.generate(sess, model_name=model_name, checkpoint_dir=checkpoint_dir, prefix=generated_text, nsamples=1, batch_size=1, length=100, temperature=0.7, return_as_list=True)[0]
    except wikipedia.exceptions.DisambiguationError as e:
        generated_text = "There are multiple options. Please be more specific."
    except wikipedia.exceptions.PageError as e:
        generated_text = "Sorry, I couldn't find information on that."

    # Extract the text up to the first period
    first_period_index = generated_text.find('.')
    if first_period_index != -1:
        generated_text = generated_text[:first_period_index + 1]

    # Print the generated text
    print("AI:", generated_text)
