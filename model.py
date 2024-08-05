import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import os
from pgdv import PGDV
from random import randint


class MusicDataset(Dataset):
    def __init__(self, context_size):
        self.dir = "./training_data"
        self.files = [PGDV.from_csv(os.path.join(self.dir, i)).data for i in os.listdir(self.dir) if i[-5:] == ".pgdv"]
        L = len(min(self.files, key=len))
        if L < context_size:
            raise ValueError('Dataset contains data shorter than context size.')
        ret = []
        for sub in self.files:
            R = len(sub) % context_size
            if R != 0 and len(sub) > context_size:
                shift = randint(0, R - 1)
                sub = sub[shift:shift - context_size + 1]
            ret += [sub[j:j + context_size] for j in range(0, len(sub), context_size)]
        self.data = ret

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


class Embedding(nn.Module):
    def __init__(self, d_p, d_gd, d_v, context):
        super().__init__()
        self.p_emb = nn.Embedding(88, d_p)
        self.gd_emb = nn.Linear(2, d_gd)
        self.v_emb = nn.Linear(1, d_v)

    def forward(self, x):  # x is a tensor of shape (batch_size, sequence_length, 4)
        pass


data = MusicDataset(context_size=2)
loader = DataLoader(data, batch_size=2, shuffle=False, collate_fn=torch.tensor)
print(list(loader))