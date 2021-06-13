echo $PWD

docker system prune -f
docker build -f hanzi.Dockerfile -t hanzi_image .

docker run -it \
--name hanzi \
-v $PWD:/hanzi-handwriting \
-v $(cd ../makemeahanzi; PWD):/makemeahanzi \
-p 80:80 \
hanzi_image \
/bin/bash -c "cd hanzi-handwriting; ./helper.sh"