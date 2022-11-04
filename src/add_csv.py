import argparse
import datetime

import pandas as pd


def main(opt: argparse.Namespace):
    
    old_stopwords = pd.read_csv(opt.old_csv, header=None)
    new_stopwords = pd.read_csv(opt.new_stopwords, header=None)
    
    # lower kemudian menghilangkan newline (\n)
    new_stopwords[0] = new_stopwords[0].map(lambda x: x.lower().strip())
    # mencari stopwords yang berbeda dengan sebelumnya
    stopwords_diff = new_stopwords[~new_stopwords.isin(old_stopwords)]
    
    stopwords_full = pd.concat([old_stopwords, stopwords_diff], ignore_index=True)
    
    # mencari waktu sekarang berdasarkan utc + 8
    curr_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    curr_time = curr_time.strftime("%Y-%m-%d %H.%M.%S")
    
    # menyimpan csv berdasarkan waktu
    stopwords_full.to_csv(f"{curr_time} stopwords_twitter.csv", index=False)
    
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--old_csv", type=str, help="File csv yang menyimpan stopwords lama", default="./stopwords_twitter.csv")
    # parser.add_argument("--new_csv", type=str, help="Nama File yang digunakan untuk menamakan file csv stopwords baru", default="./datex stopwords_twitter.csv")
    parser.add_argument("--new_stopwords", type=str, required=True, help="File txt yang berisikan stopwords baru untuk ditambahkan ke list stopwords")
    
    opt = parser.parse_args()
    print(type(opt))
    main(opt)
