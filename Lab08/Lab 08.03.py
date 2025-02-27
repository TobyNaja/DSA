import json
def findstation(city_list,station):
    city_list = set(city_list)
    ans_list = []
    
    while city_list:
        best_station = None
        max_cover = 0
        best_cover_cities = set()
        
        for name, cities in station.items():
            cover_cities = city_list.intersection(set(cities))
            if len(cover_cities) > max_cover:
                max_cover = len(cover_cities)
                best_station = name
                best_cover_cities = cover_cities
        
        if best_station:
            ans_list.append(best_station)
            city_list -= best_cover_cities
        else:
            break
    
    return ans_list

def main():
    city_list = json.loads(input())
    stations = {}
    num = int(input())
    for _ in range(num):
        station = json.loads(input())
        stations[station["Name"]] = station["Cities"]
    ans = findstation(city_list, stations)
    ans.sort(reverse=False)
    print(ans)

main()