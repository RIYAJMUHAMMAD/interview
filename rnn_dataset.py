import pytorch
import torch.nn as nn
from torch.utils.data import Dataset
import numpy as numpy


class TextDataset:
    def __init__(self, text_data: str, seq_length:int=25)-> None:

        self.chars = sorted(list(set(text_data)))
        self.data_size, self.vocab_size = len(text_data), len(self.chars)
        self.idx_to_char = {i:ch for i, ch in enumerate(self.chars)}
        self.char_to_idx = {ch:i for i, ch in enumerate(self.chars)}
        self.seq_length = seq_length
        self.input = self.string_to_vector(text_data)

    def __len__(self)-> int:
        return int(len(self.input)/self.seq_length-1)

    def __getitem__(self,index) -> tuple[torch.Tensor, torch.Tensor]:

        start_idx = index* self.seq_length
        end_idx = (index+1)* self.seq_length
        X = torch.tensor(self.input[start_idx:end_idx]).float()
        y = torch.tensor(self.input[start_idx+1:end_idx+1]).float()
        return X, y

    def string_to_vector(self, name: str) -> list[int]:

        vector = list()
        for s in name:
            vector.append(self.char_to_idx[s])
        return vector

    def vector_to_string(self, vector: list[int]) -> str:

        vector_string = ""
        for i in vector:
            vector_string += self.idx_to_char[i]
        return vector_string

    

    