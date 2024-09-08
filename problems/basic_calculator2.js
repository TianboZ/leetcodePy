/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
  const stack = [];
  const items = s.replace(" ", "").split(/([+\-*/])/);
  console.log(items);
  let sign = "+";

  for (let i = 0; i < items.length; i++) {
    const n = items[i];

    if (n === "+" || n === "/" || n === "-" || n === "*") {
      // opertand
      sign = n;
    } else {
      // number
      const num = Number(n);
      if (sign === "*") {
        stack.push(stack.pop() * n);
      } else if (sign === "/") {
        const isNeg = stack[stack.length - 1] * n < 0 ? -1 : 1;
        stack.push(Math.floor(Math.abs(stack.pop()) / n) * isNeg);
      } else if (sign === "-") {
        stack.push(-Number(n));
      } else {
        stack.push(Number(n));
      }
    }
  }
  // console.log(stack)
  let sum = 0;
  stack.forEach((n) => {
    sum += n;
  });
  // stack.forEach()
  return sum;
};
