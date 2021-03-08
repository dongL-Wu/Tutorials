#------------------------------------------------------------------------------
#  Libraries
#------------------------------------------------------------------------------
from tqdm import tqdm
from glob import glob
import os, cv2, random
from collections import defaultdict
random.seed(2020)

#-----------------------------------------------------------------------------------------------------
#  Funtion : Create [txt] of train and valid for [MMU2] [CASIA1] [CASIA 4 Interval] [CASIA 4 Thousand]
#                                                [CASIA 4 Lamp]
#-----------------------------------------------------------------------------------------------------

#  MMU2------------------------------------------------------------------------
def split_train_val_mmu2():

    # path
    IMAGE_DIR = "D:\\0MyCode\\Dataset\\MMU2"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "*\\*")))

    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[:-4])
        eye_id = int(basename[-4:-2])
        ins_id = int(basename[-2:])
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []

    for key, vals in data_dict.items():
        for val in vals.values():
            train_list += [val[i] for i in range(3)]
            valid_list += [val[i] for i in range(3,5)]

    # Write to file
    random.shuffle(train_list)
    with open("test/mmu2_train.txt", 'w') as fp:
        for file in train_list:
            fp.writelines(file+'\n')

    random.shuffle(valid_list)
    with open("test/mmu2_valid.txt", 'w') as fp:
        for file in valid_list:
            fp.writelines(file+'\n')

#  CASIA1----------------------------------------------------------------------
def split_train_val_casia1():

    # path
    IMAGE_DIR = "D:\\0MyCode\\Dataset\\CASIA1_Unnormalization"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "**/*.*"), recursive=True))
    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file).split('.')[0]
        person_id, eye_id, ins_id = basename.split('_')
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []

    for key, vals in data_dict.items():
        for val in vals.values():
            train_list += [val[i] for i in range(2)]
            valid_list += [val[i] for i in range(2,len(val))]

    # Write to file
    random.shuffle(train_list)
    with open("test/unnormal_casia1_train.txt", 'w') as fp:
        for file in train_list:
            fp.writelines(file+'\n')

    random.shuffle(valid_list)
    with open("test/unnormal_casia1_valid.txt", 'w') as fp:
        for file in valid_list:
            fp.writelines(file+'\n')

#  CASIA 4 Interval------------------------------------------------------------
def split_train_val_casia4Interval():

    # path
    IMAGE_DIR = r"F:\jdd\Dataset-Interval\CASIA-Iris-Interval-train"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "*\\L\\*"), recursive=True))# 左右眼路径修改！
    files = [file for file in files if 'jpg' in file]
    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[2:5])
        eye_id = 0 if basename[5]=='L' else 1
        
        #ins_id = int(basename[-2:])# 01-10 有两位，故不像thousand
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []
    test_list = []
    for key, vals in data_dict.items():
        for val in vals.values():
            train_samples = int(len(val) * 1)
            train_list += [val[i] for i in range(train_samples)]
            valid_list += [val[i] for i in range(train_samples, len(val))]

    # Write to file
    #random.shuffle(train_list)
    with open(r"F:\jdd\Dataset-Interval\txt\CASIA-Iris-Interval-joint_train.csv", 'w') as fp:
        for file in train_list:
            fp.writelines(file +','+ str(int(file.split('\\')[-3])-1)+'\n')

    #random.shuffle(valid_list)
    #with open("F:\\jdd\\tools\\temp-txts\\CASIA-Interval_norm_testR.txt", 'w') as fp:
        #for file in valid_list:
            #fp.writelines(file+'\n')


#  CASIA 4 Thousand------------------------------------------------------------
def split_train_val_casia4Thousand():

    # path
    IMAGE_DIR = r"C:\jdd\Dataset8\splice_test\CASIA-Iris-Thousand"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "*\\*\\*"), recursive=True))# 左右眼路径修改！
    files = [file for file in files if 'jpg' in file] #  bmp
    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[2:5])
        eye_id = 0 if basename[5]=='L' else 1

        ins_id = int(basename[-1])# 00-09 只取一位
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []

    for key, vals in data_dict.items():
        for val in vals.values():

            #-----------------------------------------------------
            train_samples = int(len(val) * 0) # split rate 
            #-----------------------------------------------------

            train_list += [val[i] for i in range(train_samples)]
            valid_list += [val[i] for i in range(train_samples, len(val))]

    #random.shuffle(train_list)
    with open(r"CASIA4-Iris-Thousand_splice_train.csv", 'w') as fp:
        for file in train_list:
            
            #fp.writelines(file+'\n')

            if file.split('\\')[-2] == "L" :fp.writelines(file + ',' + str(int(file.split('\\')[-3]) -1      )   +'\n') 
            if file.split('\\')[-2] == "R" :fp.writelines(file + ',' + str(int(file.split('\\')[-3]) -1 +1000 )   +'\n')
            # 再用 excel 排序！

    #random.shuffle(valid_list)
    with open(r"CASIA4-Iris-Thousand_splice_test.csv", 'w') as fp:
        for file in valid_list:
            fp.writelines(file+'\n')

