#!/usr/bin/env bash
# Read the descriptor selected for a Paper/Bukkit jar without extracting files.
set -euo pipefail
for descriptor in paper-plugin.yml plugin.yml; do
    if yaml="$(unzip -p "$1" "$descriptor" 2>/dev/null)"; then
        printf '%s\n' "$yaml"
        exit 0
    fi
done
echo '::error::El jar requiere paper-plugin.yml o plugin.yml' >&2
exit 1
