# JavaScript - Warm Up


## Introduction

This project marks the beginning of my journey with **JavaScript** as part of the ALX Higher-Level Programming curriculum.

JavaScript is a powerful, versatile language, and here I use it primarily for **scripting** purposes—similar to how I used Python previously. Later on, I’ll use JavaScript (along with jQuery) to make web applications dynamic, including the AirBnB clone project.

This warm-up focuses on the **basics**: printing output, handling arguments, using loops, writing functions, and understanding scopes.

## Learning Objectives

By the end of this project, I was able to:

- Explain why JavaScript is such a powerful and popular programming language
- Run JavaScript scripts using `Node.js`
- Work with variables and constants using `let` and `const`
- Understand the differences between `var`, `let`, and `const`
- Identify and use different JavaScript data types
- Use control flow statements like `if`, `else`, and loops (`for`, `while`)
- Write and invoke functions
- Use arrays and objects effectively
- Handle command-line arguments using `process.argv`
- Understand variable scope and function returns
- Import files/modules in JavaScript

## Setup & Requirements

To ensure consistent behavior, I used the following setup:

- JavaScript executed with **Node.js v14.x**
- Code follows **semistandard** style rules (Standard JS + semicolons)
- No use of `var`; I used `const` and `let` exclusively
- Every script starts with the shebang: `#!/usr/bin/node`
- Scripts are executable and end with a new line
- Editors used: `vim`, `emacs`

### Installing Node.js 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Installing semistandard

```bash
$ sudo npm install semistandard --global
```

### Task List

- Here are the scripts I wrote during this project:

| **#**  | **Filename**                     | **Description**                                               |
|--------|-----------------------------------|---------------------------------------------------------------|
| 0      | `0-javascript_is_amazing.js`      | Print a string using a `const` variable                        |
| 1      | `1-multi_languages.js`            | Print three lines using `console.log`                          |
| 2      | `2-arguments.js`                  | Print a message depending on the number of arguments           |
| 3      | `3-value_argument.js`             | Print the first argument or “No argument”                      |
| 4      | `4-concat.js`                     | Concatenate and print two arguments                            |
| 5      | `5-to_integer.js`                 | Convert and print an argument as an integer                    |
| 6      | `6-multi_languages_loop.js`       | Print lines from an array using a loop                         |
| 7      | `7-multi_c.js`                    | Print “C is fun” multiple times using a loop                   |
| 8      | `8-square.js`                     | Print a square using “X” characters                           |
| 9      | `9-add.js`                        | Print the sum of two integers using a function                 |
| 10     | `10-factorial.js`                 | Compute and print factorial recursively                        |
| 11     | `11-second_biggest.js`            | Print the second biggest number from args                      |
| 12     | `12-object.js`                    | Update an object property value                               |
| 13     | `13-add.js`                       | Export an addition function                                   |
| 14     | `100-let_me_const.js`             | Modify an externally declared variable (`myVar`)               |
| 15     | `101-call_me_moby.js`             | Call a function `x` times                                     |
| 16     | `102-add_me_maybe.js`             | Increment and call a callback function                        |
| 17     | `103-object_fct.js`               | Add a method to an object that increments its property        |


## Resources Used

To complete this project, I referred to the following:

- [JavaScript Guide - MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

Concepts on:

- Writing JavaScript

- Variables and Constants

- Data Types and Operators

- Functions and Loops

- Objects, Arrays, Scope

- var, let, const

- Module patterns

- ES6 basics


## How I Tested

- I made each script executable using:
```bash
chmod +x filename.js
./filename.js
```

- I verified code style using semistandard:
```bash
semistandard filename.js
```

- I checked line counts using:
```bash
wc -l filename.js
```# JavaScript - Warm up