#  CASIA 4 Lamp----------------------------------------------------------------
def split_train_val_casia4Lamp():

    # path
    IMAGE_DIR = r"F:\jdd\Dataset\CASIA-IrisV4(JPG)\CASIA-Iris-Lamp"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "*\\*\\*"), recursive=True))# 仅单眼
    files = [file for file in files if 'jpg' in file]
    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[2:5])
        eye_id = 0 if basename[5]=='L' else 1
        ins_id = int(basename[-1])
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []
    test_list  = []
    for key, vals in data_dict.items():#  0.5:0.2:0.3 = 10: 4: 6  共20张
        for val in vals.values():
            train_samples = int(len(val) * 1   )# 12 ：8
            train_list += [val[i] for i in range(          train_samples  ) ]
            test_list  += [val[i] for i in range( train_samples, len(val) ) ]

    #random.shuffle(train_list)
    with open("data\\CASIA-Iris-Lamp.txt", 'w') as fp:
        for file in train_list:
            fp.writelines(file+'\n')

    #random.shuffle(test_list)
    #with open("data\\CASIA-Lamp_testR.txt", 'w') as fp:
        #for file in test_list:
            #fp.writelines(file+'\n')

#  5000Rename------------------------------------------------------------------
def split_train_val_5000Rename():

    # path
    IMAGE_DIR = r"D:\0MyCode\MyDataset\Unnorm2\5000rename"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "**/*.*"), recursive=True))
    files = [file for file in files if 'jpg' in file]
    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[2:6])
        eye_id = 0 if basename[6]=='L' else 1
        ins_id = int(basename[-1])# 00-09 只取一位
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []

    for key, vals in data_dict.items():
        for val in vals.values():
            train_samples = int(len(val) * 1)
            train_list += [val[i] for i in range(train_samples)]
            valid_list += [val[i] for i in range(train_samples, len(val))]

    # Write to file
    random.shuffle(train_list)
    with open("05000Rename_train.txt", 'w') as fp:
        for file in train_list:
            fp.writelines(file+'\n')

    random.shuffle(valid_list)
    with open("05000Rename_valid.txt", 'w') as fp:
        for file in valid_list:
            fp.writelines(file+'\n')

# casia 通用！
#  IITD-RE    -----------------------------------------------------------------
def split_train_val_iitd():

    # path
    IMAGE_DIR = r"F:\jdd\Dataset3\j12080\new1000"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "*\\*\\*"), recursive=True))  # 自由选择 单双眼
    files = [file for file in files if 'jpg' in file]
    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[2:5])
        eye_id = 0 if basename[5]=='L' else 1
        #ins_id = int(basename[-1])
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []
    test_list  = []
    for key, vals in data_dict.items():
        for val in vals.values():
            train_samples = int(len(val) * 1  )# 训练集比例！
            train_list += [val[i] for i in range(          train_samples  ) ]
            test_list  += [val[i] for i in range( train_samples, len(val) ) ]

    #random.shuffle(train_list)
    with open(r"samples-13.csv", 'w') as fp:#thousand-joint12080_train_L.csv
        for file in train_list:
            
            fp.writelines(file+'\n')# test 不必生成label
            #fp.writelines(file +','+ file.split('\\')[-3]+'\n') # train 直接生成 label

    #random.shuffle(test_list)
    #with open(r"CASIA-Iris-Thousand-test.csv", 'w') as fp:
        #for file in test_list:
            #fp.writelines(file+'\n')

# new1000
def split_train_val_new():

    # path
    IMAGE_DIR = r"C:\jdd\Dataset5\j12080\new1356"

    # Get files
    files = sorted(glob(os.path.join(IMAGE_DIR, "*\\*\\*"), recursive=True))  # 自由选择 单双眼
    files = [file for file in files if 'jpg' in file]
    print("Number of files:", len(files))

    # Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[15:21])
        eye_id = 0 if basename[14]=='L' else 1
        #ins_id = int(basename[-1])
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)

    # Split train/valid
    train_list = []
    valid_list = []
    test_list  = []
    for key, vals in data_dict.items():
        for val in vals.values():
            train_samples = int(len(val) * 0.7  )# 训练集比例！
            train_list += [val[i] for i in range(          train_samples  ) ]
            test_list  += [val[i] for i in range( train_samples, len(val) ) ]

    #random.shuffle(train_list)
    with open(r"new1356_train0.7.csv", 'w') as fp:#thousand-joint12080_train_L.csv
        for file in train_list:

            if file.split('\\')[-2] == "L" :fp.writelines(file + ',' + str(int(file.split('\\')[-3]) -1      )   +'\n') 
            if file.split('\\')[-2] == "R" :fp.writelines(file + ',' + str(int(file.split('\\')[-3]) +1356-1 )   +'\n')


    #random.shuffle(test_list)
    with open(r"new1356_test0.3.csv", 'w') as fp:
        for file in test_list:
            fp.writelines(file+'\n')#不必生成label

