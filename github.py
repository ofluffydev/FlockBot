import os

import requests
from discord import Embed


def get_github_social_card(owner, repo):
    # GitHub API endpoint for repository details
    url = f"https://api.github.com/repos/{owner}/{repo}"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        repo_data = response.json()

        # Extract the social card image URL
        social_card_url = repo_data.get('social_image_url')

        if social_card_url:
            return social_card_url
        else:
            return "No social card image found for this repository."
    else:
        return f"Error: Unable to fetch repository data. Status code: {response.status_code}"


def get_github_repo(owner: str, repo: str) -> Embed:
    github_link = f'https://github.com/{owner}/{repo}'
    description = f'View our [GitHub Repository]({github_link})'
    embed_color = int(os.getenv('EMBED_COLOR'), 16)
    embed = Embed(title='GitHub Repository', description=description, color=embed_color)
    return embed
