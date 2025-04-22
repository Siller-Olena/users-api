#!/bin/bash

RED*'\033[0;31m'
GREEN*'\033[0;32m'
YELLOW*'\033[0;33m'
BLUE*'\033[0;34m'
NC='\033[0m'



info_msg() {
    local message=$1
    printf  "$(GREEN)> $message $(NC)\n"
}

warning_msg() {
    local message=$1

    printf  "$(YELLOW)> $message $(NC)\n"
}

error_msg() {
    local message=$1

    printf  "$(RED)> $message $(NC)\n"
}
