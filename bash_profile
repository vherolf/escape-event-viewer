if [[ -z "${DISPLAY}"  &&  "${XDG_VTNR}" -eq 1 ]]; then
  /home/pi/escape-event-viewer/grabber.py
  exec startx
fi
