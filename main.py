from GetDataCMEMS import GetDataCMEMS


# # Set the download parameters(Just modify on this block)
"""
Account information
"""
username = "Your username"
password = "Your password"

"""
option: Check in https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/services
"""
dataset_id = "cmems_mod_glo_phy_my_0.083deg_P1D-m"

"""
option:
thetao: potential temperature [℃]
so: Salinity [psu]
uo: Eastward ocean current velocity [m/s]
vo: Northward ocean current velocity [m/s]
zos: Sea surface height [m]
mlotst: Mixed layer thickness [m]
"""
variable_list = ["vo"]

"""
longitude: -180, 180
latitude: -90, 90

"""
minimum_longitude = 90
maximum_longitude = 130
minimum_latitude = -5
maximum_latitude = 30

"""
. The interim datasets cover 01/07/2021 to M-4 period.
"""
start_time = "1996-09"
end_time = "1996-09"

"""
'Y': one year per data
'M': one month per data
"""
download_type = 'M'  # 'Y' or 'M'

"""
[0.49402499198913574, 5727.9169921875]
"""
minimum_depth = 0.49402499198913574
maximum_depth = 5727.9169921875

"""
Your output directory
"""
output_directory = r'C:\Users\admin\Desktop'

# Reconstitution
spacial_range = [minimum_longitude, maximum_longitude, minimum_latitude, maximum_latitude]
time_range = [start_time, end_time]
depth_range = [minimum_depth, maximum_depth]

# Execute
data_downloader = GetDataCMEMS(username, password, dataset_id, variable_list, spacial_range, time_range, download_type,
                               depth_range, output_directory)
data_downloader.download()
