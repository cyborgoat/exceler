#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/2/27 00:25
# @Author  : Cyborgoat
# @Desc    :
import xlsxwriter
import pathlib
from pathlib import Path


def gen_basic_template(file: pathlib.Path):
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()
    basic_headers = ['query', 'prompt', 'response', 'response_time', 'expected_response',
                     'num_characters',
                     'num_tokens',
                     'correct',
                     'error_type',
                     'notes',
                     ]

    for col in range(0, len(basic_headers)):
        worksheet.write(0, col, basic_headers[col])
    workbook.close()
