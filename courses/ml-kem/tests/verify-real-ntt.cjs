'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const R = require('../real-ntt.js');
const q = 3329n;
const n = 256;
const canonical = x => Number(((BigInt(x) % q) + q) % q);
const vec = f => Array.from({length: n}, (_, i) => f(i));
const basis = (index, coefficient = 1) => vec(i => i === index ? coefficient : 0);
let assertions = 0;
function same(actual, expected, name) {
  assert.deepEqual(actual, expected, name);
  assertions++;
}

// Independent reference: first form the ordinary length-511 BigInt product,
// then apply X^256 = -1. Does not use any function from real-ntt.js.
function directProduct(a, b) {
  const expanded = new Array(511).fill(0n);
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) expanded[i + j] += BigInt(a[i]) * BigInt(b[j]);
  }
  for (let d = 510; d >= 256; d--) expanded[d - 256] -= expanded[d];
  return expanded.slice(0, n).map(canonical);
}

function powBig(base, exponent) {
  let result = 1n;
  for (let i = 0; i < exponent; i++) result = result * BigInt(base) % q;
  return result;
}

// Independent CRT evaluation: split even/odd coefficients and evaluate at
// gamma = 17^(2*BitRev7(block)+1). Checks orientation and block ordering.
function directCRT(a) {
  const answer = [];
  for (let block = 0; block < 128; block++) {
    const reversed = parseInt(block.toString(2).padStart(7, '0').split('').reverse().join(''), 2);
    const g = powBig(17, 2 * reversed + 1);
    let p = 1n;
    let even = 0n;
    let odd = 0n;
    for (let degree = 0; degree < 128; degree++) {
      even += BigInt(a[2 * degree]) * p;
      odd += BigInt(a[2 * degree + 1]) * p;
      p = p * g % q;
    }
    answer.push(canonical(even), canonical(odd));
  }
  return answer;
}

// Reproducible test data, not cryptographic randomness.
let seed = 0x2032024;
function next() {seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0; return seed;}
const vectors = [
  vec(() => 0), vec(() => 1), vec(() => -1),
  basis(0), basis(1), basis(255),
  vec(i => i), vec(i => i % 2 ? -3328 : 3328),
  vec(i => (i % 7) - 3),
  ...Array.from({length: 15}, () => vec(() => (next() % 19975) - 9987))
];

let roundTrips = 0;
let crtCases = 0;
let productCases = 0;
let logReplays = 0;

for (let index = 0; index < vectors.length; index++) {
  const a = vectors[index];
  const copy = a.slice();
  const trace = R.forward(a);
  same(a, copy, 'forward must not mutate its input');
  same(trace.input, a.map(canonical), 'input normalized');
  same(R.inverse(trace.output), a.map(canonical), 'round trip ' + index);
  roundTrips++;
  same(trace.output, directCRT(a), 'direct CRT ' + index);
  crtCases++;
  same(trace.stages.length, 7, 'seven stages');
  same(trace.logs.length, 896, '7*128 butterflies');
  const replay = trace.input.slice();
  for (let k = 0; k < trace.logs.length; k++) {
    const step = trace.logs[k];
    same([step.u, step.v], [replay[step.i], replay[step.j]], 'replay reads');
    same(step.j - step.i, step.len, 'butterfly spacing');
    same(step.stage, Math.floor(k / 128) + 1, 'stage numbering');
    replay[step.i] = step.left;
    replay[step.j] = step.right;
    if ((k + 1) % 128 === 0) same(replay, trace.stages[step.stage - 1], 'stage snapshot');
  }
  same(replay, trace.output, 'trace replay ends at output');
  logReplays++;
  const b = vectors[(index * 5 + 3) % vectors.length];
  const expected = directProduct(a, b);
  same(R.multiply(a, b), expected, 'NTT multiply against independent BigInt ' + index);
  same(R.schoolbook(a, b), expected, 'provided schoolbook against independent BigInt ' + index);
  productCases++;
}

for (let i = 0; i < n; i++) {
  const a = basis(i);
  same(R.inverse(R.forward(a).output), a, 'every basis inverse ' + i);
  roundTrips++;
}

// Explicit negative cyclic fold: X^255 * X = -1, not +1.
same(R.multiply(basis(255), basis(1)), basis(0, 3328), 'X^256 = -1');
same(R.multiply(basis(255), basis(255)), basis(254, 3328), 'X^510 = -X^254');
productCases += 2;

same(R.gamma(0), 17, 'first quadratic factor');
same(R.gamma(1), 3312, 'second quadratic factor');
same(R.baseMultiply([1, 2], [3, 4], 17), [139, 10], 'base product example');
same(R.baseMultiply([-1, 2], [3, -4], -17), [133, 10], 'signed base product');
same(R.forward(basis(0)).output, vec(i => i % 2 ? 0 : 1), 'constant maps to all constant residues');
same(R.forward(basis(1)).output, vec(i => i % 2 ? 1 : 0), 'X maps to all linear residues');
for (const call of [
  () => R.forward([1]),
  () => R.forward(vec(i => i === 5 ? NaN : 0)),
  () => R.inverse(vec(i => i === 0 ? 0.5 : 0)),
  () => R.gamma(128),
  () => R.baseMultiply([1, 2], [3, 4], NaN)
]) {assert.throws(call); assertions++;}

const summary = {
  status: 'passed',
  reference: 'FIPS 203 algorithms 9–12; independently checked with BigInt convolution and CRT remainders',
  parameters: {q: 3329, n: 256, zeta: 17, layers: 7, butterflies: 896, blocks: 128},
  roundTrips, directCRTCases: crtCases, productCases, replayedTraces: logReplays,
  assertions,
  boundaryExamples: {'X^255 * X': '-1', 'X^255 * X^255': '-X^254'},
  productionCertification: false
};
fs.writeFileSync(path.join(__dirname, 'real-ntt-verification.json'), JSON.stringify(summary, null, 2) + '\n');
console.log(JSON.stringify(summary, null, 2));
