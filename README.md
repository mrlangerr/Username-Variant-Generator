Markdown

# 🐍 Username Variant Generator

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Description

The **Username Variant Generator** is a straightforward yet powerful **Python utility script** designed to help you generate a comprehensive list of potential usernames.

Whether you're looking to secure a consistent handle across multiple social media platforms, create a list for a security audit, or just need creative suggestions, this tool efficiently combines a base name with a set of predefined roles, keywords, and common delimiters to maximize your chances of finding an available username.

## ⚙️ How It Works

The script generates username variants by:

1.  Taking a **primary input name** (e.g., "johnsmith").
2.  Combining the name with an internal or custom list of **roles, keywords, and suffixes** (e.g., "dev", "official", "real", "gaming").
3.  Applying common **separators and modifiers** (e.g., `_`, `-`, `.`, numbers) to create a vast array of unique combinations.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You only need **Python 3.x** installed on your system.

```bash
python --version
Installation
Clone the repository to your local machine:

Bash

git clone [https://github.com/mrlangerr/Username-Variant-Generator.git](https://github.com/mrlangerr/Username-Variant-Generator.git)
cd Username-Variant-Generator
💻 Usage
To generate the list of usernames, simply run the main script generate_username.py using the Python interpreter. You will be prompted to enter the base name you want to generate variants for.

Running the Script
Bash

python generate_username.py
Example Input/Output
When prompted, if you enter a name like mrlanger, the script might generate a list similar to:

Plaintext

mrlanger
mrlanger_official
mrlangerdev
mrlanger.real
the_mrlanger
mrlanger_gaming
... (and hundreds more variants)
The output list is usually printed to the console, and can easily be redirected to a file for later use:

Bash

python generate_username.py > generated_usernames.txt
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.
