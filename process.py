#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import os
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def process(input_dir, output_dir):
    if not os.path.isdir(input_dir):
        print("Input directory {0} does not exist".format(input_dir))
    if not os.path.isdir(output_dir):
        print("Create output directory: {0}".format(output_dir))
        os.mkdir(output_dir)

    for item in os.walk(input_dir):
        path, file_list = item[0], item[2]
        for i, file in enumerate(file_list):
            df = pd.DataFrame.from_csv(os.path.join(path, file), index_col=3).iloc[:, 3:4]
            df = df.rename(columns = {"Unnamed: 4": "Y"})
            df = df.loc[(df.index > 1.4e-05) & (df.index < 2.4e-5)]
            # save to file
            df.to_csv(os.path.join(output_dir, file))
            # plot figure
            df["Y"].plot(label=file)
            plt.legend()
        plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="process file")
    parser.add_argument("input_dir", help="directory contains files to process")
    parser.add_argument("output_dir", help="directory contains files to save")
    args = parser.parse_args()

    process(args.input_dir, args.output_dir)

