import json
import pandas


def death_rate_df(disease):
    with open(f"data/{disease}_cases.json", 'r') as file:
        cases_data = json.load(file)

    with open(f"data/{disease}_deaths.json", 'r') as file:
        deaths_data = json.load(file)

    cases_by_country = {}
    for case in cases_data["value"]:
        year = case["TimeDim"]
        country = case["SpatialDim"]
        case_count = case["NumericValue"]

        if year != 2022:
            continue

        cases_by_country[country] = case_count  # stores number of cases

    death_rate_list = []
    for death in deaths_data["value"]:
        year = death["TimeDim"]
        country = death["SpatialDim"]
        death_count = death["NumericValue"]

        if year != 2022:
            continue

        if cases_by_country[country] == 0:
            death_rate = 0
        else:
            death_rate = death_count / cases_by_country[country]

        death_rate_list.append({
            "Country Code": country,
            f"{disease}": death_rate
        })

    df = pandas.DataFrame(death_rate_list, columns=["Country Code", f"{disease}"])
    return df


def gdp_df():
    df = pandas.read_csv("data/gdp_data.csv", skiprows=4)[["Country Code", "2022"]]
    df.rename(columns={"2022": "GDP"}, inplace=True)
    df = df.dropna(subset=["GDP"])
    return df


def gdp_and_death_rate_df():
    main_df = gdp_df()
    for disease in ["tuberculosis", "hepatitis_B", "hepatitis_C"]:
        df = death_rate_df(disease)
        main_df = pandas.merge(main_df, df, on="Country Code", how="left")

    return main_df


if __name__ == "__main__":
    print(gdp_and_death_rate_df())
