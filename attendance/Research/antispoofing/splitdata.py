import os
import random
import shutil
from itertools import islice

outputFolderPath = "dataset/SplitData"
inputFolderPath = "dataset/all"
splitRatio = {"train": 0.7, "val": 0.2, "test": 0.1}
classes = ["fake", "real"]

# --------  Remove existing output folder if it exists -----------
try:
    shutil.rmtree(outputFolderPath)
except OSError as e:
    pass

# --------  Create new directories -----------
os.makedirs(f"{outputFolderPath}/train/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/train/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/labels", exist_ok=True)

# --------  Get unique names without extensions  -----------
listNames = os.listdir(inputFolderPath)
uniqueNames = list(set(name.split('.')[0] for name in listNames))

# --------  Shuffle -----------
random.shuffle(uniqueNames)

# --------  Calculate the number of images for each split -----------
lenData = len(uniqueNames)
lenTrain = int(lenData * splitRatio['train'])
lenVal = int(lenData * splitRatio['val'])
lenTest = int(lenData * splitRatio['test'])

# --------  Adjust training length to account for any remaining images -----------
if lenData != lenTrain + lenTest + lenVal:
    remaining = lenData - (lenTrain + lenTest + lenVal)
    lenTrain += remaining

# --------  Split the list -----------
lengthToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input, elem)) for elem in lengthToSplit]

print(f'Total Images: {lenData} \nSplit: {len(Output[0])} {len(Output[1])} {len(Output[2])}')

# --------  Copy the files with checks  -----------
sequence = ['train', 'val', 'test']
for i, out in enumerate(Output):
    for fileName in out:
        imgPath = f'{inputFolderPath}/{fileName}.jpg'
        labelPath = f'{inputFolderPath}/{fileName}.txt'
        if os.path.exists(imgPath):
            shutil.copy(imgPath, f'{outputFolderPath}/{sequence[i]}/images/{fileName}.jpg')
        else:
            print(f'Image file not found: {imgPath}')
        if os.path.exists(labelPath):
            shutil.copy(labelPath, f'{outputFolderPath}/{sequence[i]}/labels/{fileName}.txt')
        else:
            print(f'Label file not found: {labelPath}')

print("Split Process Completed...")

# -------- Creating data.yaml file  -----------
dataYaml = f'path: ../Data\n\
train: ../train/images\n\
val: ../val/images\n\
test: ../test/images\n\
\n\
nc: {len(classes)}\n\
names: {classes}'

with open(f"{outputFolderPath}/data.yaml", 'w') as f:
    f.write(dataYaml)

print("data.yaml file Created...")
