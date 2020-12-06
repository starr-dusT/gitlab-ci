#!/bin/sh

# Arguments
VERSION=${1:-${VERSION}}

# Extract version changelog
sed -n "/^## \[${VERSION}\]/,/^## \[/{
  n;
  :a;
  n;
  h;
  /^$/{
    n;
    H;
    /^$/{
      n;
      H;
      /^<a name=/{
        q;
      };
    };
    g;
  };
  p;
  ba;
}" ./CHANGELOG.md
