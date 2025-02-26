#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/2/27 00:27
# @Author  : Cyborgoat
# @Desc    :
from exceler import llm_auditor
import pathlib

if __name__ == '__main__':
    fp = pathlib.Path(__file__).resolve().parent.joinpath('data', 'template_table.xlsx')
    fp.parent.mkdir(parents=True, exist_ok=True)
    llm_auditor.gen_basic_template(fp)
