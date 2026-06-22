import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-3, 10, 100) # 100 evenly spaced numbers between 0.1 and 10
Y = np.exp(-X) + np.random.normal(0, 0.1, size=X.shape) # y = exp(-x) + noise

W1 = np.random.rand(2) # Random initial weight
B1 = np.random.rand(2)

W2 = np.random.rand(2) # Random initial weight
B2 = np.random.rand()

#model = lambda x: np.matmul(np.maximum(0, W1 * x + B1), W2) + B2

def model(x):
    Y = np.zeros_like(x)
    for i in range(len(x)):
        # First layer
        z1 = W1 * x[i] + B1
        a1 = np.maximum(0, z1)  # ReLU activation

        # Second layer
        z2 = np.dot(a1, W2) + B2
        Y[i] = z2
    return Y

eta = 5e-3 # Learning rate
for epoch in range(5000):
    loss = np.mean((Y - model(X))**2) # Mean Squared Error
    print(f'Epoch {epoch+1}, Loss: {loss}')

    # Backpropagation
    dYhat = 2 * (model(X) - Y) / len(Y) # Derivative of loss w.r.t. predictions

    dW2 = np.array([np.sum(dYhat * np.maximum(0, W1[0] * X + B1[0])), np.sum(dYhat * np.maximum(0, W1[1] * X + B1[1]))])
    dB2 = np.sum(dYhat)

    dA1 = dYhat[:, None] * W2 # Derivative of loss w.r.t. activations
    dZ1 = dA1 * ((W1 * X[:, None] + B1) > 0) # Derivative of ReLU

    dW1 = np.array([np.sum(dZ1[:, 0] * X), np.sum(dZ1[:, 1] * X)])
    dB1 = np.sum(dZ1, axis=0)

    # Update weights and biases
    W2 -= eta * dW2
    B2 -= eta * dB2
    W1 -= eta * dW1
    B1 -= eta * dB1

print(f'Final weights: W1 = {W1}, B1 = {B1}, W2 = {W2}, B2 = {B2}')

plt.scatter(X, Y, color='blue', label='Data', s=5)
plt.plot(X, model(X), color='red', label='Model Prediction')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data and Model Prediction')
plt.legend()

plt.show()


##################
'''
fig, ax = plt.subplots(1, 3)
fig.set_size_inches(19.2, 4.8)

originalReLU = np.maximum(0, X)
ax[0].plot(X, originalReLU, label='ReLU')
ax[0].set_title('Original ReLU Function')
ax[0].set_xlim([-10, 10])
ax[0].set_ylim([-0.5, 10])
w1,w2 = 2, 0.1
b1,b2 = 4, 3



Stage1ReLU = np.maximum(0, w1 * X + b1)
ax[1].plot(X, Stage1ReLU, label='Stage 1 ReLU')
ax[1].set_title('Stage 2 Output')
ax[1].set_xlim([-10, 10])
ax[1].set_ylim([-0.5, 10])

Stage2ReLU = w2 * Stage1ReLU + b2
ax[2].plot(X, Stage2ReLU, label='Stage 2 ReLU')
ax[2].set_title('Stage 3 Output')
ax[2].set_xlim([-10, 10])
ax[2].set_ylim([-0.5, 10])
plt.savefig('Neural Networks/Media/ReLU.png')
plt.show()
'''