export default function guardrail(mathFunction) {
  const queue = [];

  try {
    // try to execute mathFunction and store the result
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // Catch any errors thrown by mathFunction and store the error message
    queue.push(`Error: ${error.message}`);
  }

  // Regardless of success or failure add message to queue
  queue.push('Guardrail was processed');

  return queue;
}
