import os
import tarfile
import wget
import tqdm
import pandas


def download_id(wnid, out):
    print(f"Downloading: {wnid}")
    download_url = f"https://image-net.org/data/winter21_whole/{wnid}.tar"
    filename = wget.download(download_url, out)
    
    folder_name = os.path.join(out, wnid)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    compress = tarfile.open(filename)
    compress.extractall(folder_name)
    os.remove(filename)


if __name__ == "__main__":
    ds = pandas.read_csv("imagenet-contributors.csv", skipinitialspace=True)
    tar = "/home/lengx/SSD/imagenet_subset/"
    if not os.path.exists(tar):
        os.makedirs(tar)
    unique_sets = ds["synset"].unique()
    for unique_set in tqdm.tqdm(unique_sets):
        download_id(unique_set, tar)
