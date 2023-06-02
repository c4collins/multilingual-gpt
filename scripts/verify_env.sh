#!/bin/sh

echo "Testing .env"

check_variable() {
  if [ -z "$(grep "^$1=" .env)" ]; then
    echo "    $1 is missing or has an empty value in .env"
    echo "Process: FAILED"
    exit 1
  fi
}

check_variable "OPENAI_API_TOKEN"
check_variable "GITHUB_USERNAME"
check_variable "GITHUB_PAT"
check_variable "STABLE_DIFFUSION_WEBUI_URL"
check_variable "PINECONE_API_KEY"
check_variable "PINECONE_ENV"
check_variable "PINECONE_MEMORY_INDEX"

echo "All required variables are present and have non-empty values in .env"