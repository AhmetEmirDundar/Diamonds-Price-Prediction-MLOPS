import pickle
import pandas as pd


def main():
    path = "C:/Users/ahmet/PycharmProjects/DiamondPrice/diamond_model.pkl"

    with open(path, "rb") as f:
        saved_data = pickle.load(f)

    model = saved_data["model"]
    X_test_scaled = pd.read_csv("C:/Users/ahmet/PycharmProjects/DiamondPrice/30_test_data_scaled.csv")

    print(model.predict(X_test_scaled))

if __name__ == '__main__':
    main()