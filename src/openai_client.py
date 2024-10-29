from openai import AzureOpenAI

from src.config_loader import load_config

config = load_config('../config/azure_config.json')


def init_openai_client(config):
    """Initialize Azure OpenAI client with key-based authentication."""
    return AzureOpenAI(
        azure_endpoint=config['ENDPOINT'],
        api_key=config['OPENAI_API_KEY'],
        api_version="2024-02-15-preview",
    )


def call_openai_api(client, context, prompt):
    """Call OpenAI API to generate AsciiDoc content."""
    completion = client.chat.completions.create(
        model=config['DEPLOYMENT'],
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )
    return completion.choices[0].message.content.strip().replace("```asciidoc", '').replace("```", '')
