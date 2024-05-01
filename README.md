The README file should have the following:

project data structure implemented
short explanation of the data structure
If your project is something I can run, please give instructions on how to do that
If your project isn't something that I can run, show me what it does. You can take a video and upload it to YouTube or Vimeo or simply to a private Google drive link. Or if video isn't your thing, a document with screenshots and words explaining what's going on.
The main goal is to communicate clearly what you did and why.

# Storing Parsed Characters from Screenplays into a Radix Trie

This project parses the character names (with speaking roles) from a bundle of screenplays and organizes those into a radix trie which can be searched using an autocomplete text field in the provided web frontend.

## What is a Radix Trie?

A radix trie is a tree data structure that compresses strings by having shared parent nodes with the same prefix then concatenating it with children nodes until a leaf is reached, or more simply, a complete word is formed. The benefit of this structure is in reducing the space needed to store a large collection of data, such as IP addresses or words in a dictionary.

Insert the diagram generated:

## Running the Project

I'd recommend making a virtual environment for this to run in. I used Python 3.11.5 and venv.

## Why this Project

This project is a bit of "proof of concept" in a couple ways. 1. For me personally that I can actually build something. 2. That I can build something that might have future commercial viability. Having a little experience in the film industry much of the work for deriving information from screenplays is done by hand. Some of this is by neccessity and some of this by lack of innovation. I wanted to see if there is a way to streamline the assessment of screenplays by extracting key information a computer can accomplish quickly so that a person can focus on qualitative elements of story.

## Commentary on the Project

Being relatively new to programming, I wanted to push myself to cover several topics I hadn't worked on before but was curious about. I tried my hand at data mining and Python web development. Getting these two topics under control actually took more of my time than I expected versus implementing the radix trie. I found that PDFs are difficult to work with and wiring up a simple Flask application can be finicky at times for a beginner. The hardest part for me was diving into JavaScript to make the frontend of this application dynamically update.

## Fair Use Notice

This project uses copyrighted materials (i.e. screenplays in their entirety) under a fair use doctrine for the purpose education and is non-commercial in nature.
