#!/bin/sh
xrandr --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output LVDS1 --off --output VIRTUAL1 --off --output DP1 --off --output VGA1 --off
#!/bin/sh
xrandr --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output LVDS1 --off --output VIRTUAL1 --off --output DP1 --off --output VGA1 --mode 1680x1050 --pos 1920x0 --rotate normal
nitrogen --restore
