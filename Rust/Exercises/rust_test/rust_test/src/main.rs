use std::io;
use std::io::prelude::*;

fn pause() {
    let mut stdin = io::stdin();
    let mut stdout = io::stdout();

    // We want the cursor to stay at the end of the line, so we print without a newline and flush manually.
    write!(stdout, "Press any key to continue...").unwrap();
    stdout.flush().unwrap();

    // Read a single byte and discard
    let _ = stdin.read(&mut [0u8]).unwrap();
    }

fn main() {
	/*
	 * The let keyword introduces a local variable.
	 * Variables are immutable by default.
	 * To introduce a local variable that you can re-assign later, use let mut instead.
	 */
	let hi = "hi";
	let mut count = 0;

	while count < 10 {
		println!("{}, count: {}", hi, count);
		count += 1;
	}

	/*
	 * Although Rust can almost always infer the types of local variables,
	 * you can specify a variable's type by following it in the let with a colon, then the type name.
	 * Static items, on the other hand, always require a type annotation.
	 */
	static MONSTER_FACTOR: f64 = 57.8;
	let monster_size = MONSTER_FACTOR * 1000.0;
	println!("{}", monster_size);
	let monster_size = 50;
	println!("{}", monster_size);

	/*
	 * 3.4 Syntax extensions
	 * http://doc.rust-lang.org/tutorial.html#syntax-extensions
	 */
	// {} will print the "default format" of a type
	println!("{} is {}", "the answer", 43);

	// // {:?} will conveniently print any type
	println!("what is this thing: {:?}", monster_size);
    println!("what is this thing 2: {:?}", MONSTER_FACTOR);

    pause();
        // Integer addition
    println!("1 + 2 = {}", 1u32 + 2);

    // Integer subtraction
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Try changing `1i32` to `1u32` to see why the type is important

    // Short-circuiting boolean logic
    println!("true AND false is {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}", !true);

    // Bitwise operations
    println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 is {}", 1u32 << 5);
    println!("0x80 >> 2 is 0x{:x}", 0x80u32 >> 2);

    // Use underscores to improve readability!
    println!("One million is written as {}", 1_000_000u32);

        pause();
}