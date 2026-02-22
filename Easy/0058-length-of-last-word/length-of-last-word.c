#include <string.h>

int lengthOfLastWord(char* s) {
    int n = strlen(s);
    int i = n - 1;
    int length = 0;

    // skip trailing spaces
    while (i >= 0 && s[i] == ' ')
        i--;

    // count last word letters
    while (i >= 0 && s[i] != ' ') {
        length++;
        i--;
    }

    return length;
}