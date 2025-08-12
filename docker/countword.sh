if [ -z "$1" ]; then
    echo "Использование: $0 filename"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Файл '$1' не найден"
    exit 1
fi

cat "$1" \
    | tr -c '[:alnum:]' '\n' \
    | tr '[:upper:]' '[:lower:]' \
    | grep -E '.+' \
    | sort \
    | uniq -c \
    | sort -nr
