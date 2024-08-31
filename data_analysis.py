from dataframe_generation import gdp_and_death_rate_df
import scipy.stats as stats
import math

base_df = gdp_and_death_rate_df()


def pearson_correlation(disease):
    df = base_df.dropna(subset=['GDP', disease])
    corr, p_value = stats.pearsonr(df['GDP'], df[disease])

    n = len(df)
    t = corr * math.sqrt(n - 2) / math.sqrt(1 - corr ** 2)
    critical_value = stats.t.ppf(1 - 0.025, n - 2)

    print(f"Pearsonov korelačný koeficient: {corr}")
    print(f"P-hodnota: {p_value}")
    print(f"Testová statistika t: {t}")
    print(f"Kritická hodnota t (dvojstranný test): {critical_value}")


def all_pearson_correlations():
    print("Pearsonová korelácia")
    print("Tuberculosis:")
    pearson_correlation('tuberculosis')

    print("\nHepatitis B:")
    pearson_correlation('hepatitis_B')

    print("\nHepatitis C:")
    pearson_correlation('hepatitis_C')


def generate_graphs():
    pass


if __name__ == "__main__":
    all_pearson_correlations()
