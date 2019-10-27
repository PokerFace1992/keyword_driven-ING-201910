# encoding=utf8
from util.dir_operation import make_current_date_dir, make_current_hour_dir
from util.excel import *
from action.keyword_action import *
import traceback
from util.log import *


def get_test_case_sheet(test_cases_excel_path):
    test_case_sheet_names = []
    excel_obj = Excel(test_cases_excel_path)
    excel_obj.set_sheet_by_index(1)
    test_case_rows = excel_obj.get_rows_object()[1:]
    for row in test_case_rows:
        if row[3].value == 'y':
            print(row[2].value)
            test_case_sheet_names.append((int(row[0].value)+1, row[2].value))
    return test_case_sheet_names


# print(get_test_case_sheet(ProjDirPath+"\\TestData\\testdata.xlsx"))
def execute(test_cases_excel_path, row_no,test_case_sheet_name):
    excel_obj = Excel(test_cases_excel_path)
    excel_obj.set_sheet_by_name(test_case_sheet_name)
    test_step_rows = excel_obj.get_rows_object()[1:]
    start_time = get_current_date()+" "+get_current_time()
    start_time_stamp = time.time()
    test_result_flag = True
    for test_step_row in test_step_rows:
        if test_step_row[6].value == "y":
            test_action = test_step_row[2].value
            locator_method = test_step_row[3].value
            locator_exp = test_step_row[4].value
            test_value = test_step_row[5].value
            # print(test_action,locator_method,locator_exp,test_value)
            if locator_method is None:
                if test_value is None:
                    command = test_action+"()"
                else:
                    command = test_action + "('%s')" % test_value
            else:
                if test_value is None:
                    command = test_action+"('%s','%s')" % (locator_method, locator_exp)
                else:
                    command = test_action + "('%s','%s','%s')" % (locator_method, locator_exp, test_value)
            print(command)
            try:
                info(command)
                eval(command)
                excel_obj.write_cell_value(int(test_step_row[0].value) + 1, test_step_result_col_no, "执行成功")
                excel_obj.write_cell_value(int(test_step_row[0].value) + 1, test_step_error_info_col_no, "")
                excel_obj.write_cell_value(int(test_step_row[0].value) + 1, test_step_capture_pic_path_col_no, "")
                info('执行成功')
            except Exception as e:
                test_result_flag = False
                traceback.print_exc()
                error(command + ":" + traceback.format_exc())
                # 20.main.py中将运行结果写入excel，失败的话错误信息也写入，将列号在var.py映射中，这样容易看懂
                excel_obj.write_cell_value(int(test_step_row[0].value) + 1, test_step_result_col_no, "失败", "red")
                excel_obj.write_cell_value(int(test_step_row[0].value) + 1, test_step_error_info_col_no,\
                    command+":"+traceback.format_exc())
                # 21.Util中新增dir_operation.py，生成日期目录
                # 22.main.py中增加创建日期目录，错误截屏信息，写入excel
                dir_path = make_current_date_dir(ProjDirPath + "\\" + "screen_capture\\")
                dir_path = make_current_hour_dir(dir_path + "\\")
                pic_path = os.path.join(dir_path,get_current_time()+".png")
                capture(pic_path)
                excel_obj.write_cell_value(int(test_step_row[0].value) + 1, test_step_capture_pic_path_col_no, pic_path)

    # 23.main.py中判断测试用例执行情况和计算运行时间，写入excel
    end_time = get_current_date() + " " + get_current_time()
    end_time_stamp = time.time()
    elapsed_time = int(end_time_stamp - start_time_stamp)
    elapsed_minutes = int(elapsed_time//60)
    elapsed_seconds = elapsed_time % 60
    elapsed_time = str(elapsed_minutes)+"分"+str(elapsed_seconds)+"秒"
    if test_result_flag:
        test_case_result = "测试用例执行成功"
    else:
        test_case_result = "测试用例执行失败"
    excel_obj.set_sheet_by_index(1)
    excel_obj.write_cell_value(int(row_no), test_case_start_time_col_no, start_time)
    excel_obj.write_cell_value(int(row_no), test_case_end_time_col_no, end_time)
    excel_obj.write_cell_value(int(row_no), test_case_elapsed_time_col_no, elapsed_time)
    if test_result_flag:
        excel_obj.write_cell_value(int(row_no), test_case_result_col_no, test_case_result)
    else:
        excel_obj.write_cell_value(int(row_no), test_case_result_col_no, test_case_result, "red")


# 25.清除测试用例执行结果
def clear_test_data_file_info(test_data_excel_file_path):
    excel_obj = Excel(test_data_excel_file_path)
    excel_obj.set_sheet_by_index(1)
    test_case_rows = excel_obj.get_rows_object()[1:]
    for test_step_row in test_case_rows:
        excel_obj.set_sheet_by_index(1)
        if test_step_row[test_case_is_executed_flag_row_no].value == "y":
            excel_obj.write_cell_value(
                int(test_step_row[test_case_id_col_no].value) + 1, test_case_start_time_col_no,"")
            excel_obj.write_cell_value(
                int(test_step_row[test_case_id_col_no].value) + 1, test_case_end_time_col_no, "")
            excel_obj.write_cell_value(
                int(test_step_row[test_case_id_col_no].value) + 1, test_case_elapsed_time_col_no, "")
            excel_obj.write_cell_value(
                int(test_step_row[test_case_id_col_no].value) + 1, test_case_result_col_no, "")

            excel_obj.set_sheet_by_name(test_step_row[test_case_sheet_name].value)
            test_step_rows = excel_obj.get_rows_object()[1:]
            for test_step_row in test_step_rows:
                if test_step_row[test_step_id_col_no].value is None:
                    continue
                excel_obj.write_cell_value(
                    int(test_step_row[test_step_id_col_no].value) + 1, test_step_result_col_no, "")
                excel_obj.write_cell_value(
                    int(test_step_row[test_step_id_col_no].value) + 1, test_step_error_info_col_no, "")
                excel_obj.write_cell_value(
                    int(test_step_row[test_step_id_col_no].value) + 1, test_step_capture_pic_path_col_no, "")

if __name__ == "__main__":
    # 24.遍历执行所有测试用例
    test_data_excel_file_path = ProjDirPath+"\\test_data\\testdata.xlsx"
    for test_case_sheet in get_test_case_sheet(test_data_excel_file_path):
        execute(test_data_excel_file_path, test_case_sheet[0], test_case_sheet[1])
    # clear_test_data_file_info(test_data_excel_file_path)
    from util.send_mail import *
    send_mail()