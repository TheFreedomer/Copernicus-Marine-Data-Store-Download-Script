import pandas as pd
import copernicusmarine as cm
import os


class GetDataCMEMS:
    """
    2021 -- 2024
    """
    def __init__(self, username, password, dataset_id,
                 variable_list, spacial_range, time_range, download_type,
                 depth_range, output_directory):
        """

        :param username:
        :param password:
        :param dataset_id:
        :param variable_list:
        :param spacial_range:
        :param time_range:
        :param download_type:
        :param depth_range:
        :param output_directory:
        """
        self.username = username
        self.password = password
        self.dataset_id = dataset_id
        self.variable_list = variable_list
        self.minimum_longitude = spacial_range[0]
        self.maximum_longitude = spacial_range[1]
        self.minimum_latitude = spacial_range[2]
        self.maximum_latitude = spacial_range[3]
        self.time_start = pd.to_datetime(time_range[0])
        self.time_end = pd.to_datetime(time_range[1])
        self.download_type = download_type
        self.minimum_depth = depth_range[0]
        self.maximum_depth = depth_range[1]
        self.output_directory = output_directory

    def get_date_tuple(self):
        """

        :return:
        """
        if self.download_type == "Y":
            date_temp = pd.date_range(start=self.time_start, end=self.time_end, freq='YS')
            date_target = [(d.strftime('%Y-%m-%dT%H:%M:%S'),
                            (d + pd.DateOffset(years=1) - pd.Timedelta('1s')).strftime('%Y-%m-%dT%H:%M:%S'))
                           for d in date_temp]
            return date_target

        elif self.download_type == "M":
            date_temp = pd.date_range(start=self.time_start, end=self.time_end, freq='MS')
            date_target = [(d.strftime('%Y-%m-%dT%H:%M:%S'),
                            (d + pd.DateOffset(months=1) - pd.Timedelta('1s')).strftime('%Y-%m-%dT%H:%M:%S'))
                           for d in date_temp]
            return date_target

        else:
            raise "DownTypeError: Please input 'M' or 'Y'!"

    def download(self):
        """

        :return:
        """
        # Get all filename of output directory
        file_exist = os.listdir(self.output_directory)

        if self.download_type == "Y":
            date_tuple = self.get_date_tuple()
            for time_start, time_end in date_tuple:
                filename = time_start[0:4] + ".nc"
                print(filename + ">>>")
                if filename in file_exist:
                    print(filename + " is exist!")
                    continue
                cm.subset(
                    username="your username",
                    password="your password",
                    dataset_id=self.dataset_id,
                    variables=self.variable_list,
                    minimum_longitude=self.minimum_longitude,
                    maximum_longitude=self.maximum_longitude,
                    minimum_latitude=self.minimum_latitude,
                    maximum_latitude=self.maximum_latitude,
                    start_datetime=time_start,
                    end_datetime=time_end,
                    minimum_depth=self.minimum_depth,
                    maximum_depth=self.maximum_depth,
                    output_filename=filename,
                    output_directory=self.output_directory,
                    force_download=True
                )
        else:
            date_tuple = self.get_date_tuple()
            for time_start, time_end in date_tuple:
                filename = time_start[0:4] + '_' + time_start[5:7] + ".nc"
                print(filename + ">>>")
                if filename in file_exist:
                    print(filename + " is exist!")
                    continue
                cm.subset(
                    username=self.username,
                    password=self.password,
                    dataset_id=self.dataset_id,
                    variables=self.variable_list,
                    minimum_longitude=self.minimum_longitude,
                    maximum_longitude=self.maximum_longitude,
                    minimum_latitude=self.minimum_latitude,
                    maximum_latitude=self.maximum_latitude,
                    start_datetime=time_start,
                    end_datetime=time_end,
                    minimum_depth=self.minimum_depth,
                    maximum_depth=self.maximum_depth,
                    output_filename=filename,
                    output_directory=self.output_directory,
                    force_download=True
                )


if __name__ == "__main__":
    pass
