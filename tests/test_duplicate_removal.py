import pandas as pd
from src.duplicate_removal import remove_duplicates


def test_remove_duplicates(tmp_path):

    input_file = tmp_path / "input.csv"
    output_file = tmp_path / "output.csv"

    test_data = pd.DataFrame({
        "age": [40, 49, 49, 37],
        "sex": [1, 0, 0, 1]
    })

    test_data.to_csv(input_file, index=False)

    cleaned_df = remove_duplicates(input_file, output_file)

    assert len(cleaned_df) == 3
    assert cleaned_df.duplicated().sum() == 0
