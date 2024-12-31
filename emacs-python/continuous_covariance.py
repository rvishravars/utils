import numpy as np
import matplotlib.pyplot as plt

def generate_data(seed: int = 0, size: int = 1000) -> tuple[np.ndarray, np.ndarray]:
    np.random.seed(seed)
    x = np.random.normal(0, 1, size)
    y = 2 * x + np.random.normal(0, 1, size)
    return x, y

def calculate_covariance(x: np.ndarray, y: np.ndarray) -> float:
    cov_matrix = np.cov(x, y)
    return cov_matrix[0, 1]

def plot_data(x: np.ndarray, y: np.ndarray) -> None:
    plt.hexbin(x, y, gridsize=50, cmap='Blues')
    plt.colorbar(label='count in bin')
    plt.title('Hexbin plot of x and y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main() -> None:
    x, y = generate_data()
    cov_xy = calculate_covariance(x, y)
    print(f"Covariance between x and y: {cov_xy}")
    plot_data(x, y)

if __name__ == "__main__":
    main()
    plt.figure()
    plt.title('Covariance Matrix')
    plt.imshow(np.cov(x, y), cmap='coolwarm', interpolation='none')
    plt.colorbar()
    plt.xticks([0, 1], ['x', 'y'])
    plt.yticks([0, 1], ['x', 'y'])
    plt.show()