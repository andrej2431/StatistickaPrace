# Štatistická práca
## Dáta
Dáta chorôb som získal z World Health Organization, špecificky tento API [https://www.who.int/data/gho/info/gho-odata-api](https://www.who.int/data/gho/info/gho-odata-api).  
Keďže niektoré mali len dáta v 2022 tak som sťahoval všetky dáta len v 2022.  
GDP krajín per capita som skopíroval na internete a spracoval.  
Pomocou pythonu som si stiahol všetky relevantné dáta v [data_download.py](./data_download.py).  
Následne som spracoval dáta do dataframu v [dataframe_generation.py](./dataframe_generation.py)

Ten som už daľej použil v [data_analysis.py](./data_analysis.py) kde je všetka analýza dát a generácia grafov ktorú budem používať.

## 

## Miera úmrtí na tuberkulózu s porovnaním s GDP per capita
**H0** - Nulová hypotéza je, že neexistuje korelácia medzi mierou úmrtnosti na tuberkulózu a GDP per capita  
**H1** - Nulová hypotéza je, že existuje korelácia medzi mierou úmrtnosti na tuberkulózu a GDP per capita

Na zistenie toho, či existuje nejaká korelácia medzi mierou úmrtí na dané choroby a GDP per capita použijem Pearsonov korelačný koeficient ktorý mi určí mieru lineárneho vzťahu medzi nimi.

hladinu významnosti použijem 0.05



### Kód
```python
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
```

### Výsledok
```
Tuberculosis:
Pearsonov korelačný koeficient: -0.05496085552305478
P-hodnota: 0.4525670299736609
Testová statistika t: -0.7527161185204676
Kritická hodnota t (dvojstranný test): 1.9727310334056902
```

### Uzáver
Korelačný koeficient je síce správne negatívny (viacej peniaz -> menej smrtí) ale je veľmi malý, čiže nie je štatisticky významný.  
P-hodnota je príliš veľká a teda nemôžeme zamietnuť nulovú hypotézu.  
Testová štatistika t sa nenachádza v kritickom obore (-1.9 < -0.75 < 1.9).  
Z toho vyplýva, že neexistuje štatisticky významná korelácia medzi mierou úmrtnosti na tuberkulózu a gdp per capita.


## Miera úmrtí na hepatitis B/C s porovnaním s GDP per capita
Použil som rovnaké predpoklady a kód ako s tuberkulózou

### Výsledok
```
Hepatitis B:
Pearsonov korelačný koeficient: -0.26099330361280265
P-hodnota: 0.0012088776803803384
Testová statistika t: -3.3002126287856344
Kritická hodnota t (dvojstranný test): 1.976013177679155

Hepatitis C:
Pearsonov korelačný koeficient: -0.07164677714315626
P-hodnota: 0.38040138948297514
Testová statistika t: -0.8797511296988669
Kritická hodnota t (dvojstranný test): 1.9759053308869137
```

### Uzáver Hepatitis B
Korelačný koeficient je štatisticky významný, aj keď nie veľmi silný, negatívny lineárny vzťah medzi gdp per capita a úmrtnosťou na hepatitis B.  
P-hodnota je výrazne menšia než 0.05 a teda je výsledok štatisticky významný.  
Testová štatistika t sa nenachádza v kritickom obore (-1.9 < -0.75 < 1.9).  
Z toho vyplýva, že neexistuje štatisticky významná korelácia medzi mierou úmrtnosti na tuberkulózu a gdp per capita.