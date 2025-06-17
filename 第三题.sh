#!/bin/bash

file=$1
search_content=$2
output_file=$3

if [ ! -f "$file" ]; then
    echo "文件 $file 不存在"
    exit 1
fi

grep -n "$search_content" "$file" > "$output_file"
cat "$output_file"


echo "搜索结果已保存到 $output_file"

