import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("--old_csv", type=str, help="File CSV yang menyimpan stopwords lama", default="./stopwords_twitter.csv")
ap.add_argument("--collected_stopwords", type=str, required=True, help="Stopwords baru yang sudah dikumpulkan", default="./collected.txt")
args = vars(ap.parse_args())

def merge(old, new):
    old_stopwords = pd.read_csv(old, names=["stopword"])
    new_stopwords = pd.read_csv(new, names=["stopword"])

    stopwords_diff = new_stopwords[~new_stopwords.isin(old_stopwords)]
    
    stopwords_full = pd.concat([old_stopwords, stopwords_diff])

    stopwords_full = stopwords_full.sort_values(by="stopword", ascending=True)
    stopwords_full.reset_index(drop=True, inplace=True)
    stopwords_full.drop_duplicates(inplace=True, ignore_index=True)
    
    stopwords_full.to_csv("stopwords_twitter.csv", index=False)
    
if __name__=="__main__":
    merge(args["old_csv"], args["collected_stopwords"])