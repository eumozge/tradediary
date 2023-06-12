#!/bin/bash

for arg in $@
  do
    case $arg in
      '--demon')
        DEMON=1
      ;;
      '--drop-db')
        DROP_DATABASE=1
      ;;
      '--down')
        DOWN=1
      ;;
    esac
  done

if [ $DROP_DATABASE == 1 ]
  then
    echo '' && echo 'Drop database volumes:'
    IS_POSTGRES_DROPPED=$(sudo docker volume rm $(sudo docker volume ls -q --filter name=diary-postgres))
    echo '- $IS_POSTGRES_DROPPED' && echo ''
  fi

if [ $DOWN == 1 ]
  then
    sudo docker compose -f dev.compose.yml down
  else
    if [ $DEMON == 1 ]
      then
        sudo docker compose -f dev.compose.yml up -d --remove-orphans --build
      else
        sudo docker compose -f dev.compose.yml up --remove-orphans --build
    fi
  fi
