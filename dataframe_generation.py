import json
import pandas


def death_rate_df(disease):
    populations = country_populations()
    with open(f"data/{disease}_deaths.json", 'r') as file:
        deaths_data = json.load(file)

    death_rate_list = []
    for death in deaths_data["value"]:
        year = death["TimeDim"]
        country = death["SpatialDim"]
        death_count = death["NumericValue"]

        if year != 2022 or country not in populations:
            continue

        death_rate = death_count / populations[country]

        death_rate_list.append({
            "Country Code": country,
            f"{disease}": death_rate
        })

    df = pandas.DataFrame(death_rate_list, columns=["Country Code", f"{disease}"])
    return df


def gdp_df():
    df = pandas.read_csv("data/gdp_pcap.csv")[["Country Code", "2022"]]
    df.rename(columns={"2022": "GDP"}, inplace=True)
    df = df.dropna(subset=["GDP"])
    return df


def country_populations():
    df = pandas.read_csv("data/population.csv")[["Country Code", "2022"]]
    df.rename(columns={"2022": "Population"}, inplace=True)
    df = df.dropna(subset=["Population"])
    return df.set_index('Country Code')['Population'].to_dict()


def gdp_and_death_rate_df():
    main_df = gdp_df()
    for disease in ["tuberculosis", "hepatitis_B", "hepatitis_C"]:
        df = death_rate_df(disease)
        main_df = pandas.merge(main_df, df, on="Country Code", how="left")

    return main_df


if __name__ == "__main__":
    print(gdp_and_death_rate_df())
