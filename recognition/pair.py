import os, random
import time
from tqdm import tqdm
from tqdm._tqdm import trange
from PIL import Image
from collections import defaultdict
import cv2 as cv 
random.seed(0)

# list ---> txt
def text_save(filename, data):# filename为写入txt文件的路径，data为要写入的list
    file = open(filename,'w')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("write txt is OK") 


# new
def pair_new(dataset_name):

    lines_same = [] # 类内
    lines_diff = [] # 类间
    lines_all  = [] # 类内 + 类间

    anno_path = '../Dataset/annotations/' + dataset_name 
    test_csv =  anno_path +'/' + dataset_name +'_test.csv'
    with open( test_csv ) as f:
        imgs = f.read().splitlines()[0:] # 所有行都放到一个 list 中
    len_imgs = len(imgs)
    print('测试集中的图片数量',len_imgs)

    print('生成匹配对中 ... ...')
    for i in tqdm(range(len_imgs)):

        j = i + 1
        while j < len_imgs:

            if imgs[i].split('\\')[-1][0] == 'S': # for CASIA

                if imgs[i].split('\\')[-1][0:6] == imgs[j].split('\\')[-1][0:6] :  # img名字某部分相同，也就是类内的话
                    line_same = str(imgs[i])+ ' ' +str(imgs[j]) + ' ' + str(1) + ' '               # 放到类内list
                    lines_same.append(line_same)                
                elif imgs[i].split('\\')[-1][0:6] != imgs[j].split('\\')[-1][0:6] : 
                    line_diff = str(imgs[i])+ ' '+str(imgs[j]) + ' ' + str(0)+ ' ' 
                    lines_diff.append(line_diff)

            elif imgs[i].split('\\')[-1][0] != 'S': # for NEW
                if imgs[i].split('\\')[-1][14:21] == imgs[j].split('\\')[-1][14:21] :# for new
                    line_same = str(imgs[i])+ '\t' +str(imgs[j]) + '\t' + str(1) + '\t'                 # 放到类内list
                    lines_same.append(line_same)               
                elif imgs[i].split('\\')[-1][14:21] != imgs[j].split('\\')[-1][14:21] : # for new
                    line_diff = str(imgs[i])+ '\t'+str(imgs[j]) + '\t' + str(0) + '\t'
                    lines_diff.append(line_diff)

            j = j+1

    len_same = len(lines_same)
    len_diff = len(lines_diff)
    print('类内一共:',len_same)
    print('类间一共:',len_diff)
    #print('类间选择:',len(lines_diff_part))

    print('generate pair.txt and maybe spend lots of time ... ...')

    random.shuffle(lines_diff) # 打乱类间

    lines_diff_part1 = lines_diff[:] # 1倍  len_same 100000 1000000  1000000 5000000
    #lines_diff_part2 = lines_diff[len_same:11*len_same] # 10倍
    #lines_diff_part3 = lines_diff[11*len_same:61*len_same] # 50倍
    lines_diff_part4 = lines_diff[61*len_same:161*len_same] # 100倍
    
    lines_all1 = lines_same + lines_diff_part1
    #lines_all2 = lines_same + lines_diff_part2
    #lines_all3 = lines_same + lines_diff_part3
    lines_all4 = lines_same + lines_diff_part4

    test_pair = anno_path +'/' + dataset_name +'_' +str(len_same)+'_'+str(len(lines_diff_part1))+'.csv'
    test_pair1 = anno_path +'/' + dataset_name +'_' +str(len_same)+'_'+str(len(lines_diff_part4))+'.csv'

    text_save(test_pair,lines_all1)
    #text_save('pair\\CASIA4-Iris-Thousand-12080_resnet_pairs_'+str(len_same)+'_'+str(len(lines_diff_part1))+'.csv',lines_all1)
    #text_save('pair\\pairs_2000_'+str(len_same)+'_'+str(len(lines_diff_part2))+'_ACC.txt',lines_all2)
    #text_save('pair\\pairs_2822_'+str(len_same)+'_'+str(len(lines_diff_part3))+'_ACC.txt',lines_all3)
    text_save(test_pair1,lines_all4)

    print('finish')

    
if __name__ == '__main__':

    dataset = 'CASIA-Iris-Lamp'
    pair_new(dataset)
