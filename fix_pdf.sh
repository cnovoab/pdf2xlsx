BASE_DIR="/home/inzpiral/Documents/PDF2XLSX/docs"
CUR_DIR="$BASE_DIR/$1"
find "$CUR_DIR" -type f -name "*.pdf" -print0 | while IFS= read -r -d '' file; do
  filename=${file##*/}
  echo "file = $file"
  echo "filename: $filename"
  mkdir -p "$CUR_DIR/fixed"
  qpdf "$file" "$CUR_DIR/fixed/$filename" > /dev/null
  read line </dev/tty
done
