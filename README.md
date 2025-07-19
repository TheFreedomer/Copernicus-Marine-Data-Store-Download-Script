# Copernicus-Marine-Data-Store-Download-Script
该项目实现了自动化下载哥白尼海洋数据存储系统中的数据，具体而言就是数据下载脚本，能够解放双手，提高下载效率  
The project has automated the downloading of data from the Copernicus Marine Data Store, specifically through data download scripts, freeing up manual effort and improving download efficiency.  
## 项目结构  
- CMEMS-GLO-PUM-001-030.pdf：Copernicus Marine Data Store的详细信息pdf文件
- check_data.py：用于检查已下载数据的完整（因为远程下载的数据未必完整）
- GetDataCMEMS.py：用于实现下载逻辑的类
- main.py：下载入口
## 依赖库  
需要确保python环境中安装了以下库：  
- copernicusmarine
- pandas
- netCDF4<br>
安装命令>>><br>
```
pip install copernicusmarine
pip install pandas
pip install netCDF4
```
由于copernicusmarine库需要经常更新，否则可能无法正常使用API  
更新命令如下>>><br>
```
pip install --upgrade copernicusmarine
```
## 使用说明<br>
请参考main.py文件中的示例，里面有详细介绍<br>
需要结合信息https://data.marine.copernicus.eu/product/GLOBAL_MULTIYEAR_PHY_001_030/services<br>
下载参数包括>>>
- username：哥白尼账号对应的用户名
- password：哥白尼账号对应的密码
- dataset_id：数据集id
- variable_list：所需下载变量列表
- spacial_range：空间范围
- time_range：时间范围
- download_type：下载类型（"M"为每月的所有数据保存为一个文件，"Y"为每年的所有数据保存为一个文件）
- depth_range：深度范围
- output_directory：下载到指定文件夹
