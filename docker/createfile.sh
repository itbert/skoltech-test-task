if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Использование: $0 filename output_dir"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "Файл '$1' не найден"
    exit 1
fi

mkdir -p "$2"

cat "$1" \
    | tr -c '[:alnum:]' '\n' \
    | tr '[:upper:]' '[:lower:]' \
    | grep -E '.+' \
    | sort \
    | uniq -c \
    | sort -nr \
    | head -n 10 \
    | awk '{print $2}' \
    | nl -w1 -s'_' \
    | while read n word; do
        touch "$2/${word}_${n}"
      done
