alias rr := render_remote

render_remote scene:
    cd .. && rsync -azP expos kali:~ --exclude=".git" --exclude="videos"
    ssh kali  "pwd && cd ~/expos && just lrf {{scene}} && exit"
    cd .. && rsync -azP kali:~/expos/media/videos/main/2160p60/{{scene}}.mp4 expos/videos
    just open {{scene}}

edit:
    open Notebook.wls -a "Mathematica"
    
open scene:
    qil "QuickTime Player"
    open videos/{{scene}}.mp4 -a "QuickTime Player"

lrvl scene:
    just render_local manim_very_low.cfg {{scene}}

lrl scene:
    just render_local manim_low.cfg {{scene}}

lrf scene:
    just render_local manim.cfg {{scene}}

render_local config scene:
    manim \
        --format mp4 \
        -c cfg/{{config}} \
        --disable_caching \
        -p \
        main.py {{scene}}
