# Enumeration

## Data that can be one of multiple different possibilities
- ### Each possibility is called a "variant"

## Provides information about your program to the compiler
- ### More robust programs

# Example
```
enum Direction {
    Up,
    Down,
    Left,
    Right
}
```

```
fn which_way(go: Direction) {
    match go {
        Direction::Up => "up",
        Direction::Down => "down",
        Direction::Left => "left",
        Direction::Right => "right",
    }
}
```

# Recap

## Enums can only be one variant at a time

## More robust programs when paired with match

## Make program code easier to read

# Structure

## A type that contains multiple pieces of data
- ### All or nothing - cannot have some pieces of data and not others

## Each piece of data is called a "field"

## Makes working with data easier
- ### Similar data can be grouped together

# Example
```
struct ShippingBox {
    depth: i32,
    width: i32,
    height: i32,
}
```

```
let my_box = ShippingBox {
    depth: 3,
    width: 2,
    height: 5,
};
```

```
let tall = my_box.height;

println!("the box is {:?} units tall", tall);
```

# Recap

## Structs deal with multiple pieces of data

## All fields must be present to create a struct

## Fields can be accessed using a dot (.)

# Tuples

## A type of "record"

## Store data anonymously
- ### No need to name fields

## Useful to return pairs of data from functions

## Can be "destructured" easily into variables

# Example
```
enum Access {
    Full,
}

fn one_two_three() -> (i32, i32, i32) {
    (1, 2, 3)
}

let numbers = one_two_three();
let (x, y, z) = one_two_three();
println!("{:?}, {:?}", x, numbers.0);
println!("{:?}, {:?}", y, numbers.1);
println!("{:?}, {:?}", z, numbers.2);

let (employee, access) = ("Jake", Access::Full);

```

# Recap

## Allow for anonymous data access

## Useful when destructuring

## Can contain any number of fields
- ### Use struct when more than 2 or 3 fields

# Expressions

## Rust is an expression-based language
- ### Most things are evaluted and return some value

## Expression values coalesce to a single point
- ### can be used for nesting logic

# Example
```
let my_num = 3;
let is_lt_5 = if my_num <5 {
    true
}
else {
    false
};

let is_lt_5 = my_num < 5;
```

# Example
```
let my_num = 3;
let message = match my_num {
    1 => "hello",
    _ => "goodbye"
}
```

# Example
```
enum Menu {
    Burger,
    Fries,
    Drink,
}

let paid = true;
let item = Menu::Drink;
let drink_type = "water";
let order_placed = match item {
    menu::Drink => {
        if drink_type == "water" {
            true
        }
        else {
            flase
        }
    }
    _ => true,
};
```

# Recap

## Expressions allow nested logic

## if and match expressions can be nested
- ### Best to not use more than two or three levels