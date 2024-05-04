export default function uploadPhoto(filename) {
  return new Promise((resolve, reject) => {
    reject(new Error(`${filename} cannot be processed`));
  });
}

// uploadPhoto takes  argument filename and returns a Promise.
// The Promise is constructed to always reject with an Error object.
// The Error object's message includes the filename and that the file cannot be processed.
