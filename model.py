import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import os
from format import PGDV


class MusicDataset(Dataset):
    def __init__(self):
        self.dir = "./training_data"
        self.filenames = [i for i in os.listdir(self.dir) if i[-5:] == ".pgdv"]

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        return PGDV.data_from(os.path.join(self.dir, self.filenames[idx]))


class Embedding(nn.Module):
    def __init__(self, d_p, d_gd, d_v, context):
        super().__init__()
        self.p_emb = nn.Embedding(128, d_p)
        self.gd_emb = nn.Linear(2, d_gd)
        self.v_emb = nn.Linear(1, d_v)
        self.positional_emb = nn.Embedding(context, d_p + d_gd, d_v)

    def forward(self, x):  # x is a tensor of shape (batch_size, sequence_length, 4)
        pass


