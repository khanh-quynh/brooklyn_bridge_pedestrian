import csv

def main():
    # read file
    f = open("./data/raw_data.csv","r")
    csv_reader = csv.DictReader(f)
    csv_list = list(csv_reader)
    
    # new dataset: year, season, time, total_pedestrian, to_manhattan, to_brooklyn, weather_summary, event
    month_list = []
    year_list = []
    time_list = []
    for line in csv_list:
        date = line['hour_beginning']
        month_list.append(int(date[:2]))
        year_list.append(int(date[6:10]))
        time_list.append(date[11:])
    
    #new column: season
    season_list = []
    for m in month_list:
        if 3<=m<= 5:
            season_list.append('Spring')
        elif 6<=m<=8:
            season_list.append('Summer')
        elif 9<=m<=11:
            season_list.append('Fall')
        else:
            season_list.append('Winter')

    #columns unchanged: pedestrians, towards_manhattan, towards_brooklyn, event, weather_summary
    def take_col(col_name):
        list_col = []
        for line in csv_list:
            list_col.append(line[col_name])
        return list_col

    total_pedes_list = take_col('Pedestrians')
    to_manh_list = take_col('Towards Manhattan')
    to_bk_list = take_col('Towards Brooklyn')
    event_list = take_col('events')
    weather0_list = take_col('weather_summary')

    weather_list = []
    for w in weather0_list:
        w = w.replace("-"," ")
        weather_list.append(w)

    #clean_data.csv
    d = open('./data/clean_data.csv', 'w',encoding='utf-8')
    columns = ['year','season','time','total_pedestrian',
               'to_manhattan','to_brooklyn','weather','event']

    data_dict = []
    for i in range(len(year_list)):
        data_dict.append({
            "year": year_list[i],
            "season": season_list[i],
            "time": time_list[i],
            "total_pedestrian": total_pedes_list[i],
            "to_manhattan": to_manh_list[i],
            "to_brooklyn": to_bk_list[i],
            "weather": weather_list[i],
            "event": event_list[i]})

    dict_writer = csv.DictWriter(d, fieldnames=columns)
    dict_writer.writeheader()
    for data in data_dict:
        dict_writer.writerow(data)
    f.close()

if __name__ == "__main__":
    main()
