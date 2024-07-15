from arxiv_api import get_abstracts, get_xml_entries
from data_preparation import split_abstract
from embeddings import embed_pieces_of_abstracts, embed_query
from retrieval_and_generation import retrieve_relevant_pieces, generate_response
import streamlit


def answer_question(arxiv_query,complete_query):
    xml_entries = get_xml_entries(arxiv_query)
    abstracts = get_abstracts(xml_entries)

    pieces_of_abstracts = {}
    for abstract_index,abstract in enumerate(abstracts):
        pieces_of_abstracts[str(abstract_index)] = split_abstract(abstract)

    embedded_pieces_of_abstracts = embed_pieces_of_abstracts(pieces_of_abstracts)
    embedded_query = embed_query(complete_query)

    relevant_pieces = retrieve_relevant_pieces(embedded_query,embedded_pieces_of_abstracts,pieces_of_abstracts)
    response = generate_response(relevant_pieces,complete_query)
    return response


def streamlit_view():
    streamlit.title("Ask a STEM Question.")

    complete_query = streamlit.text_input("Enter your STEM question.")
    arxiv_query = streamlit.text_input("Enter 1-2 words that are closely related to your STEM question.")

    if streamlit.button("Submit"):
        response = answer_question(arxiv_query,complete_query)

        streamlit.write("Answer:")
        streamlit.write(response)










if __name__ == '__main__':
    streamlit_view()


def print_abstracts(pieces_of_abstracts):
    for abstract_index in pieces_of_abstracts:
        for document in pieces_of_abstracts[abstract_index]:
            print(document.page_content)


    