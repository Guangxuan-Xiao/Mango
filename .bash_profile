function gacp() {
    # gacp: git add commit push in one command
    git add .
    git commit -a -m  "$*"
    git push
}