def periocular_split(dataset_name,class_id):
    image_path = '../Dataset/images/' + dataset_name 
    if not os.path.exists(image_path):
        print('image path do not exist........')
    
    anno_path = '../Dataset/annotations/' + dataset_name 
    if not os.path.exists(anno_path):
        os.makedirs(anno_path)
    
    # Get files
    files = sorted(glob(os.path.join(image_path, "*\\*\\*"), recursive=True))  # 自由选择 单双眼
    files = [file for file in files if 'jpg' in file]
    print("Number of files:", len(files))

    f = open(anno_path + '/' + 'info.txt', 'a')
    f.write("number of files is " + str(len(files)))
    #Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[2:5])
        eye_id = 0 if basename[5]=='L' else 1
        #ins_id = int(basename[-1])
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)
    #print(val)

    
    # Split train/valid
    train_list = []
    valid_list = []
    test_list  = []
    for key, vals in data_dict.items():
        for val in vals.values():
            train_samples = int(len(val) * 0.6  )# 训练集比例！
            train_list += [val[i] for i in range(          train_samples  ) ]
            test_list  += [val[i] for i in range( train_samples, len(val) ) ]
    
    #random.shuffle(train_list)
    train_csv = anno_path +'/' + dataset_name +'_train.csv'
    with open(train_csv, 'w') as fp:#thousand-joint12080_train_L.csv
        for file in train_list:
            file = file.split('Dataset/images/')[1]
            if file.split('\\')[-2] == "L" :fp.writelines(file + ',' + str(int(file.split('\\')[-3])  -1     )   +'\n') 
            if file.split('\\')[-2] == "R" :fp.writelines(file + ',' + str(int(file.split('\\')[-3])  - 1 + class_id )   +'\n')
            #fp.writelines(file[3:]+'\n')# test 不必生成label
            #fp.writelines(file[3:] +','+ file.split('\\')[-3]+'\n') # train 直接生成 label

    #random.shuffle(test_list)
    test_csv = anno_path +'/' + dataset_name +'_test.csv'
    with open(test_csv, 'w') as fp:
        for file in test_list:
            
            file = file.split('Dataset/images/')[1]
            fp.writelines(file+'\n')

def pe_split(dataset_name,class_id):
    image_path = '../Dataset/images/' + dataset_name 
    if not os.path.exists(image_path):
        print('image path do not exist........')
    
    anno_path = '../Dataset/annotations/' + dataset_name 
    if not os.path.exists(anno_path):
        os.makedirs(anno_path)
    
    # Get files
    files = sorted(glob(os.path.join(image_path, "*\\*\\*"), recursive=True))  # 自由选择 单双眼
    files = [file for file in files if 'jpg' in file]
    print("Number of files:", len(files))

    #Aggregate data
    data_dict = defaultdict(lambda: defaultdict(lambda: list()))
    for file in files:
        basename = os.path.basename(file)[:-4]
        person_id = int(basename[2:5])
        eye_id = 0 if basename[5]=='L' else 1
        #ins_id = int(basename[-1])
        data_dict[person_id][eye_id].append(file)

    for vals in data_dict.values():
        for val in vals.values():
            random.shuffle(val)
    #print(val)

    
    # Split train/valid
    train_list = []
    valid_list = []
    test_list  = []
    for key, vals in data_dict.items():
        for val in vals.values():
            train_samples = int(len(val) * 0.6  )# 训练集比例！
            train_list += [val[i] for i in range(          train_samples  ) ]
            test_list  += [val[i] for i in range( train_samples, len(val) ) ]
    
    #random.shuffle(train_list)
    train_csv = anno_path +'/' + dataset_name +'_train.csv'
    with open(train_csv, 'w') as fp:#thousand-joint12080_train_L.csv
        for file in train_list[:3]:
            print(file)
            file = file.split('Dataset/images/')[1]
            print(file.split('\\'))

    

if __name__ == "__main__":

    #split_train_val_mmu2()

    #split_train_val_casia1()

    #split_train_val_casia4Interval()

    #split_train_val_casia4Thousand()

    #split_train_val_casia4Lamp()

    #split_train_val_5000Rename()

    #split_train_val_iitd()# casia4 通用！！！

    #split_train_val_new()

    dataset = 'CASIA-Iris-Lamp'
    id = 411
    periocular_split(dataset, id)

    #pe_split(dataset, id)
