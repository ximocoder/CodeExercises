// This is a comment, and will be ignored by the compiler
// You can test this code by clicking the "Run" button over there ->
// or if prefer to use your keyboard, you can use the "Ctrl + Enter" shortcut

// This code is editable, feel free to hack it!
// You can always return to the original code by clicking the "Reset" button ->
use std::io;
use std::io::prelude::*;

//https://www.rust-lang.org/en-US/install.html
//https://www.visualstudio.com/downloads/#build-tools-for-visual-studio-2017-rc

  fn pause() {
    let mut stdin = io::stdin();
    let mut stdout = io::stdout();

    // We want the cursor to stay at the end of the line, so we print without a newline and flush manually.
    write!(stdout, "Press any key to continue...").unwrap();
    stdout.flush().unwrap();

    // Read a single byte and discard
    let _ = stdin.read(&mut [0u8]).unwrap();
    }

// This is the main function
fn main() {
    // The statements here will be executed when the compiled binary is called

  
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;

    // Print text to the console
    println!("Hello World!");
    println!("test");
    if (true)
    {
      println!("testif");
    }
     // Special formatting can be specified after a `:`.
    println!("{} of {:b} people know binary, the other half don't", _unused_variable, 2);
    pause();
    
      
}