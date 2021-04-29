if [ $(curl -LI http://localhost:8001 -o /dev/null -w '%{http_code}\n' -s) == "200" ]; then echo 0; fi
