import requests 
from langchain_community.docstore.document import Document
import xml.etree.ElementTree # manipulate XML

def get_xml_entries(word_for_query):
    precise_query = "all:" + word_for_query
    url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": precise_query,
        "start": 0,
        "max_results": 10
    }
    response = requests.get(url, params=params)
    xml_entries = xml.etree.ElementTree.fromstring(response.text)
    return xml_entries

def get_abstracts(xml_entries):

    arxiv_namespace = {
        'atom': 'http://www.w3.org/2005/Atom',
    }
    abstracts = []
    for entry in xml_entries.findall('atom:entry', arxiv_namespace):
        abstract = entry.find('atom:summary', arxiv_namespace)
        if abstract is not None:
            list_of_one_abstract = form_list_with_abstract(abstract)
            abstracts.append(list_of_one_abstract)
    return abstracts

def form_list_with_abstract(abstract):
    abstract_list = []
    abstract_list.append(Document(abstract.text))
    return abstract_list
    




