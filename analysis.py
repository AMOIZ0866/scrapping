import json
import pandas as pd
import matplotlib.pyplot as plt


class Analysis:

    # Getting Top 10 Height Rating Movies #
    def get_high_rating(self):
        rawdata = pd.read_json('data.json')
        result = rawdata.nlargest(10, ['rating_score'])
        filtered_result = result.filter(['title', 'rating_score'])
        df = pd.DataFrame(filtered_result)
        df.plot.barh(x='title', y='rating_score', rot=0)
        plt.xticks(rotation=30)
        plt.show()

    # Getting author with most number of books
    def get_author_with_most_books(self):
        rawdata = pd.read_json('data.json')
        df = pd.DataFrame(rawdata, columns=['author'])
        duplicate = df[df.duplicated('author')]
        datalist = duplicate['author'].tolist()
        authorslist = {item: datalist.count(item) for item in datalist}
        output_file = open('author_books_most.json', 'w', encoding='utf-8', )
        json_object = json.dumps(authorslist, indent=4)
        output_file.write(json_object)

    # Getting genres with number of books #
    def get_genres_with_number_of_books(self):
        rawdata = pd.read_json('data.json')
        df = pd.DataFrame(rawdata, columns=['genre'])
        genre = df['genre']
        genre_obj = genre.values.tolist()
        rawlist = []
        for obj in genre_obj:
            for g in obj:
                rawlist.append(g)
        genrelist = {item: rawlist.count(item) for item in rawlist}
        output_file = open('genres_number_of_books.json', 'w', encoding='utf-8', )
        json_object = json.dumps(genrelist, indent=4)
        output_file.write(json_object)

    # Getting average rating per genre
    def get_avg_rating_genres(self):
        rawdata = pd.read_json('data.json')
        df = pd.DataFrame(rawdata, columns=['genre', 'rating_score'])
        obj = df.values.tolist()
        avglist = {}
        genrelist = {}
        countlist = {}

        for d in obj:
            for g in d[0]:
                if genrelist.get(g):
                    prerating = int(genrelist[g])
                    newrating = d[1] + prerating
                    countkey = str(g)
                    precount = countlist[countkey]
                    newcount = precount + 1
                    countlist[g] = newcount
                    genrelist[g] = newrating
                else:
                    countkey = str(g)
                    countlist[countkey] = 1
                    genrelist[g] = d[1]

        for k, v in genrelist.items():
            if countlist.get(k):
                totalgenres = countlist[k]
                total = v / totalgenres
                avglist[k] = round(total, 4)

        output_file = open('avg_rating.json', 'w', encoding='utf-8', )
        json_object = json.dumps(avglist, indent=4)
        output_file.write(json_object)
