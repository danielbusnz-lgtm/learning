# React — Day 1 Notes

*Date: 2026-04-17*

Covered the absolute basics: components, JSX, props, state, and how events fire.

---

## 1. Components

A **component** is just a function that returns UI.

```jsx
function Greeting() {
  return <h1>Hello, world!</h1>;
}
```

Rules:
- Name must start with a **capital letter** (React uses this to tell components apart from HTML tags)
- Returns **JSX**
- Use as a tag: `<Greeting />` — React calls the function for you

## 2. JSX

JSX = **JavaScript + HTML-like syntax**. It's not real JS — a build tool converts it:

```jsx
const el = <h1>Hello</h1>;
// becomes: React.createElement('h1', null, 'Hello')
```

Inside JSX tags: HTML-like mode.
Inside `{ }` within JSX: back to JavaScript.

```jsx
<h1>Hello, {name}!</h1>
//     ↑    ↑    ↑
//    JSX   JS  JSX
```

Gotchas:
- Must return **one parent element** (use `<>...</>` fragment if you need multiple)
- `class` → `className`, `for` → `htmlFor`

## 3. Props

**Props = inputs to a component**, like function arguments. Passed as a single object.

```jsx
function Greeting({ name }) {       // destructured
  return <h1>Hello, {name}!</h1>;
}

<Greeting name="Dan" />             // pass a prop
```

- Strings use quotes: `name="Dan"`
- Numbers/variables use braces: `age={23}`
- Props are **read-only** — never modify them inside a component

## 4. State (useState)

**State = data the component owns and can change.**

```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}
```

### How it works
- `useState(0)` returns an array: `[currentValue, setterFunction]`
- Destructuring gives names: `count` (value), `setCount` (function)
- React stores the value in its internal memory (a "storage box")
- `count` is a **snapshot** of the box at render time
- `setCount(newValue)` = the **remote control** that updates the box

### When state changes
1. You call `setCount(1)`
2. React updates its internal box
3. React re-runs the component function
4. `useState(0)` now returns `[1, setCount]`
5. UI re-renders with new value

### Never mutate state directly
```js
count = 5;         // ✗ React doesn't know
setCount(5);       // ✓ tells React to re-render
```

---

## Key JavaScript concepts (that React relies on)

### Functions are values ("first-class")

Functions can be stored in variables, passed as arguments, returned from other functions — just like numbers or strings.

```js
const greet = () => console.log("hi");   // stored in variable
runTwice(greet);                          // passed as argument
```

### Arrow functions = anonymous functions

```js
() => setCount(count + 1)
//  ↑         ↑
// no params  body
```

Equivalent to:
```js
function() {
  setCount(count + 1);
}
```

Just a function without a name. Defining one **does not run it** — it just sits there until called.

### Destructuring

```js
const [a, b] = [10, 20];              // array destructuring
const { name } = { name: "Dan" };     // object destructuring
```

React uses this everywhere (props, useState).

---

## How onClick actually works

```jsx
<button onClick={() => setCount(count + 1)}>
```

- `onClick` is a **prop** (named slot) on the button
- Its value is an **arrow function** (not called yet — just defined)
- React internally does `button.addEventListener('click', yourFunction)`
- When the user clicks, the **browser** fires a click event
- The browser calls your function
- Your function calls `setCount(...)` → React re-renders

### Critical distinction

```jsx
onClick={handleClick}      // ✓ passes the function
onClick={handleClick()}    // ✗ CALLS it immediately during render
```

`()` at the end = "call it now." No `()` = "here's the function itself."

---

## Project structure

A React app has:
- **`index.html`** — one real HTML file with an empty `<div id="root">`
- **`main.jsx`** — JavaScript entry point that tells React to render into that div
- **`App.jsx`**, **`Counter.jsx`**, etc. — your components

```jsx
// main.jsx
import { createRoot } from 'react-dom/client';
import { App } from './App';

const root = createRoot(document.getElementById('root'));
root.render(<App />);
```

`.jsx` extension = "JavaScript with JSX inside." Not HTML.

---

## What's next

- [ ] `Toggle` exercise — boolean state, button flips it
- [ ] `useEffect` — running code in response to changes (side effects)
- [ ] `useRef` — refs & DOM access
- [ ] Lifting state up
- [ ] Custom hooks
