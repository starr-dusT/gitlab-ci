#!/bin/bash

# Header
for i in $(seq 1 30); do
  echo ''
done

# Delay
sleep 3

# Previewer
function previewer()
{
  # Variables
  command=("${@}")

  # Prompt
  echo ''
  echo -en "\033[32m${USER}@preview \033[33mgitlabci-local\033[0m $ "
  sleep 1

  # Input
  if [ ! -z "${command[*]}" ]; then
    echo -n "${command[*]} "
    sleep 1
  fi

  # Execution
  if [ ! -z "${command[*]}" ]; then
    echo ''
    "${command[@]//\"/}"
  else
    sleep 1
    echo ''
  fi
}

# Help
previewer gitlabci-local -h

# Jobs selector
previewer cd ./examples/
previewer gitlabci-local

# Job selector
previewer gitlabci-local -c ./.gitlab-ci.yml -l

# Job runner
previewer gitlabci-local -b -a \"Job\ 1\ -\ 3\"

# Pipeline runner
previewer cd ../tests/failures/
previewer gitlabci-local -b -a -p

# Stages runner
previewer cd ../stages/
previewer gitlabci-local -p one two

# Delay
previewer ''
sleep 5
