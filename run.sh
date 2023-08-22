sudo docker run \
    --rm \
    --network host \
    -e PORT=2732 \
    -v $(pwd)/app.py:/app/app.py \
    -v $(pwd)/token.txt:/app/token.txt \
    -t telegram_proxy
