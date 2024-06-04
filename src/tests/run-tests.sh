if [ "$(basename "$PWD")" = "src" ]; then
    :
elif [ "$(basename "$PWD")" = "tests" ]; then
    cd ..
else
    echo "Please run \"./run-tests\" from the src or tests directory"
    exit 1
fi

echo "Building..."
    antlr4-build 2>&1 > /dev/null

for file in tests/ValidTests/*.agl; do
    #in green if output has last line "Semantic check passed." or red otherwise
    if cat $file | antlr4-run 2>&1 | grep -q "Semantic check passed."; then
        echo -e "\e[32m $(basename "$file"): OK\e[0m"
    else
        echo -e "\e[31m $(basename "$file"): FAIL\e[0m"
    fi
done

cd .. 
echo "Cleaning up..."
antlr4-clean 2>&1 > /dev/null
