import json
def multiply_recursive(coordinate_list):
    if any([isinstance(i, list) for i in coordinate_list]):
        return [multiply_recursive(i) for i in coordinate_list]
    x,y = coordinate_list
    return [round(x*1000, 3), round(y*1000, 3)]

if __name__ == '__main__':
    with open("./ny_new_york_zip_codes_geo.min.json") as json_file:
        geojson = json.load(json_file)
        for f in geojson['features']:
            lst = multiply_recursive(f['geometry']['coordinates'])
            f['geometry']['coordinates'] = lst
    with open("./modified_ny_new_york_zip_codes_geo.min.json", 'w') as out_file:
        json.dump(geojson, out_file)
