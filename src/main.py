# read csv into df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from constants import *
from glob import glob
from datetime import datetime
import os

def read_data():
    print(DATA_GLOB_PLANINSKE_MAKRO_ALL)

    df = pd.DataFrame(columns=['datum', "location_id", "pretocnost"])

    LOCATION_DICT = {
        "kum": 0,
        "lovrenška_jezera": 1,
        "osp": 2,
        "storžič": 3,
        "triglavski_narodni_park": 4,
        "vršič": 5,
    }

    for path in glob(DATA_GLOB_PLANINSKE_MAKRO_ALL):
        print(path)

        # get file name without extension and path
        file_name = os.path.basename(path).split('.')[0].lower().replace(" ", "_")
        if file_name == "zdruzeno":
            continue
        
        # file_name = path.split('/')[-1].split('.')[0].replace(" ", "_").lower()
        assert file_name in LOCATION_DICT.keys(), f"file_name = {file_name}"
        print(file_name)
        location_id = LOCATION_DICT[file_name]

        df_planine = pd.read_csv(path, sep=',', encoding='UTF-8')
        assert df_planine.columns[0] == 'datum', f"columns[0] = {df_planine.columns[0]}"
        assert df_planine.columns[1] == 'vhodi', f"columns[1] = {df_planine.columns[1]}"
        assert df_planine.columns[2] == 'izhodi', f"columns[2] = {df_planine.columns[2]}"
        # print(df_planine.head())
        
        # sum vhodi and izhodi
        df_planine['pretocnost'] = df_planine['vhodi'] + df_planine['izhodi']
        # drop "vhodi" and "izhodi" columns
        df_planine = df_planine.drop(columns=['vhodi', 'izhodi'])

        # add "location_id" column
        df_planine['location_id'] = location_id

        df = pd.concat([df, df_planine], ignore_index=True)

        # sum vhodi and izhodi based on "datum_dan"
        # df_planine = df_planine.groupby('datum').sum()
        print(df_planine.head())

        
        # break

    df = df.sort_values(by=['datum', 'location_id'])
    print(df.head())

    df.to_csv(OUT_PLANINSTVO, index=False)




def main():
    # load data
    df = pd.read_csv(OUT_PLANINSTVO, sep=',', encoding='UTF-8')
    print(df.head())


if __name__ == '__main__':
    main()
