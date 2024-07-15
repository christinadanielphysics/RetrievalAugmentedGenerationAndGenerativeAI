from langchain_openai import OpenAIEmbeddings

OPENAI_API_KEY = "sk-proj-SYAXhaEVw54Bud4ejM5iT3BlbkFJ37RCu74YVSdHN2ekjW13"

def embed_pieces_of_abstracts(pieces_of_abstracts):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    embedded_pieces_of_abstracts = {}
    for abstract_index in pieces_of_abstracts:
        embedding_for_pieces_of_abstract = []
        for document in pieces_of_abstracts[abstract_index]:
            text = document.page_content
            dense_vector = embeddings.embed_documents([text])[0]
            embedding_for_pieces_of_abstract.append(dense_vector)
        embedded_pieces_of_abstracts[abstract_index] = embedding_for_pieces_of_abstract
    return embedded_pieces_of_abstracts

def embed_query(query):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    text = query
    dense_vector = embeddings.embed_documents([text])[0]
    return dense_vector



