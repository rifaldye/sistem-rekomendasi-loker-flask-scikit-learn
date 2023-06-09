import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import RegexpTokenizer
import re
import string
import random
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

class ai:

    def search(data,keyword):
        df = pd.DataFrame(data,columns=["id","title","desc"])
        df = df.dropna()
        factory = StopWordRemoverFactory()
        stopword = factory.create_stop_word_remover()
        for i, kalimat in enumerate (df.iterrows()):
            html_pattern = re.compile('<.*?>')
            df.at[i,"desc"] = stopword.remove(html_pattern.sub(r'',df.loc[i,'desc'].lower()))
            df.at[i,"title"] = stopword.remove(html_pattern.sub(r'',df.loc[i,'title'].lower()))
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(df['desc'])
        
        new_tfidf_vector = vectorizer.transform([keyword])

        similarity_scores = cosine_similarity(new_tfidf_vector, tfidf_matrix)
        return similarity_scores
        

        
    
