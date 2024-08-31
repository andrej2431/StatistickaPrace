from dataframe_generation import gdp_and_death_rate_df
import matplotlib.pyplot as plt
import seaborn as sns

base_df = gdp_and_death_rate_df()


def disease_gdp_plot(disease):
    df_cleaned = base_df.dropna(subset=['GDP', disease])
    sns.scatterplot(x="GDP", y=disease, data=df_cleaned)

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("GDP per capita")
    plt.ylabel(f"{disease} Death rate")
    plt.title(f"{disease} Death rate by GDP per capita")

    plt.tight_layout()
    plt.show()


def disease_ordered_gdp_plot(disease):
    df_cleaned = base_df.dropna(subset=['GDP', disease])
    lower_bound = df_cleaned[disease].quantile(5 / 100)
    upper_bound = df_cleaned[disease].quantile(95 / 100)
    df_filtered = df_cleaned[(df_cleaned[disease] >= lower_bound) & (df_cleaned[disease] <= upper_bound)]

    df_sorted = df_filtered.sort_values(by='GDP')
    sns.lineplot(x=range(len(df_sorted)), y=df_sorted[disease])

    plt.xlabel('GDP per capita order')
    plt.ylabel(f'{disease} Death rate')
    plt.title(f'{disease} Death rate by GDP Order')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    for disease in ["tuberculosis", "hepatitis_B", "hepatitis_C"]:
        #disease_gdp_plot(disease)
  #      disease_ordered_gdp_plot(disease)
        df_sorted = base_df.sort_values(by=disease, ascending=False)
        print(f"Top 5 highest death counts for {disease.replace('_', ' ').title()}:")
        print(df_sorted[['Country Code', 'GDP', disease]].head(5))