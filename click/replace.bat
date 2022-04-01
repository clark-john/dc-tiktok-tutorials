@echo off
cd examples
set /p file="Type a file: "
type %file% > ../main.py
cd ..