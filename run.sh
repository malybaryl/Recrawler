 sudo docker run -it \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix:Z \
    --device /dev/dri \
    reclawler