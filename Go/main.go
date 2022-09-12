package main

import (
    "fmt"
    "strings"
)

func PluralBottles(count int) string {
    var wordForm string
    if count == 1 {
        wordForm = "bottle"
    } else {
        wordForm = "bottles"
    }
    return wordForm
}

func Verse(count int) string {
    var str strings.Builder
    if count == 0 {
        str.WriteString("No more bottles of beer on the wall, no more bottles of beer.\n")
        str.WriteString("Go to the store and buy some more, 99 bottles of beer on the wall.")
        return str.String()
    }
    msg := fmt.Sprintf("%d %s of beer on the wall, %d %s of beer.\nTake one down and pass it around, ",
                       count, PluralBottles(count), count, PluralBottles(count))
    str.WriteString(msg)
    if count == 1 {
        str.WriteString("no more bottles of beer on the wall.\n\n")
    } else {
        msg := fmt.Sprintf("%d %s of beer on the wall.\n\n", count -1, PluralBottles(count - 1))
        str.WriteString(msg)
    }
    return str.String()
}

func main() {
    var str strings.Builder
    for count := 99; count >= 0; count-- {
        str.WriteString(Verse(count))
    }
    fmt.Println(str.String())
}
