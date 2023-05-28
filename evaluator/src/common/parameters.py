import argparse
import os
import sys
import re
from datetime import datetime as dt
from src.common.utilities import Application
from __meta__ import  __root_config__

messages = None

def is_valid_text(value: str):
    pattern: str = r'\s'
    if re.search(pattern, value):
        raise argparse.ArgumentTypeError(f"invalid value: '{value}', remove spaces.")
    return value

def exist_file(value: str):
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeErrorf("file not found : {value}")
    return value

def get_args():

    if Application.is_empty_folder(os.path.join(__root_config__, 'config', 'profiles')):
        raise Exception("You must configure the app before using it, please run:\npython evaluator/app.py --init\n")
    
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument('--profile-name', type=is_valid_text, default="default", required=False, help="user profile name")
    common_parser.add_argument('--format', choices=['csv', 'json', 'excel', 'parquet'], required=False, help="file format")
    
    # create the main parser
    parser = argparse.ArgumentParser(
        prog='\npython evaluator/app.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="© all rights reserved {}.".format( dt.now().year),
        add_help=False,
        usage='%(prog)s [options]',
        conflict_handler='resolve',
        description='''\
    Tool that allows automating and facilitating tasks related to:
    --------------------------------------------------------------

        - courses
        - bootcamps
        - performance tests
        - others
            '''
)
        

    subparsers = parser.add_subparsers(
        title="Homework evaluation",
        dest="command"
    )

    # create the parser for  init profile
    init_parser = subparsers.add_parser('init', parents=[common_parser], help="user application profiler")


    # create the parser for teachers
    teacher_parser = subparsers.add_parser('teachers', parents=[common_parser], help="tool to add info")
    # teachers sub-opt : list
    teacher_list_parser = teacher_parser.add_subparsers(title="list", dest="teachers_actios", metavar="")
    list_parser = teacher_list_parser.add_parser('list', help="list registered teachers")
    list_parser.add_argument('--active', choices=['Y', 'N'], required=True, help="teacher status")

    # teachers sub-opt : add
    add_parser = teacher_list_parser.add_parser('add', help="add new teacher")
    
    
   # teachers sub-opt : disable
    add_parser = teacher_list_parser.add_parser('disable', help="disable a teacher")
    add_parser.add_argument('--id', type=str, required=True, help="teacher identifier")


    # if no option set , show help 
    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit()
    return parser

