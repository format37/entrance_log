sudo docker run \
    --network host \
    -e PORT=2732 \
    -v $(pwd)/app.py:/app/app.py \
    -v $(pwd)/token.txt:/app/token.txt \
    -d \
    -t \
    --restart on-failure \
    telegram_proxy
