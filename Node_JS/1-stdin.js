// Welcomes the user and prompts for their name. 

console.log('Welcome to Holberton School, what is your name?');

// Listen for readable input from the user
process.stdin.on('readable', () => {
  const name = process.stdin.read();
  if (name !== null) {
    // Print the user's name
    process.stdout.write(`Your name is: ${name}`);
  }
});

// On the end of input (when piped input is used), print the closing message.
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
