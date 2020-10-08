"""
Code Coverage script 1.0  (By Hamster)

What this script does:
    
    Discovers all unittests (following the format _TEST.py) from the given input directory.
    Then runs the tests and calculates code coverage using the "coverage" python module.
    It then saves the results (in html format) in the specified output folder.
    
To use: 
    Before Starting: Download and install 'coverage' (e.g. pip install coverage)
    
    Open up cmd/powershell (script only tested on windows) and enter:
        python <path_to_this_file>/CodeCoverageScript.py "<path_of_directory_to_test>" "<path_of_results>"
        
    Yo Mr future Hamster! copy and paste this:
        PS D:\Code\Repo\Scripts\CardBoard> python .\CodeCoverageScript.py "D:\Code\Repo\Scripts\CardBoard\mechazorg\mechazorg" "D:\Code\Repo\Scripts\CardBoard"
"""


import subprocess
import sys
import datetime
import os
import shutil

def run_code_coverage(in_d, out_d):
    
    datetime_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    result_folder_name = f"code_coverage_{datetime_now}"
    result_path = os.path.join(out_d, result_folder_name)
    
    if os.path.exists(result_path):
        shutil.rmtree(result_path)
    else:
        os.mkdir(result_path)
       
    old_dir = os.getcwd()
    os.chdir(in_d)
    
    print("Discovering unit tests and calculating code coverage...\n")
    run_coverage = subprocess.Popen('coverage run -m --branch unittest discover -p "*_TEST.py"')
    run_coverage.wait()
    gen_report = subprocess.Popen(f'coverage html -d {result_path}')
    gen_report.wait()
    print(f"\nCoverage report saved to {result_path}\n")
    os.chdir(old_dir)

if __name__ == "__main__":

    print("\n#### CODE COVERAGE 1.0 ####")
    print("###########################\n")
        
    try:
        to_test_dir = sys.argv[1]
        output_dir = sys.argv[2]
    except:
        print("failed to parse arguements")
    
    try:
        run_code_coverage(to_test_dir, output_dir)
    except Exception as e:
        print (e)
        sys.exit(1)
            
    sys.exit(0)
