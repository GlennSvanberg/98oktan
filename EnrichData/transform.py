import json
from datetime import date

today = date.today()
today_str = today.strftime("%Y-%m-%d")


outlist = []
with open('res.json') as json_file:
    stations = json.load(json_file)
    print("stations", len(stations))
    for index, station in enumerate(stations):
        try:

            out = {}
            out["station"] = station["Station"]
            out["city"] = station["City"].title().rstrip(",")
            address_components = station["location"]["address_components"]
            for comp in address_components:
                if "route" in comp["types"]:
                    out["short_address"] = comp["short_name"].title()
            out["formatted_address"] = station["location"]["formatted_address"]
            out["position"] = station["location"]["geometry"]["location"]
            out["place_id"] = station["location"]["place_id"]
            out["oktan"] = station["Oktan"]
            out["source"] = station["Source"]
            out["distance"] = 0
            out["updated"] = today_str
            match = False

            for o in outlist:
                if o["formatted_address"] == out["formatted_address"]:
                    print("skipping: ", o["station"], o["formatted_address"])
                    print("o", json.dumps(out))
                    print("out", json.dumps(out))
                    match = True
                    break
            if not match:
                print(index)
                outlist.append(out)

        except:
            print("FAILED FOR STATION: unknown")


f = open("stations.json", "w", encoding="utf-8")
f.write(json.dumps(outlist))
f.close()


# DATA MODEL
"""
    {
        "station": "Preem",
        "short_address": "G\u00f6teborg",
        "formatted_address": "Rantorget 1, 416 64 Gothenburg, Sweden",
        "position": {
            "lat": 57.7087521,
            "lng": 11.9923221
        },
        "place_id": "ChIJlbCfcH_zT0YRCpZs9v6VUvs",
        "oktan": "Ja",
        "source": "https://www.preem.se/hitta-station#filters=f-1-3",
        "distance": 0
    },

"""

# NEW DATA
"""
 {
        "Station": "OKQ8",
        "City": "Uddevalla,",
        "Adress": "Trumpetv\u00e4gen 1",
        "Oktan": "Ja",
        "Source": "https://www.okq8.se/pa-stationen/bensinstationer/uddevalla-trumpetvagen/",
        "location": {
            "address_components": [
                {
                    "long_name": "1",
                    "short_name": "1",
                    "types": [
                        "street_number"
                    ]
                },
                {
                    "long_name": "Trumpetv\u00e4gen",
                    "short_name": "Trumpetv\u00e4gen",
                    "types": [
                        "route"
                    ]
                },
                {
                    "long_name": "Ramner\u00f6d",
                    "short_name": "Ramner\u00f6d",
                    "types": [
                        "political",
                        "sublocality",
                        "sublocality_level_1"
                    ]
                },
                {
                    "long_name": "Uddevalla",
                    "short_name": "Uddevalla",
                    "types": [
                        "postal_town"
                    ]
                },
                {
                    "long_name": "V\u00e4stra G\u00f6talands l\u00e4n",
                    "short_name": "V\u00e4stra G\u00f6talands l\u00e4n",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "Sweden",
                    "short_name": "SE",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "451 62",
                    "short_name": "451 62",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "Trumpetv\u00e4gen 1, 451 62 Uddevalla, Sweden",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 58.3661018,
                        "lng": 11.9307579
                    },
                    "southwest": {
                        "lat": 58.36558369999999,
                        "lng": 11.9296832
                    }
                },
                "location": {
                    "lat": 58.36584970000001,
                    "lng": 11.9302295
                },
                "location_type": "GEOMETRIC_CENTER",
                "viewport": {
                    "northeast": {
                        "lat": 58.36719173029149,
                        "lng": 11.9315695302915
                    },
                    "southwest": {
                        "lat": 58.36449376970848,
                        "lng": 11.9288715697085
                    }
                }
            },
            "place_id": "ChIJ4QO-NFYFRUYR9kyybMywZjk",
            "types": [
                "premise"
            ]
        }
    },

"""
