import sys

from com.conversion_rate_analysis import buildConversion, buildConversionInput, buildConversionHadoopShell, \
    buildConversionResult

if __name__ == '__main__':
    # 统计时间范围的开始时间，通过命令行参数传入
    start = sys.argv[1]

    # 统计时间范围的结束时间，通过命令行参数传入
    end = sys.argv[2]

    print('########## Phase 1 ##########')
    # 解析配置文件
    urls = buildConversion.resolve_conf()

    print('########## Phase 2 ##########')
    # 提取所需数据
    buildConversionInput.extract_data(start, end)

    print('########## Phase 3 ##########')
    # 通过MapReduce进行统计
    buildConversionHadoopShell.count_urls(start, end, urls)

    print('########## Phase 4 ##########')
    # 对中间结果进行汇总并得到最后结果表
    buildConversionResult.get_result(start, end, "/user/hive/warehouse/conversion_out")
