import pandas as pd


def remove_duplicates(input_file, output_file):
    df = pd.read_csv(input_file)
    cleaned_df = df.drop_duplicates()
    cleaned_df.to_csv(output_file, index=False)
    return cleaned_df


if __name__ == "__main__":
    remove_duplicates("data/raw_dataset.csv", "data/processed_dataset.csv")
    print("Duplicate rows removed successfully.")
