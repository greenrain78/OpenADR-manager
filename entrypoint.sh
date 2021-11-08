# git pull
git fetch --all
git pull origin main

# check para
# shellcheck disable=SC2145
echo "실행 환경 변수 : $@"

# run main
python -u main.py $1