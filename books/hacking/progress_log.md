# Hacking: The Art of Exploitation Progress Log

## Book: Hacking: The Art of Exploitation, 2nd Edition
## Author: Jon Erickson

---

## 2026-04-03: Chapter 0x250 - Getting Your Hands Dirty

**Status:** In Progress
**Confidence:** 3/5 (solid foundation building)

### Key Concepts Covered

**C Compilation Basics**
- `#include <stdio.h>` imports standard I/O library (function prototypes)
- GCC compiles C code to machine code
- Can create custom print functions using `write()` syscall

**Pointers**
- `*` = dereference (go to the address, get the value)
- `&` = address of (get the address of a variable)
- `p` = the address stored in pointer
- `*p` = the value at that address
- Pointers are needed for malloc because malloc returns an address

**Memory Layout**
- **text** = compiled code (read-only)
- **data** = initialized global variables
- **BSS** = uninitialized global variables (zeroed)
- **heap** = malloc'd memory, grows toward higher addresses
- **stack** = local variables, grows toward lower addresses

**Stack vs Heap**
- Stack: automatic allocation/deallocation, dies when function returns
- Heap: manual (malloc/free), persists until freed
- Stack overflow: too much stack usage (big arrays, infinite recursion)
- Memory leak: forgetting to free heap memory
- Heap fragmentation: gaps from random alloc/free patterns

**Registers**
- Tiny storage inside the CPU itself
- CPU can only do operations on registers
- Must load from RAM -> register -> operate -> store back to RAM
- x86: eax, ebx, ecx, edx, esp, ebp, eip
- ARM: x0, x1, x2... x30, sp

**Assembly Basics**
- Assembly = human-readable mnemonics for machine code
- `sub sp, sp, #0x20` = subtract 32 from stack pointer (make room)
- `ldr` = load register (RAM -> register)
- `str` = store register (register -> RAM)
- Each architecture has different assembly (x86 vs ARM)
- AT&T syntax vs Intel syntax (same instructions, different format)

**Hexadecimal**
- Base 16: 0-9 and A-F (A=10, B=11, C=12, D=13, E=14, F=15)
- Each position is power of 16 (1s, 16s, 256s, 4096s...)
- 0x10 = 16, 0x20 = 32, 0xFF = 255
- Used because it's compact representation of binary

**Architecture**
- x86 = Intel processors (8086, 80286... naming convention)
- ARM = Advanced RISC Machine (used in Mac M-series, phones)
- 32-bit = 4 billion addresses (4 GB max RAM)
- 64-bit = way more addresses (practically unlimited RAM)

**Tools Used**
- gcc (compiler)
- objdump (disassembler - shows assembly)
- gdb (debugger - inspect registers, memory)

### Practice Files Created
- `practice.c` - Hello World loop
- `myprint.c` - Custom print function using write()
- `pointer_practice.c` - Pointer exercises (Q1-Q5)

### Pointer Practice Answers
- Q1a: 5 (correct)
- Q1b: 5 (correct)
- Q2: 20 (pointer follows the value)
- Q3: 100 (*p = 100 changes x)
- Q4a: 10 (correct)
- Q4b: 30 (not the address, the value at the address)
- Q5: 10 (7 + 3 = 10)

### External Resources Used
- UIUC CS 225 Stack/Heap page: https://courses.grainger.illinois.edu/cs225/sp2022/resources/stack-heap/

### Next Up
- Continue 0x250 chapter
- GDB debugger section
- More assembly reading practice

---

## Completed Chapters
- 0x240 Fundamental Concepts (completed prior session)
- 0x250 Getting Your Hands Dirty (in progress)
