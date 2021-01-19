def prepare_score_ranking(score_ranking):

    #delete column's names
    del score_ranking[0]

    #european to standard number format
    for i in range(len(score_ranking)):
        score_ranking[i][0] = int(score_ranking[i][0])
        score_ranking[i][1] = float(score_ranking[i][1].replace(",", "."))

    #scale score_ranking
    for l in range(len(score_ranking)):
        score_ranking[l][1] = score_ranking[l][1] / 100

    return score_ranking
