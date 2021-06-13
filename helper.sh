python3 source/main.py
(cd worksheet; luatex --ini lualatex.ini; luatex --shell-escape --fmt=lualatex hanzi_worksheet.tex) &
(cd flashcard; luatex --ini lualatex.ini; luatex --shell-escape --fmt=lualatex hanzi_flashcard.tex) &
wait
mv worksheet/hanzi_worksheet.pdf .
mv flashcard/hanzi_flashcard.pdf .
rm -rf worksheet
rm -rf flashcard