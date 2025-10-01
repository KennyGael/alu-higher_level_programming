# JavaScript - Web Scraping

> By: Guillaume, CTO at Holberton School  
> Duration: Oct 1, 2025 – Oct 7, 2025

## Description

This project is a practical demonstration of my understanding of JavaScript in the context of web scraping and file system operations. Through this project, I explored how to interact with APIs, parse JSON data, and handle files using Node.js.

I used the deprecated but still widely-used `request` module to make HTTP requests and scrape data from public APIs like the Star Wars API and JSONPlaceholder. I also worked with the built-in `fs` module in Node.js to read from and write to files.

---

## Learning Objectives

By completing this project, I gained the ability to:

- Explain why JavaScript is a powerful programming language
- Read and manipulate JSON data
- Use both the `request` and `fetch` APIs to make HTTP requests
- Read from and write to the file system using the Node.js `fs` module
- Understand and apply asynchronous programming using callbacks

---

## Requirements

### General

- Code is written in JavaScript and executed using Node.js v10.14.x on Ubuntu 14.04 LTS
- All scripts are executable and start with the shebang: `#!/usr/bin/node`
- Code follows the **semistandard** style guide (Standard + semicolons)
- Usage of `const` and `let` is enforced — `var` is not used
- Each file ends with a new line

---

## Setup Instructions

### Install Node.js v10

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semistandard
```bash
$ sudo npm install semistandard --global
```

### Install request module
```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

### Resources Used
- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON)
- [Node.js fs module documentation](https://nodejs.org/api/fs.html)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

### Note

Although the request module is deprecated, it remains an excellent tool for learning the fundamentals of HTTP requests in Node.js. This project helped me understand how web scraping works, and gave me a solid foundation for working with real-world APIs and file handling.