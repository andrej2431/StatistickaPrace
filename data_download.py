import requests
from time import sleep
import json

indicators = {
    "tuberculosis_deaths": "Number of deaths due to tuberculosis, excluding HIV",
    "hepatitis_B_deaths": "Deaths caused by chronic hepatitis B (HBV) infection (number)",
    "hepatitis_C_deaths": "Deaths caused by chronic hepatitis C (HCV) infection (number)"
}


def get_indicator_code(indicator):
    url = f"https://ghoapi.azureedge.net/api/Indicator?$filter=IndicatorName eq '{indicator}'"
    r = requests.get(url)
    if r.status_code != 200:
        return None

    response_json = r.json()
    if 'value' in response_json and len(response_json['value']) > 0 and 'IndicatorCode' in response_json['value'][0]:
        return response_json['value'][0]['IndicatorCode']
    else:
        return None


def store_indicator_data(indicator_code, output_filename):
    url = f"https://ghoapi.azureedge.net/api/{indicator_code}"
    r = requests.get(url)
    if r.status_code != 200:
        return None

    with open(output_filename, 'w') as json_file:
        json_file.write(r.text)


def store_indicators():
    for name, indicator in indicators.items():
        indicator_code = get_indicator_code(indicator)
        if indicator_code is not None:
            filename = f"data/{name}.json"
            store_indicator_data(indicator_code, filename)
        else:
            print(f"failed to get indicator code for {indicator}")
        sleep(0.1)


if __name__ == '__main__':
    store_indicators()
