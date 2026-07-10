#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

cp rules/domain/apple.yaml apple.yaml
cp rules/classical/openai.yaml openai.yaml
cp snippets/instagram.list "instagram (2).list"

echo "Legacy compatibility files synchronized."
