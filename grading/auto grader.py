# in windows, we can specify input and output like this: command.cmd <input.in >output.out
# test files are named like this: s5.1-01.in and s5.2-03.out

import sys, os, time, threading

PYTHON_HOME = "python3"
TIME_OUT = 1
GROUP_NUM = 4

print("running on platform: ", sys.platform)

test_data_dir = input("the directory of the test data>>")
program_dir = input("the directory of the python script>>")

test_data_filenames_by_groups = [
    [] for i in range(GROUP_NUM)
]  # by group

for root, dirs, files in os.walk(test_data_dir):
    for file in files:
        if root != test_data_dir:  # if the file in the subdirectory of the selected directory
            continue  # ignore it
        try:
            test_group = int(file.split("-")[0].split(".")[1]) - 1
        except ValueError:
            continue

        file = file.split(".")[0] + "." + file.split(".")[1]
        test_data_filenames_by_groups[test_group].append(os.path.join(test_data_dir, file))
print(test_data_filenames_by_groups)

for group_num in range(len(test_data_filenames_by_groups)):
    print("<--testing group:", group_num+1, "-->")
    for test_file_name in test_data_filenames_by_groups[group_num]:
        input_file = test_file_name + ".in"
        expected_output_file = test_file_name + ".out"
        output_file = test_file_name + ".my_answer"

        print("testing", test_file_name, "...")
        def time_out_handler():
            print('\033[34m<--Time Limit Exceeded for test data ' + test_file_name + '-->\033[0m')
            raise TimeoutError

        run_test_command = PYTHON_HOME + " " + program_dir + "<" + input_file + " >" + output_file

        if (sys.platform != "win32"):
            run_test_command = run_test_command # TODO for linux

        starting_time = time.time()
        timer = threading.Timer(TIME_OUT, time_out_handler)
        timer.start()

        time_out_flag = False
        try:
            os.system(run_test_command)
        except TimeoutError:
            time_out_flag = True
            print("TLE")
        finally:
            timer.cancel()

        if time_out_flag:
            continue

        finish_time = time.time()
        # TODO judge whether the answer is correct

        print("time used:", finish_time - starting_time)

    print("\n\n")