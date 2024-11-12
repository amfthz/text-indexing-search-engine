
# 📄 Project Title: Text Indexing and Search Engine

## Overview
This project is a Python-based indexing and search engine that allows you to extract, index, and search text content from PDF and HTML documents. The project consists of two main modules:
1. `main_indexing.py`: Indexes the documents in a specified directory.
2. `main_search.py`: Provides a search interface to find relevant documents based on user queries.

## Features
- **Text Extraction**: Extracts text content from PDF files using `pdfplumber` and from HTML files using `BeautifulSoup`.
- **Indexing**: Creates an inverted index of terms, storing their positions in the documents.
- **Search Functionality**: Supports both regular and phrase-based searches using TF-IDF scoring for relevance ranking.
- **Stop Word Removal**: Filters out common English stop words to improve search results.

## Technologies Used
- Python 3
- `pdfplumber` for PDF text extraction
- `BeautifulSoup` for HTML parsing
- `pickle` for saving and loading the index
- `math` module for TF-IDF calculations

## 🛠️ Setup and Installation

### Prerequisites
- Python 3 installed on your system.
- Git installed and configured.
- Python packages: `pdfplumber`, `beautifulsoup4`

### Installation Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/text-indexing-search-engine.git
   cd text-indexing-search-engine
   ```

2. **Install the required Python packages**:
   ```bash
   pip install pdfplumber beautifulsoup4
   ```

3. **Ensure you have a directory with PDF or HTML files for indexing**.

## 🚀 Usage

### 1. Indexing Documents
To index the documents in a specified directory, run the `main_indexing.py` script:
```bash
python main_indexing.py
```
- You will be prompted to enter the directory path containing your documents.
- The indexed data will be saved as `index.pkl`.

### 2. Searching Documents
To search the indexed documents, run the `main_search.py` script:
```bash
python main_search.py
```
- Enter your search query when prompted.
- Specify if it is a phrase search (`yes`/`no`).
- The script will display the list of matching documents along with their relevance scores.

## 📝 Example

### Indexing
```bash
Enter the directory to index: ./documents
Index successfully saved to 'index.pkl'
```

### Searching
```bash
Enter your search query: data analysis
Is this a phrase search? (yes/no): no
Term/phrase 'data analysis' found in the following documents:
Document ID: 0, Path: ./documents/report1.pdf, Relevance Score: 0.1234
Document ID: 2, Path: ./documents/analysis.html, Relevance Score: 0.0987
Total documents found: 2
```

## 🗂️ Project Structure
```
text-indexing-search-engine/
├── main_indexing.py       # Indexing script
├── main_search.py         # Search script
├── index.pkl              # Saved index data (auto-generated)
├── README.md              # Project documentation
```

## ⚠️ Notes
- The project uses a list of common English stop words to filter out irrelevant terms during indexing and searching.
- The index is saved as a `pickle` file (`index.pkl`) for quick loading during searches.

## 💡 Future Improvements
- Add support for more file formats (e.g., Word documents).
- Implement a graphical user interface (GUI) for easier search functionality.
- Enhance search ranking by incorporating more sophisticated algorithms (e.g., BM25).

## 🤝 Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Contact
For any questions or feedback, please contact:
- **Your Name**: [your-email@example.com](mailto:your-email@example.com)
- GitHub: [your-username](https://github.com/your-username)
