#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

cp rules/classical/apple.yaml apple.yaml
cp rules/classical/openai.yaml openai.yaml
cp rules/classical/instagram.yaml "instagram (2).list"

echo "Legacy compatibility files synchronized."
