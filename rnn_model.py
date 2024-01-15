import torch
import torch.nn as nn

class RNN(nn.Module):

    def __init__(self, input_size: int, hidden_size: int, output_size: int) -> None:
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.batch_size = batch_size

        self.i2h = nn.Linear(input_size, hidden_size, bias=False)
        self.h2h = nn.Linear(hidden_size, hidden_size)
        self.h2o = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden_state) -> tuple[torch.Tensor, torch.Tensor]:

        x = self.i2h(x)
        hidden_state = self.h2h(hiddem_state)
        hidden_state = torch.tanh(x + hidden_state)
        return self.h2o(hidden_state), hidden_state

    def init_hidden(self, batch_size=1) -> torch.Tensor:

        return torch.init.kaiming_uniform_(torch.empty(1, self.hidden_size))