package main

import "testing"

func TestOneBottle(t *testing.T) {
    got := PluralBottles(1)
    want := "bottle"
    if got != want {
        t.Fatalf("Expected %q, got %q", want, got)
    }
}

func TestPluralBottles(t *testing.T) {
    got := PluralBottles(2)
    want := "bottles"
    if got != want {
        t.Fatalf("Expected %q, got %q", want, got)
    }
}

func TestOneBottleVerse(t *testing.T) {
    got := Verse(1)
    want := "1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\n"
    if got != want {
        t.Fatalf("Expected %q, got %q", want, got)
    }
}

func TestTwoBottlesVerse(t *testing.T) {
    got := Verse(2)
    want := "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n\n"
    if got != want {
        t.Fatalf("Expected %q, got %q", want, got)
    }
}

func TestZeroBottlesVerse(t *testing.T) {
    got := Verse(0)
    want := "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
    if got != want {
        t.Fatalf("Expected %q, got %q", want, got)
    }
}
