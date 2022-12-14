#!/bin/sh

set -enable

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.confnginx -g 'daemon off;'