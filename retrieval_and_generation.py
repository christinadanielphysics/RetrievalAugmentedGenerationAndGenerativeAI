from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

OPENAI_API_KEY = "sk-proj-SYAXhaEVw54Bud4ejM5iT3BlbkFJ37RCu74YVSdHN2ekjW13"
client = OpenAI(api_key=OPENAI_API_KEY) 

def retrieve_relevant_pieces(embedded_query,embedded_pieces_of_abstracts,pieces_of_abstracts):
    similarity_scores = {}
    for abstract_index, embedded_abstract_pieces in embedded_pieces_of_abstracts.items():
        for embedded_piece_index, embedded_piece in enumerate(embedded_abstract_pieces):
            similarity_score = cosine_similarity([embedded_query],[embedded_piece])
            similarity_scores[(abstract_index, embedded_piece_index)] = similarity_score[0][0]
    sorted_scores_list = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    relevant_pieces = []
    max_number_of_relevant_pieces = 3
    for index,the_tuple in enumerate(sorted_scores_list):
        abstract_index = sorted_scores_list[index][0][0]
        abstract_pieces = pieces_of_abstracts[abstract_index]
        piece_index = sorted_scores_list[index][0][1]
        piece = abstract_pieces[piece_index]
        relevant_pieces.append(piece.page_content)
        if len(relevant_pieces) == max_number_of_relevant_pieces:
            break

    return relevant_pieces

def generate_response(relevant_pieces,query):
    prompt = query + " Here are some ideas.\n"
    prompt += "\n".join(relevant_pieces)
    prompt += "\nIn your response, please do not include information about the structure of this prompt.\n"

    print(prompt,"\n")

    # Generate the answer using the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7)

    final_response = response.choices[0].message.content.strip()
    return final_response


