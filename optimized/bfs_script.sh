#!/bin/bash
#run this script for DFS
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/aymanehassini/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/aymanehassini/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/aymanehassini/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/aymanehassini/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup

# <<< conda initialize <<<
conda activate main 

function ProgressBar {
# Process data
    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done
# Build progressbar string lengths
    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")

printf "\rProgress : [${_fill// /#}${_empty// /-}] ${_progress}%%"

}

# Variables
_start=0

# This accounts as the "totalState" variable for the ProgressBar function
_end=99

# Proof of concept
for number in $(seq ${_start} ${_end})
do
    
    ProgressBar ${number} ${_end}
    python main_bfs.py ${number}
done
printf '\nFinished!\n'
