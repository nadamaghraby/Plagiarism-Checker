import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#Plagiarism checker for texts
#Loading all text files in the directory
files=[doc for doc in os.listdir() if doc.endswith('.txt')]
#Open files
notes=[open(File).read() for File in files]
#Lambda function to convert text into array of numbers (Vectorization)
vectorize=lambda Text:TfidfVectorizer().fit_transform(Text).toarray()
#another lambda function to calculate the similarities between pairs of files
#Using cosine similarity
similarity= lambda doc1,doc2: cosine_similarity([doc1,doc2])
#Vectorize the files
vectors=vectorize(notes)
f_vectors=list(zip(files,vectors))

#function for calculating similaritest
def plagiarism_checker():
    plagiarism_results=set()
    global f_vectors
    for file_a, txt_a in f_vectors:
        new_vectors=f_vectors.copy()
        current_index=new_vectors.index((file_a,txt_a))
        del new_vectors[current_index]
        for file_b,txt_b in new_vectors:
            sim_score=similarity(txt_a,txt_b)[0][1]
            plag_pair=sorted((file_a,file_b))
            score=(plag_pair[0],plag_pair[1],sim_score)
            plagiarism_results.add(score)
    return plagiarism_results

for data in plagiarism_checker():
    print(data)
