
import os
import re
import pdfplumber
from bs4 import BeautifulSoup
from collections import defaultdict
import pickle

# List of common English stop words to filter out during indexing
STOP_WORDS = set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your',
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
    "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
    'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
    'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
    'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just',
    'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
    "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn',
    "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't",
    'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
])

# Function to preprocess text by removing special characters and stop words
def preprocess_text(text):
    # Convert to lowercase and remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    # Split text into words and filter out stop words
    words = [word for word in text.split() if word not in STOP_WORDS]
    return words

# Function to extract text from PDF files using pdfplumber
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
    return text

# Function to extract text from HTML files using BeautifulSoup
def extract_text_from_html(file_path):
    text = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            text = soup.get_text()
    except Exception as e:
        print(f"Error extracting text from {file_path}: {e}")
    return text

# Main function to index documents in the given directory
def index_documents(directory):
    dictionary = defaultdict(set)
    posting_list = defaultdict(lambda: defaultdict(list))
    file_paths = []
    term_frequency = defaultdict(lambda: defaultdict(int))

    # Traverse the directory and process files
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_id = len(file_paths)
            file_paths.append(file_path)

            # Extract text based on file extension
            if file.lower().endswith('.pdf'):
                text = extract_text_from_pdf(file_path)
            elif file.lower().endswith('.html'):
                text = extract_text_from_html(file_path)
            else:
                continue

            # Preprocess the extracted text
            words = preprocess_text(text)

            # Index each word in the document
            for position, word in enumerate(words):
                dictionary[word].add(file_id)
                posting_list[word][file_id].append(position)
                term_frequency[word][file_id] += 1

    # Save the index to disk using pickle
    save_index(dictionary, posting_list, file_paths, term_frequency)

# Function to save the index data using pickle
def save_index(dictionary, posting_list, file_paths, term_frequency):
    with open('index.pkl', 'wb') as index_file:
        pickle.dump((dictionary, posting_list, file_paths, term_frequency), index_file)
    print("Index successfully saved to 'index.pkl'")

# Entry point of the script
if __name__ == "__main__":
    directory = input("Enter the directory to index: ").strip()
    index_documents(directory)
