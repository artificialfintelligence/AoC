# pylint: disable=missing-module-docstring, missing-docstring
import os

from aocd import get_data


def load_data(day: int, year: int, is_testmode: bool) -> list[str]:
    data_filename_no_ext = os.path.splitext(os.path.basename(__file__))[0]
    if is_testmode:
        data_filename_no_ext += "_test"
    data_file_path = os.path.join("data", f"{data_filename_no_ext}.txt")
    if os.path.isfile(data_file_path):
        print(f"Using local data file {data_file_path}...")
        with open(data_file_path, "r", encoding="utf-8") as f:
            data = f.read()
    else:
        if is_testmode:
            raise FileNotFoundError(
                f"Test data must be manually saved to {data_file_path} first."
            )
        print("Local data file not found. Downloading and saving data...")
        data = get_data(day=day, year=year)
        with open(data_file_path, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"Data succesfully downloaded and saved to {data_file_path}.")
    return data
