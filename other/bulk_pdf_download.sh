#!/bin/bash

# 📂 Folder to save PDFs
#SAVE_DIR="downloaded_papers"
#mkdir -p "$SAVE_DIR"

# 📜 Check input arguments
if [[ "$1" == "-f" && -n "$2" ]]; then
    PDF_LINKS_FILE="$2"
    if [ ! -f "$PDF_LINKS_FILE" ]; then
        echo "❌ Error: File '$PDF_LINKS_FILE' not found!"
        exit 1
    fi
    MODE="file"
elif [[ -n "$1" ]]; then
    SINGLE_DOI_OR_URL="$1"
    MODE="single"
else
    echo "❌ Usage: $0 [-f pdf_link.txt] OR $0 <DOI/URL>"
    exit 1
fi

# 🛠 Function to resolve DOI to a URL
resolve_doi() {
    DOI="$1"
    URL=$(curl -s -L -w "%{url_effective}" -o /dev/null "https://doi.org/${DOI}")
    echo "$URL"
}

# 🎯 Function to download PDF
download_pdf() {
    DOI_OR_URL="$1"

    # Extract a safe filename (replace '/' with '_')
    SAFE_NAME=$(echo "$DOI_OR_URL" | tr '/' '_')

    # Define the output file
#    OUTPUT_FILE="${SAVE_DIR}/${SAFE_NAME}.pdf"
    OUTPUT_FILE="${SAFE_NAME}.pdf"

    echo "⬇️ Downloading: $DOI_OR_URL → $OUTPUT_FILE"

    # Try downloading with wget, fallback to curl
    wget --quiet --show-progress --output-document="$OUTPUT_FILE" "$DOI_OR_URL" || \
    curl -sL -o "$OUTPUT_FILE" "$DOI_OR_URL"

    if [ -s "$OUTPUT_FILE" ]; then
        echo "✅ Downloaded: $OUTPUT_FILE"
    else
        echo "❌ Failed: $DOI_OR_URL"
        rm -f "$OUTPUT_FILE"
    fi
}

# 🔄 Process a single DOI/URL
if [[ "$MODE" == "single" ]]; then
    if [[ "$SINGLE_DOI_OR_URL" == 10.* ]]; then
        URL=$(resolve_doi "$SINGLE_DOI_OR_URL")
        if [[ "$URL" == *".pdf" ]]; then
            download_pdf "$URL"
        else
            echo "⚠️ DOI resolved, but no direct PDF: $URL"
        fi
    else
        download_pdf "$SINGLE_DOI_OR_URL"
    fi
    exit 0
fi

# 🔄 Process multiple DOIs/URLs from file
while IFS= read -r LINE || [[ -n "$LINE" ]]; do
    [[ -z "$LINE" ]] && continue  # Skip empty lines
    DOI_OR_URL=$(echo "$LINE" | xargs)

    if [[ "$DOI_OR_URL" == 10.* ]]; then
        URL=$(resolve_doi "$DOI_OR_URL")
        if [[ "$URL" == *".pdf" ]]; then
            download_pdf "$URL"
        else
            echo "⚠️ DOI resolved, but no direct PDF: $URL"
        fi
    else
        download_pdf "$DOI_OR_URL"
    fi

    sleep 2  # ⏳ Avoid rate limits
done < "$PDF_LINKS_FILE"

echo "🎉 Done! All PDFs processed."

