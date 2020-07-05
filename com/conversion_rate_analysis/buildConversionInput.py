from com.utils.HiveUtil import HiveUtil


def extract_data(start, end):
    hql = "\"insert into table conversion_input partition (dt='" + start + "-" + end + "') " \
           "select url,uniqueid as uuid,sessionid,csvp from clickstream_log where dt>= '" + start + "' and dt<= '" + end + "'\""
    print(hql)
    HiveUtil.execute_shell(hql)
