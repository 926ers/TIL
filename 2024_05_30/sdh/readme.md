## Create binary (application)
```
$ cargo new name
```

## Compile
```
$ cargo run --bin name
```

## without compile message
```
$ cargo run -q --bin name
```

# Match

## Add logic to program

## Similar to if..else

## Exhaustive
- ### All options must be accounted for

# Example with boolean
```
fn main() {
    let some_bool = true;
    match some_bool {
        true => println!("its true"),
        false => println!("its false"),
    }
}
```

```
fn main() {
    let some_int = 3;
    match some_int {
        1 => println!("its 1"),
        2 => println!("its 2"),
        3 => println!("its 3"),
        _ => println!("its anything else"),
    }
}
```

# match vs else..if

## match will be checked by the compiler
- ### if a new possibility is added, you will be notified when this occurs

## else..if is not checked by the compiler
- ### if a new possibility is added, your code may contain a bug

# Recap

## Prefer match over else..if when working with a single variable

## match considers all possibilities
- ### More robust code