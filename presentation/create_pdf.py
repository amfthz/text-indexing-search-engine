from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def create_pdf(file_path):
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Page 1: Introduction
    story.append(Paragraph("Document Indexing and Search System", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Welcome to the documentation of our Document Indexing and Search System. This system is designed to efficiently "
        "index and search through various document types, including PDF, TXT, and HTML files. The key features include the "
        "use of stop words, positional indexing, and the calculation of term frequency-inverse document frequency (TF-IDF) scores.",
        styles['BodyText']
    ))
    story.append(Spacer(1, 48))

    # Page 2: Stop Words
    story.append(Paragraph("Stop Words", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Stop words are common words that are often excluded from indexing and search operations to improve performance and relevance. "
        "In our system, we use a predefined set of English stop words to filter out terms that do not contribute significantly to the "
        "meaning of the documents.", styles['BodyText']
    ))
    story.append(Spacer(1, 12))
    stop_words = "a, an, the, and, but, if, or, because, as, until, while, of, at, by, for, with, about, against, between, into, through, during, before, after, above, below, to, from, up, down, in, out, on, off, over, under, again, further, then, once, here, there, when, where, why, how, all, any, both, each, few, more, most, other, some, such, no, nor, not, only, own, same, so, than, too, very, s, t, can, will, just, don, should, now"
    story.append(Paragraph("List of Common Stop Words:", styles['Heading3']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(stop_words, styles['BodyText']))
    story.append(Spacer(1, 48))

    # Page 3: Positional Indexing
    story.append(Paragraph("Positional Indexing", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "Positional indexing is a powerful technique used in our system to keep track of the positions of words within documents. "
        "This allows for advanced search capabilities, including phrase searches and proximity queries.", styles['BodyText']
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph("How Positional Indexing Works:", styles['Heading3']))
    story.append(Spacer(1, 12))
    steps = [
        "Tokenization: Text is tokenized into individual words, excluding stop words.",
        "Index Creation: For each document, the positions of each token are recorded.",
        "Posting Lists: These positions are stored in posting lists, which map each token to its occurrences in the documents."
    ]
    for step in steps:
        story.append(Paragraph(step, styles['BodyText']))
        story.append(Spacer(1, 12))
    story.append(Paragraph("Example:", styles['Heading3']))
    story.append(Spacer(1, 12))
    example = "Document 1: \"The quick brown fox jumps over the lazy dog\"\nToken: \"quick\" -> Positions: [1]\nToken: \"fox\" -> Positions: [3]"
    story.append(Paragraph(example, styles['BodyText']))
    story.append(Spacer(1, 48))

    # Page 4: TF-IDF
    story.append(Paragraph("Term Frequency-Inverse Document Frequency (TF-IDF)", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "TF-IDF is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus). "
        "Our system uses TF-IDF to rank documents based on their relevance to the search query.", styles['BodyText']
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph("TF-IDF Calculation:", styles['Heading3']))
    story.append(Spacer(1, 12))
    tfidf_steps = [
        "Term Frequency (TF): Measures how frequently a term appears in a document.",
        "Inverse Document Frequency (IDF): Measures how important a term is in the entire corpus.",
        "TF-IDF Score: Combines TF and IDF to give the final score."
    ]
    for step in tfidf_steps:
        story.append(Paragraph(step, styles['BodyText']))
        story.append(Spacer(1, 12))
    tf_formula = [
        "TF = (Number of occurrences of the term in the document) / (Total number of terms in the document)",
        "IDF = log(Total number of documents / Number of documents containing the term)",
        "TF-IDF = TF * IDF"
    ]
    for formula in tf_formula:
        story.append(Paragraph(formula, styles['BodyText']))
        story.append(Spacer(1, 12))
    story.append(Paragraph("Example:", styles['Heading3']))
    story.append(Spacer(1, 12))
    tfidf_example = "Term: \"fox\"\nDocument Frequency (DF): 1 (appears in 1 out of 10 documents)\nIDF: log(10 / 1) = 1\nTF in Document 1: 1 / 9\nTF-IDF: (1/9) * 1 ≈ 0.111"
    story.append(Paragraph(tfidf_example, styles['BodyText']))

    doc.build(story)

# Create the PDF
create_pdf("Document_Indexing_and_Search_System.pdf")
