import pandas as pd 
import torch
from torch.utils.data import Dataset

#定义一个数据集
class BulldozerDataset(Dataset):
    """ 数据集演示 """
    def __init__(self, csv_file):
        """实现初始化方法，在初始化的时候将数据读载入"""
        self.df=pd.read_csv(csv_file)

    def __len__(self):
        '''
        返回df的长度
        '''
        return len(self.df)
    def __getitem__(self, idx):
        '''
        根据 idx 返回一行数据
        '''
        return self.df.iloc[idx]
        
demo = BulldozerDataset(r"D:\university\mywprjs\Python\Pytorch\median_benchmark.csv")

demo[0]
len(demo)

# Dataloader
dl = torch.utils.data.DataLoader(demo, batch_size=10, shuffle=True, num_workers=0)
idata = iter(dl)

for i,data in enumerate(dl):
    print(i,data)
    break;
