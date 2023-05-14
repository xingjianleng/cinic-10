import os
import shutil
import pandas


ds = pandas.read_csv("imagenet-contributors.csv", skipinitialspace=True)
cinic_sets = ds["cinic_set"].unique()
cinic_classes = ds["class"].unique()
unique_sets = ds["synset"].unique()


src = "/home/lengx/SSD/imagenet_subset/"
dst = "/home/lengx/SSD/cinic-10-original/"

# verify all images required are in the src folder
downloaded = os.listdir(src)
assert all([unique_set in downloaded for unique_set in unique_sets])

for cinic_set in cinic_sets:
    for cinic_class in cinic_classes:
        class_set_path = os.path.join(dst, cinic_set, cinic_class)
        # create dataset folder
        if not os.path.exists(class_set_path):
            os.makedirs(class_set_path)
        subset = ds[(ds["cinic_set"] == cinic_set) & (ds["class"] == cinic_class)]
        for _, row in subset.iterrows():
            imagenet_set = row["synset"]
            imagenet_num = row["image_num"]
            # copy images
            img_name = f"{imagenet_set}_{imagenet_num}.JPEG"
            shutil.copyfile(
                os.path.join(src, imagenet_set, img_name),
                os.path.join(class_set_path, img_name)
            )
