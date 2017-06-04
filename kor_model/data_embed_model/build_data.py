from kor_model.data_embed_model.data_utils import CoNLLDataset


def build_data(config):
    """
    Procedure to build data

    Args:
        config: defines attributes needed in the function
    Returns:
        creates vocab files from the datasets
        creates a npz embedding file from trimmed glove vectors
    """

    # Generators
    dev   = CoNLLDataset(config.dev_filename)
    test  = CoNLLDataset(config.test_filename)
    train = CoNLLDataset(config.train_filename)


    for a in dev:
        print(a)

