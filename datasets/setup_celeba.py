import os
import glob
import numpy as np
import shutil

dir = './data/img_align_celeba'

categories = os.listdir(dir)

if not os.path.exists(dir + '/test/'):
    os.mkdir(dir + '/test/')
if not os.path.exists(dir + '/train/'):
    os.mkdir(dir + '/train/')

categories = ['1']

for cat in categories:
    files = glob.glob(os.path.join(dir,'*.jpg'))
    num_all = len(files)
    num_train = round(num_all * 99 / 100)
    id_all = np.random.choice(num_all, num_all, replace=False)

    if not os.path.exists(dir + '/test/' + cat):
        os.mkdir(dir + '/test/' + cat)
    if not os.path.exists(dir + '/train/' + cat):
        os.mkdir(dir + '/train/' + cat)

    for i in id_all[0:num_train]:
        shutil.copy(files[i], dir + '/train/' + cat)
    for i in id_all[num_train:]:
        shutil.copy(files[i], dir + '/test/' + cat)
