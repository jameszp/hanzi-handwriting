# hanzi-handwriting
Generate handwriting practice worksheets and flashcards for Simplified Chinese 汉子 .

1. Clone this repo.
2. Clone https://github.com/skishore/makemeahanzi into the same location so that the directories are at the same level.
3. Have `docker` installed and have the daemon up and running. If you do not have `docker`, download from https://www.docker.com/products/docker-desktop.
4. Enter characters into `input.txt`. As of now, any whitespace, linebreaks, and non-Chinese Unicode code points will be ignored.
5. Run the `run.sh` script: `./run.sh`.
6. The resulting pdf files should be titled `hanzi_worksheet.pdf` and `hanzi_flashcard.pdf`.

svgs-still from https://github.com/skishore/makemeahanzi