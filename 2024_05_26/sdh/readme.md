# Topics

## Computer science fundamentals
- ### Logic : 프로그램이 실행되는 동안 결정을 내리는 것을 뜻합니다
- ### Repetition : 조건에 따라 여러 작업을 반복하는것을 뜻합니다
- ### Data : 데이터

## Rust code

***

# Teaching Style

## Continuous reinforcement
- ### Short lecture
- ### Coding demonstration
- ### Code exercise
    - #### Implement concepts presented
    - #### See alternative implementation

## Code quality

# Install

## rustup
- ### Manages Rust installation

## visual studio code
- ### coding environment

## MSVC C++ Build Tools
- ### Neede to build on windows

# Data Types

## Memory only stores binary data
- ### Anything can be represented in binary

## Program determines what the binary represents

## Basic types that are universally useful are provided by tthe language

# Basic Data Types

## Boolean
- ### true, false

## Integer
- ### 1, 2, 50, 99, -2

## Double / Float
- ### 1.1, 5.5, 200.0001, 2.0

## Character
- ### 'A', 'B', 'C', '6', '$'

## String
- ### "Hello", "string", "acer"

# Recap

## Anything can be represented withg binary

## Basic data types are:
- ### boolean, integer, double & float, character, string

# What is a variable?

## Assign data to a temporary memory location
- ### Allows programmer to easily work with memory

## Can be set to any value & type

## Immutable by default, but can be mutable
- ### Immutable: cannot be changed
- ### Mutable: can be changed 

```
let two = 2;
let hello = "hello";
let j = 'j';
let my_half = 0.5;
let mut my_name = 'Bill';
let quit_program = false;
let your_half = my_half;
```

# Recap

## Variables make it easier to work with data

## Variables can be assigned to any value
- ### This include other variables

## Immutable by default

# What are functions?

## A way to encapsulate program functionality

## Optionally aceept data

## Optionally return data

## Utilized for code organization
- ### Also makes code easier to read

# Anatomy of a function
```
fn add(a: i32, b: i32) -> i32 {
    # i32 : 32비트 정수
    a + b
}

let x = add(1, 1);
let y = add(3, 9);
let z = add(x, 1);
```

# The println macro

## "Prints" (displays) information to the terminal

## Useful for debugging
```
let life = 42;
println!("hello");
println!("{:?}", life);
println!("{:?} {:?}", life, life);

# 매크로와 함수 호출의 차이는 끝에 느낌표를 쓰는지 여부입니다.
# :? 디버그 모드
```

# Recap

## Macros use an exclamation point to call

## Generate additional Rust code