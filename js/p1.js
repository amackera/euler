/* If we list all the natural numbers below 10 that are multiples of 3 or 5,  */
/* we get 3, 5, 6 and 9. The sum of these multiples is 23. */
/* Find the sum of all the multiples of 3 or 5 below 1000. */

const _ = require('lodash');

function p1() {
  const numbers = _.range(1, 1000);

  const multiples = _.filter(numbers, (num) => {
    return num % 3 === 0 || num % 5 === 0;
  });

  const sum = _.reduce(multiples, (sum, num) => {
    return sum + num;
  }, 0);

  console.log(sum);
}

p1();
