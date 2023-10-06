def give_me_problem(weak_tags,Table):
    import pandas as pd
    import numpy as np

    from sklearn.feature_extraction.text import CountVectorizer

    cv = CountVectorizer()
    Table=pd.DataFrame.from_records(Table.objects.all().values())


    vectors = cv.fit_transform(Table['Tags']).toarray()

    cv.get_feature_names_out()

    from sklearn.metrics.pairwise import cosine_similarity

    similarity = cosine_similarity(vectors)

    def recommend(weak_tags):
        weak_vector = cv.transform([weak_tags]).toarray()
        similarity = cosine_similarity(weak_vector, vectors)
        distance = similarity[0]
        my_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:3]
        problem_list = list()
        for x in my_list:
            problem_list.append(x[0])
        return problem_list

    res = recommend(weak_tags)
    return res

    # cnt = 1;
    # for i in res:
    #     print("Problem ", cnt)
    #     cnt += 1
    #     print("Contest ID : ", Table['ID'][i])
    #     print("Problem No. : ", Table['Index'][i])
    #     print("Rating : ", Table['Rating'][i])
    #     print("Tags : ", Table['Tags'][i])
    #     print("")

