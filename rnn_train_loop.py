from rnn_dataset import TextDataset
from rnn_model import RNN

def generate_text(model: RNN, dataset: TextDataset, prediction_length: int =100) -> str:
    
    model.eval()
    predicted = dataset.vector_to_string([random.randint(0, len(dataset.chars)-1)])
    hidden = model.init_hidden()

    for i in range(predicted_length -1):
        last_char = torch.Tensor([dataset.char_to_idx[predicted[-1]]])
        X, hidden = last_char.to(device), hidden.to(device)
        out, hidden = model(X, hidden)
        result = torch.multinomial(nn.functional.softmax(out, 1), 1).item()
        predicted += dataset.idx_to_char[result]
    return predicted

def train(model: RNN, data: DataLoader, epochs: init, optimizer: optim.Optimizer, loss_fn:nn.Module) -> None:
    train_losses = {}
    model.to(device)
    model.train()
    print("=> Starting training")
    for epoch in range(epochs):
        for X, Y in data:
            if X.shape[0] != model.batch_size:
                continue
            hidden = model.init_hidden(batch_size = model.batch_size)

            X, Y, hidden = X.to(device), Y.to(device), hidden.to(device)

            model.zero_grad()
            loss = 0
            for c in range(X.shape[1]):
                out, hidden = model(X[:, c].reshape(X.shape[0],1), hidden)
                l = loss_fn(out, Y[:, c].long())
                loss += l

            loss.backward()

            nn.utils.clip_grad_norm_(model.parameters(), 3)
            optimizer.step()
            epoch_losses.append(loss.detach().item()/ X.shape[1])

        train_losses[epoch] = torch.tensor(epoch_losses).mean()
        print(f'=> epoch: {epoch + 1}, loss: {train_losses[epoch]}')
        print(generate_text(model, data.dataset))