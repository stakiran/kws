@echo off
setlocal
set targetname=task_management

python ..\regular\intoc\intoc.py -i %cd%\%targetname%.md --use-plain-enum | sort | clip
