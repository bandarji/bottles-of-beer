fn bottle_plurality(count: u8) -> String {
    if count == 1 {
        return "bottle".to_string();
    } else {
        return "bottles".to_string();
    }
}

#[test]
fn test_bottle_plurality() {
    assert!(bottle_plurality(1) == "bottle".to_string());
    assert!(bottle_plurality(2) == "bottles".to_string());
}

fn verse(count: u8) -> String {
    if count == 0 {
        return "No more bottles of beer on the wall. No more bottles of beer.\n\
                Go to the store and buy some more. 99 bottles of beer on the wall!".to_string();
    } else if count == 1 {
        return "1 bottle of beer on the wall, 1 bottle of beer.\n\
                Take one down and pass it around. \
                No more bottles of beer on the wall.\n".to_string();
    } else {
        let mut base: String = format!("{} {} of beer on the wall. {} {} of beer.\n",
                                    count, bottle_plurality(count), count,
                                    bottle_plurality(count)).to_owned();
        let add: &str = &*format!("Take 1 down and pass it around. {} {} of beer on the wall.\n",
                                  count - 1, bottle_plurality(count - 1));
        base.push_str(add);
        return base;
    }
}

#[test]
fn test_verse() {
    assert!(verse(0) == "No more bottles of beer on the wall. No more bottles of beer.\n\
                         Go to the store and buy some more. \
                         99 bottles of beer on the wall!");
    assert!(verse(1) == "1 bottle of beer on the wall, 1 bottle of beer.\n\
                         Take one down and pass it around. \
                         No more bottles of beer on the wall.\n");
    assert!(verse(2) == "2 bottles of beer on the wall. 2 bottles of beer.\n\
                         Take 1 down and pass it around. 1 bottle of beer on the wall.\n");
}

fn main() {
    let mut count: u8 = 99;
    loop {
        println!("{}", verse(count));
        if count == 0 {
            break;
        }
        count -= 1;
    }
}
