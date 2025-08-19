type TestFunction = () => void;

export function test(name: string, fn: TestFunction): void {
  try {
    fn();
    console.log(`✅ ${name}`);
  } catch (error) {
    console.error(`❌ ${name}`);
    console.error(error);
  }
}

export function assertEqual(actual: any, expected: any): void {
  if (actual !== expected) {
    throw new Error(\`Expected \${expected} but got \${actual}\`);
  }
}

// Example
test("adds numbers", () => {
  const result = 2 + 3;
  assertEqual(result, 5);
});
