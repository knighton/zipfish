find data/git/ -type f -name '*.c' -o -name '*.h' | \
    sort | \
    xargs clang -fsyntax-only -Xclang -dump-tokens -Idata/git/ 2>&1 | \
    grep \\t | \
    cut -f1 -d$'\t' | \
    sort | \
    uniq -c | \
    sort -n | \
    sed 's/^ *//' > \
    data/git_token_freqs.txt

cat data/git_token_freqs.txt | \
    cut -f1 -d' ' | \
    uniq -c | \
    sed 's/^ *//' > \
    data/git_token_freq_freqs.txt
