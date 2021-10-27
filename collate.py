import torch

def collate_fn_weighted(data):
    """Pad data in a batch.
    Parameters
    ----------
    data : list((tensor, int), )
        data and label in a batch
    Returns
    -------
    tuple(tensor, tensor)
    """
    # data: [(tensor, label), ...]
    max_len = max([i[0].shape[0] for i in data])
    labels = torch.tensor([i[1] for i in data], dtype=torch.long)
    weights = torch.tensor([i[2] for i in data], dtype=torch.float)
    padded = torch.zeros((len(data), max_len), dtype=torch.long)
    # randomizing might be better
    for i, _ in enumerate(padded):
        padded[i][:data[i][0].shape[0]] = data[i][0]
    return padded, labels, weights

def collate_fn_pad_batch(data):
    """Pad data in a batch.
    Parameters
    ----------
    data : list((tensor, int), )
        data and label in a batch
    Returns
    -------
    tuple(tensor, tensor)
    """
    max_len = max([i[0].shape[0] for i in data])
    labels = torch.tensor([i[1] for i in data], dtype=torch.long)
    padded = torch.zeros((len(data), max_len), dtype=torch.long)
    # randomizing might be better
    for i, _ in enumerate(padded):
        padded[i][:data[i][0].shape[0]] = data[i][0]
    return padded, labels
