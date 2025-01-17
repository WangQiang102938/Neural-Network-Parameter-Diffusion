import os
import shutil
import random


src = [os.path.join("../../main/cifar100_resnet18/checkpoint", i)
       for i in os.listdir("../../main/cifar100_resnet18/checkpoint")]
os.makedirs("./checkpoint", exist_ok=True)
dst = "./checkpoint"


src.sort()
src = src[:1]
for i in src:
    shutil.copy(i, os.path.join(dst, "origin.pth"))
for i in src:
    shutil.copy(i, os.path.join(dst, "repeat.pth"))
