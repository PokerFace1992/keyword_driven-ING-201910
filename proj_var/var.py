import os

firefoxDriverFilePath = "d:\\geckodriver"
chromeDriverFilePath = "d:\\chromedriver"
ieDriverFilePath = "d:\\IEDriverServer"
# 当前文件所在目录的父目录的绝对路径
ProjDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

test_step_id_col_no = 0
test_step_result_col_no = 8
test_step_error_info_col_no = 9
test_step_capture_pic_path_col_no = 10

test_case_id_col_no= 0
test_case_sheet_name=2
test_case_is_executed_flag_row_no= 3
test_case_start_time_col_no= 5
test_case_end_time_col_no= 6
test_case_elapsed_time_col_no= 7
test_case_result_col_no = 8


if __name__ == "__main__":
    print(ProjDirPath)