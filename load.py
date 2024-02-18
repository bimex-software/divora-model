Understood. To ensure the code only utilizes Wikipedia when specific keywords are present in the user input, and only if it can't find a suitable answer from Wikipedia or the user input itself, you need to refine the logic. Here's the updated code:

```python
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
    question_words = ["who is", "where was", "why was", "what does", "what is", "what"]
    for word in question_words:
        user_input = user_input.replace(word, "").strip()

    # Check if the user input is empty after removing question words
    if not user_input:
        print("AI: Please provide a valid input.")
        continue

    # Check if the user input exactly matches a Wikipedia page and if Wikipedia should be used
    if use_wikipedia:
        try:
            wikipedia_summary = wikipedia.summary(user_input, sentences=1)
            generated_text = "According to Wikipedia, " + wikipedia_summary

            # Check if the generated Wikipedia summary exactly matches the user input
            if user_input.lower() in wikipedia_summary.lower():
                # Generate a single response based on the user's input
                generated_text = gpt2.generate(sess, model_name=model_name, checkpoint_dir=checkpoint_dir, prefix=user_input, nsamples=1, batch_size=1, length=100, temperature=0.7, return_as_list=True)[0]
            else:
                generated_text = "Wikipedia data found but not exact. Generating response using model."

        except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.PageError) as e:
            generated_text = "No suitable Wikipedia data found. Generating response using model."

    else:
        # Generate a single response based on the user's input without using Wikipedia
        generated_text = gpt2.generate(sess, model_name=model_name, checkpoint_dir=checkpoint_dir, prefix=user_input, nsamples=1, batch_size=1, length=100, temperature=0.7, return_as_list=True)[0]

    # Extract the text up to the first period
    first_period_index = generated_text.find('.')
    if first_period_index != -1:
        generated_text = generated_text[:first_period_index + 1]

    # Print the generated text
    print("AI:", generated_text)
```

This code now incorporates the following logic:

- It checks if the user input contains any keywords from the list. If it does, it considers using Wikipedia.
- If Wikipedia is deemed suitable based on the keywords, it attempts to fetch a summary. If an exact match is found, it uses the Wikipedia summary; otherwise, it generates a response using the GPT-2 model.
- If the user input doesn't contain relevant keywords or if Wikipedia doesn't provide a suitable response, it generates a response solely using the GPT-2 model.
