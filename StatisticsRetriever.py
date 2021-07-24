import requests

# This is the request
api_endpoint = 'https://api.coronavirus.data.gov.uk/v1/data'
filters = 'filters=areaType=nation'
structure = 'structure={"date":"date","newCases":"newCasesByPublishDate"}'

class StatisticsRetriever:
    def __init__(self) -> None:
        self.json_data = None

    # Get fresh data and sanitise it
    def refresh_data(self) -> None:
        response = requests.get(api_endpoint + "?" + filters + "&" + structure, timeout=5)
        json = response.json()

        # The same date appears multiple times in the data but with different values
        summed = {}
        for entry in json["data"]:
            date = entry["date"]

            if date in summed.keys():
                summed[date] = summed[date] + entry["newCases"]
            else:
                summed[date] = entry["newCases"]
        
        self.json_data = summed
    
    def retrieve_data(self) -> dict or None:
        return self.json_data
