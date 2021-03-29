from wwo_hist import retrieve_hist_data
import os
os.chdir(".\weatherAPI")

frequency = 3
start_date = '11-DEC-2018'
end_date = '11-MAR-2019'
api_key = 'YOUR_API_KEY'
location_list = ['singapore','california']
hist_weather_data = retrieve_hist_data(api_key,
                                location_list,
                                start_date,
                                end_date,
                                frequency,
                                location_label = False,
                                export_csv = True,
                                store_df = True)