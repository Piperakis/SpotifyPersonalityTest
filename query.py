import ollama


def query_llama(songs_list):
    """
    Sends the user's song list to LLaMA 3.2 for analysis.
    Returns the generated personality prediction.
    """
    print("piki") #Testing
    model_name = 'llama3.2:3b'  # Adjust model name if needed
    prompt = f"""
    **Role**: You are a Music Psychologist AI trained to analyze musical preferences and correlate them with personality traits using the Big Five model and contemporary music psychology research. Keep the results concise and short and use emojis.

    **User's Top Songs**:
    {songs_list}

    **Analysis Guidelines**:
    1. **Musical Patterns Analysis**:
    - Genre distribution and tempo analysis
    - Lyrical themes (emotional vs analytical)
    - Energy level consistency
    - Era/time period preferences

    2. **Personality Inference** (Use OCEAN model framework):
    - Openness: Musical complexity preference
    - Conscientiousness: Lyrics structure analysis
    - Extraversion: Energy/danceability correlation  
    - Agreeableness: Collaborative tracks ratio
    - Neuroticism: Emotional valence patterns

    3. **Creative Presentation Requirements**:
    - Start with an eye-catching musical analogy ("Your playlist is like...")
    - Use 3-5 emojis per trait section
    - Include surprising statistical correlations
    - Add 1-2 "hidden gem" observations
    - End with 3 recommended artists they might like

    **Format**:
    💡 **Key Insight**: [Surprising observation about their music taste]
    🎭 **Personality Portrait**: [Creative description using OCEAN traits]
    🧠 **Cognitive Style**: [Information processing style based on lyrical patterns]
    ❤️ **Emotional Patterns**: [Dominant emotional themes]
    ✨ **Hidden Self**: [Contradictions/unexpected combinations in playlist]

    **Tone**: Friendly professor vibe - knowledgeable but approachable, using music metaphors rather than psychological jargon

    **Example**:
    "For someone who loves the raw energy of Arctic Monkeys but finds solace in Billie Eilish's melancholic beats, your playlist suggests..." 
    """
    
    response = ollama.chat(model=model_name, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
