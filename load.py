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

# Keywords for deciding whether to use Wikipedia
wikipedia_keywords = ["who", "where", "why", "what"]

while True:
    # Accept user input for the prompt
    user_input = input("You: ").lower()

    # Check if the user input contains any Wikipedia keywords
    use_wikipedia = any(keyword in user_input for keyword in wikipedia_keywords)

    # Remove specific question words
    question_words = ["who is", "where is", "why is", "what was", "what is"]
    for word in question_words:
        user_input = user_input.replace(word, "").strip()

    # Check if the user input is empty after removing question words
    if not user_input:
        print("AI: Please provide a valid input.")
        continue

    # Check if Wikipedia should be used and if an exact match is found in the model's responses
    if use_wikipedia:
        try:
            wikipedia_summary = wikipedia.summary(user_input, sentences=1)
            generated_text = wikipedia_summary
        except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e:
            generated_text = "Wikipedia data not available. Generating response using model."
    else:
        # Generate a single response based on the user's input without using Wikipedia
        generated_text = gpt2.generate(sess, model_name=model_name, checkpoint_dir=checkpoint_dir, prefix=user_input, nsamples=1, batch_size=1, length=100, temperature=0.7, return_as_list=True)[0]

    # Extract the text up to the first
