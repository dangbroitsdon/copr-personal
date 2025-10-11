git config --global user.name "github-actions[bot]"
git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
git commit -am "update: $1"
git push

mkdir ~/.config

tee ~/.config/copr > /dev/null <<EOF
[copr-cli]
login = $COPR_LOGIN
username = vncvltvred
token = $COPR_TOKEN
copr_url = https://copr.fedorainfracloud.org
EOF

copr-cli buildscm --clone-url https://github.com/dangbroitsdon/copr-personal --subdir specfiles --spec $1.spec --nowait vncvltvred/personal