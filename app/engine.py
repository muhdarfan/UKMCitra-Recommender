import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class Engine:
    def __init__(self, dfLocation):
        self.dataDF = pd.read_json(dfLocation)
        self.tfidf = None
        self.tfidf_matrix = None

        self.load_model()
        print('Engine has been loaded successfully!')
        

    def generate_model(self):
        try:
            self.dataDF = self.dataDF.astype({
                'matric_no': 'string',
                'program': 'string',
                'session': 'string',
                'course_code': 'string'
            })

            self.dataDF['features'] = self.dataDF[['program', 'semester', 'session']].apply(lambda x: ' '.join(x.astype('string').str.lower()), axis=1)
            self.dataDF['features'] = self.dataDF.features.values.astype('U')
            
            tfidf = TfidfVectorizer(analyzer='word', stop_words="english")
            tfidf.fit(self.dataDF['features'])
            tfidf_matrix = tfidf.transform(self.dataDF['features'])

            self.tfidf = tfidf
            self.tfidf_matrix = tfidf_matrix

            ## Export Model
            with open('./models/tfidf.pkl', "wb") as f:
                pickle.dump(tfidf, f)
                
            with open('./models/tfidf_encodings.pkl', "wb") as f:
                pickle.dump(tfidf_matrix, f)

            print("done")
        except Exception as exc:
            print(exc)

    def load_model(self):
        try:
            with open('./models/tfidf.pkl', 'rb') as f:
                self.tfidf = pickle.load(f)
            
            with open('./models/tfidf_encodings.pkl', "rb") as f:
                self.tfidf_matrix = pickle.load(f)
        except IOError:
            print('Could not load model files. Please run /generate_model')
        except Exception as exc:
            print(f'[EXCEPTION] {exc}')
            
    def get_recommendations(self, input, N = 5):
        input_tfidf = self.tfidf.transform([input.lower()])

        cos_sim = map(lambda x: cosine_similarity(input_tfidf, x), self.tfidf_matrix)
        scores = list(cos_sim)
        top = sorted(range(len(scores)), key = lambda i: scores[i], reverse=True)[:N]

        '''
        recommendation = pd.DataFrame(columns = ['courseCode', 'program', 'semester', 'session' 'score'])

        for i in top:
            recommendation.at[i, 'courseCode'] = self.dataDF['course_code'][i]
            recommendation.at[i, 'program'] = self.dataDF['program'][i]
            recommendation.at[i, 'semester'] = self.dataDF['semester'][i]
            recommendation.at[i, 'session'] = self.dataDF['session'][i]
            recommendation.at[i, 'score'] = "{:.3f}".format(float(scores[i]))
        '''
        
        recommendation = []

        for i in top:
            recommendation.append({
                'courseCode': str(self.dataDF['course_code'][i]),
                'program': str(self.dataDF['program'][i]),
                'semester': int(self.dataDF['semester'][i]),
                'session': str(self.dataDF['session'][i]),
                'score': "{:.3f}".format(float(scores[i]))
            })
        
        return recommendation
        

if __name__ == '__main__':
    engineInstance = Engine('../data/student_courses_dataset.json')
    engineInstance.generate_model()