n_clusters = 10

input_dim = 784
latent_dim = 10

n_epochs = 3
batch_size = 100

encoder_hidden_size = [500, 500, 2000]
decoder_hidden_size = [2000, 500, 500]

global_step = 0
adam_nn_learning_rate = 0.002
adam_nn_epsilon = 1e-04