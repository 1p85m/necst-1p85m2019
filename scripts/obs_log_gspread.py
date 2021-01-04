#! /usr/bin/env python3

name = 'obs_log_gspread'

import pandas as pd
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials
from std_msgs.msg import String
from std_msgs.msg import Float64


class obs_log_gspread(object):


    def __init__(self):

        json = "/home/exito/ros/src/necst-sisrx_b67/lib/observation-log-c7a8ff4b5240.json"
        spread_sheet_key = "1WPOyaK7iekOK-Hk6jNLBMzsWRHGHifUyiecQI-ogwUc"
        self.ws = self.connect_gspread(json,spread_sheet_key)

        rospy.Subscriber("/obs_log/date_time",String,self.date)
        rospy.Subscriber("/obs_log/logger_path",String,self.logger_path)


    def connect_gspread(self,json,key):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(json,scope)
        gc = gspread.authorize(credentials)
        SPREADSHEET_KEY = key
        worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
        return worksheet


    def date(self,q):
        date = q.data
        Y = date[:4]
        m = date[4:6]
        d = date[6:8]
        H = date[9:11]
        M = date[11:13]
        S = date[13:15]
        self.date_time = Y+'/'+m+'/'+d+' '+H+':'+M+':'+S
        return


    def logger_path(self,q):
        self.logger_path = q.data
        return


    def toAlpha(num):
        if num<=26:
            return chr(64+num)
        elif num%26==0:
            return toAlpha(num//26-1)+chr(90)
        else:
            return toAlpha(num//26)+chr(64+num%26)


    def write_log(self):
        df1 = pd.DataFrame(self.ws.get_all_values())
        df1.columns = list(df.loc[0, :])
        df1.drop(0, inplace=True)
        df1.reset_index(inplace=True)
        df1.drop('index', axis=1, inplace=True)
        df2 = df1.append({'date time':self.date_time,'logger path':self.logger_path},ignore_index=True)

        col_lastnum = len(df2.columns) # DataFrameの列数
        row_lastnum = len(df2.index)   # DataFrameの行数

        cell_list = self.ws.range('A1:'+toAlpha(col_lastnum)+str(row_lastnum+1))
        for cell in cell_list:
            if cell.row == 1:
                val = df2.columns[cell.col-1]
            else:
                val = df2.iloc[cell.row-2][cell.col-1]
            cell.value = val

        self.ws.update_cells(cell_list)


    def regist_gspread(self):
        while not rospy.is_shutdown():
            self.write_log()
            time.sleep(3)
            continue
            
            
    def thread(self):
        th = threading.Thread(target=self.regist_gspread)
        th.setDaemon(True)
        th.start()


if __name__=='__main__':
    rospy.init_node(name)
    olg = obs_log_gspread()
    olg.thread()
    rospy.spin()
