#!/bin/bash

# Функція перевірки наявності файла
check_file_exists() {
    local filename="$1"
    if [ ! -f "$filename" ]; then
        return 1  # файл не існує
    else
        return 0  # файл існує
    fi
}

# Функція читання імен з файла у масив
read_names_from_file() {
    local filename="$1"
    local -n names_array=$2  # використання іменованої передачі масиву (Bash 4+)
    names_array=()
    while IFS= read -r name; do
        names_array+=("$name")
    done < "$filename"
}

# Старт програми
filename="names.txt"  # Оскільки ми вже знаємо ім'я файлу, можна вказати його прямо тут

# Перевірка наявності файлу
if ! check_file_exists "$filename"; then
    echo "Помилка: файл '$filename' не знайдено!"
    exit 1
fi

# Читання імен з файлу
read_names_from_file "$filename" names

# Виведення імен з файлу
echo "Імена з файлу:"
for name in "${names[@]}"; do
    echo "- $name"
done

# Додавання нового імені
read -p "Введи нове ім'я для додавання: " new_name

# Перевірка на порожнє значення
if [ -z "$new_name" ]; then
    echo "Ім’я не може бути порожнім!"
    exit 1
fi

# Додавання імені в файл
echo "$new_name" >> "$filename"
echo "Ім'я '$new_name' додано до файлу '$filename'"

echo "Завершення скрипта."

