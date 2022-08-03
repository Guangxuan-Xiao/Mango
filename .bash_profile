MANGOROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )"/ && pwd )"

echo "Mango Root: $MANGOROOT"

export PATH=$MANGOROOT/bin:$PATH

function gacp() {
    # gacp: git add commit push in one command
    git add .
    git commit -a -m  "$*"
    git push
}
