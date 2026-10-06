#!/bin/zsh
# keynote_render.sh DECK.pptx OUTDIR — open a uniquely named copy in Keynote, export exactly that
# document's slides as PNG, close it without saving. Other open documents are left alone.
deck=$1; out=$2
tag="render_$(date +%s)"
copy="$(dirname $deck)/$tag.pptx"
cp "$deck" "$copy"
rm -rf "$out"; mkdir -p "$out"
osascript <<OSA
with timeout of 900 seconds
tell application "Keynote"
  open POSIX file "$copy"
  set d to missing value
  repeat 120 times
    repeat with x in documents
      if name of x is "$tag" then set d to contents of x
    end repeat
    if d is not missing value then exit repeat
    delay 1
  end repeat
  export d to POSIX file "$out" as slide images with properties {image format:PNG, skipped slides:false}
  close d saving no
end tell
end timeout
OSA
rm -f "$copy"
ls "$out" | wc -l
