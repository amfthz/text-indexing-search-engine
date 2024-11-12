
import pickle
from collections import defaultdict
import math

# List of common English stop words to filter out during search queries
STOP_WORDS = set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your',
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
    "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this',
    'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
    'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
    'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just'
])

# Function to load the indexed data from 'index.pkl'
def load_index():
    with open('index.pkl', 'rb') as index_file:
        return pickle.load(index_file)

# Function to calculate TF-IDF score for relevance ranking
def calculate_tfidf(term_frequency, total_documents):
    tfidf = defaultdict(lambda: defaultdict(float))
    for term, doc_freqs in term_frequency.items():
        doc_count = len(doc_freqs)
        idf = math.log(total_documents / (1 + doc_count))
        for doc_id, freq in doc_freqs.items():
            tf = freq
            tfidf[term][doc_id] = tf * idf
    return tfidf

# Function to handle phrase search queries
def phrase_search_query(terms, dictionary, posting_list, file_paths, term_frequency):
    if not terms:
        return []

    # Check if all terms exist in the dictionary
    term_positions = [posting_list.get(term, {}) for term in terms]
    if not all(term_positions):
        return []

    # Find common documents containing all terms
    potential_docs = set(term_positions[0].keys())
    for postings in term_positions[1:]:
        potential_docs.intersection_update(postings.keys())

    results = []
    for doc_id in potential_docs:
        term_indices = [positions for positions in (posting_list[term][doc_id] for term in terms)]
        for pos in term_indices[0]:
            if all((pos + i) in term_indices[i] for i in range(len(terms))):
                tfidf = calculate_tfidf(term_frequency, len(file_paths))
                score = sum(tfidf[term].get(doc_id, 0) for term in terms)
                results.append((doc_id, file_paths[doc_id], score))
                break

    return results

# Function to handle general search queries
def search(query, dictionary, posting_list, file_paths, term_frequency, phrase_search=False):
    # Split the query into terms and filter out stop words
    terms = [term for term in query.lower().split() if term not in STOP_WORDS]
    if phrase_search:
        return phrase_search_query(terms, dictionary, posting_list, file_paths, term_frequency)

    results = []
    tfidf = calculate_tfidf(term_frequency, len(file_paths))
    potential_docs = set()

    # Collect all documents containing any of the terms
    for term in terms:
        if term in dictionary:
            potential_docs.update(dictionary[term])

    # Score each potential document based on term relevance
    for doc_id in potential_docs:
        score = sum(tfidf[term].get(doc_id, 0) for term in terms)
        results.append((doc_id, file_paths[doc_id], score))

    # Sort results by relevance score
    results.sort(key=lambda x: x[2], reverse=True)
    return results

# Main function to handle user input and perform searches
def main_search():
    dictionary, posting_list, file_paths, term_frequency = load_index()

    while True:
        query = input("Enter your search query: ").strip()
        if not query:
            break
        phrase_search = input("Is this a phrase search? (yes/no): ").strip().lower() == 'yes'

        # Perform search based on user input
        result = search(query, dictionary, posting_list, file_paths, term_frequency, phrase_search)

        # Print the search results
        print(f"Term/phrase '{query}' found in the following documents:")
        if result:
            for doc_id, file_path, score in result:
                print(f"Document ID: {doc_id}, Path: {file_path}, Relevance Score: {score:.4f}")
            print("Total documents found:", len(result))
        else:
            print("No documents found.")

# Entry point of the script
if __name__ == "__main__":
    main_search()
