# import package
import requests
import pandas as pd
import numpy as np

def get_IPO_list():
    res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")
    df = pd.read_html(res.text)[0]
    # 設定column名稱
    df.columns = pd.Series(['name', 'ISIN_Code', 'start_day', 'category', 'industry', 'CFICode', 'note']) 
    df = df.iloc[1:] # 刪除第一行
    df = df.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1) # 先移除row，再移除column，超過三個NaN則移除
    df["No"] = df["name"].str.split("　", n = 1, expand = True).iloc[:,[0]]
    df["name"] = df["name"].str.split("　", n = 1, expand = True).iloc[:,[1]]
    df = df.set_index('No')
    indexNames = df[df['ISIN_Code'] == df['start_day']].index
    df.drop(indexNames , inplace=True)
    df.to_csv("IPO_list.csv", header = True)
    return df


def get_OTC_list():
    res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=4")
    df = pd.read_html(res.text)[0]
    # 設定column名稱
    df.columns = pd.Series(['name', 'ISIN_Code', 'start_day', 'category', 'industry', 'CFICode', 'note']) 
    df = df.iloc[1:] # 刪除第一行
    df = df.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1) # 先移除row，再移除column，超過三個NaN則移除
    df["No"] = df["name"].str.split("　", n = 1, expand = True).iloc[:,[0]]
    df["name"] = df["name"].str.split("　", n = 1, expand = True).iloc[:,[1]]
    df = df.set_index('No')
    indexNames = df[df['ISIN_Code'] == df['start_day']].index
    df.drop(indexNames , inplace=True)
    df.to_csv("OTC_list.csv", header = True)
    return df

get_IPO_list()
get_OTC_list()
