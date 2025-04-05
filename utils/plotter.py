import matplotlib.pyplot as plt

def plot_data(data, title="Fitness Progress"):
    plt.figure(figsize=(10, 5))
    plt.plot(data, marker="o")
    plt.title(title)
    plt.xlabel("Days")
    plt.ylabel("Progress")
    plt.grid(True)
    plt.show()
