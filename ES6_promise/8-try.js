/* eslint-disable */
export default function divideFunction(numerator, denominator) {
    if (denominator === 0) {
        throw new Error('cannot divisible by 0');
    } else {
        return numerator / denominator;
    }
}