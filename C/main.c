// 99 Bottles of Beer in C

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char strbuf[256];


char *verse(int count)
{
    char tmp[128];
    if (count == 0) {
        sprintf(strbuf, "%s%s\n",
                "No more bottles of beer on the wall. No more bottles of beer.\n",
                "Go to the store and buy some more. 99 bottles of beer on the wall.\n.");
    } else {
        sprintf(strbuf, "%d %s of beer on the wall, %d %s of beer.\n",
                count, count == 1 ? "bottle" : "bottles",
                count, count == 1 ? "bottle" : "bottles");
        strcat(strbuf, "Take 1 down and pass it around, ");
        if (count == 1) {
            sprintf(tmp, "%s", "no more");
        } else {
            sprintf(tmp, "%d", count - 1);
        }
        strcat(strbuf, tmp);
        sprintf(tmp, " %s of beer on the wall.\n\n",
                count == 2 ? "bottle" : "bottles");
        strcat(strbuf, tmp);
    }
    return strbuf;
}


int main (void)
{
    int count;
    for (count = 99; count >= 0; count--)
        printf("%s", verse(count));
    return 0;
}
