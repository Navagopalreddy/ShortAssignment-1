import openai

# Set your API key directly in the code for testing
openai.api_key = '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'

def generate_json_from_resume(resume_text):
    prompt = f"""
    I have a resume text and I need you to parse it and provide the content in JSON format. 
    Here is the resume text:
    {resume_text}
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    return response.choices[0].message['content'].strip()

# Example usage
resume_text = """<Your Resume Text>"""
json_output = generate_json_from_resume(resume_text)
print(json_output)
