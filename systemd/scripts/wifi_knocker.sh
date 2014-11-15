#!/bin/bash - 
#===============================================================================
#
#          FILE: wifi_knocker.sh
# 
#         USAGE: ./wifi_knocker.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 11/12/14 14:31
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

#lang="en" # Может быть так же "ru" это язык открываемой страницы в случае ошибки и проч, естественно работает только при авторизации через броузер
#screen="normal"
url="http%3A%2F%2Fya.ru%2F" # URL на который выполняется автоматический переход после авторизации
password="gfhjkm"
username="mosmetro"
button="4"
ef="0"
#x="101" # координаты клика по кнопке,
#y="29"  # возможно их стоит рандомизировать в пределах 1 - 100

curl -d "buttonClicked=$button&username=$username&password=$password&redirect_url=$url&err_flag=$ef" \
    -e http://1.1.1.1/login.html -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)" \
    -k --trace-ascii trace.txt http://1.1.1.1/login.html > /dev/null

