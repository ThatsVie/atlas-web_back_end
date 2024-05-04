export default function loadBalancer(chinaDownload, USDownload) {
  // Promise.race() takes an array of promises and returns a promise
  // resolves or rejects as soon as one of the promises in the array resolves or rejects
  // result or error of that first settled promise is returned
  return Promise.race([chinaDownload, USDownload]);
}
