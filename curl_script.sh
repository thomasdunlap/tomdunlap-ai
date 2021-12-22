if [ $(curl -LI http://localhost:5000 -o /dev/null -w '%{http_code}\n' -s) == "200" ]; then echo 0; fi
