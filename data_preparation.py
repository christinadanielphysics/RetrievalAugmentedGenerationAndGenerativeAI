from langchain_community.docstore.document import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def form_list_with_modified_abstract(abstract_text):
    abstract_list = []
    abstract_list.append(Document(abstract_text))
    return abstract_list

def remove_separators(list_of_separators, pieces_of_abstract):
    modified_pieces_of_abstract = []
    for piece in pieces_of_abstract:
        modified_document = piece
        for separator in list_of_separators:
            modified_document = Document(modified_document.page_content.replace(separator,' '))
        modified_pieces_of_abstract.append(modified_document)
    return modified_pieces_of_abstract

def split_abstract(old_abstract):
    abstract_text = old_abstract[0].page_content.replace('\n', ' ')

    modified_abstract = form_list_with_modified_abstract(abstract_text)

    chunk_size_limit = 20
    max_chunk_overlap = 0
    list_of_separators = [",",".","?","!",";",":"]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size_limit,
        chunk_overlap=max_chunk_overlap,
        separators=list_of_separators
    )
    
    pieces_of_abstract = text_splitter.split_documents(modified_abstract)
    modified_pieces_of_abstract = remove_separators(list_of_separators,pieces_of_abstract)

    return modified_pieces_of_abstract

