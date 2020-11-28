#!/bin/sh

# Arguments
JOB=${1:-${JOB}}

# Job selection
if [ -z "${JOB}" ]; then
  echo ''
  printf " \033[1;33m> Run job \033[1;36m[JOB] \033[1;33m: \033[0m"
  read -r JOB
fi

# Header
echo ''
printf " \033[1;32m===[ \033[1;33mrun: ${JOB:?} \033[1;36m(local, native) \033[1;32m]===\033[0m\n"
echo ''

# Execute job scripts
sed -n "/^'${JOB}.*':$/,/^$/{ /^  script:$/{ :a; n; /    - /{ s/^ *- //p; ba; } } }" ./.gitlab-ci.yml |
  while read -r line; do
    if [ "${OSTYPE}" = 'msys' ]; then
      line=${line//sudo /}
      line=${line//python3 /python }
    fi
    echo "+ ${line}"
    sh -c "${line}"
  done

# Footer
echo ''
printf " \033[1;33m> Result: \033[1;32mSuccess\033[0m\n"
echo ''
