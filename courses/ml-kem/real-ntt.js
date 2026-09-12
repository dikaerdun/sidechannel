/*
 * ML-KEM NTT teaching model — FIPS 203, algorithms 9–12.
 * q = 3329, n = 256, zeta = 17. Ordinary residues, no Montgomery encoding.
 * Exact integer arithmetic: all intermediate products are below 2^53.
 * This is an inspectable teaching model, not a constant-time cryptographic library.
 * Standard: https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf
 */
(function (root) {
  'use strict';
  const Q = 3329;
  const N = 256;
  const ROOT = 17;

  function mod(value) {
    return ((value % Q) + Q) % Q;
  }

  function normalize(input, size = N, name = 'input') {
    if (!input || typeof input.length !== 'number' || input.length !== size) {
      throw new RangeError(name + ' must have exactly ' + size + ' coefficients');
    }
    return Array.from(input, (value, index) => {
      if (!Number.isSafeInteger(value)) {
        throw new TypeError(name + '[' + index + '] must be a safe integer');
      }
      return mod(value);
    });
  }

  function power(base, exponent) {
    let result = 1;
    let factor = mod(base);
    while (exponent > 0) {
      if (exponent % 2 === 1) result = mod(result * factor);
      factor = mod(factor * factor);
      exponent = Math.floor(exponent / 2);
    }
    return result;
  }

  function bitRev7(value) {
    if (!Number.isInteger(value) || value < 0 || value > 127) {
      throw new RangeError('bitRev7 input must be an integer in 0..127');
    }
    let result = 0;
    for (let bit = 0; bit < 7; bit++) {
      result = 2 * result + (value & 1);
      value >>>= 1;
    }
    return result;
  }

  const ZETAS = Object.freeze(Array.from({length: 128}, (_, i) => power(ROOT, bitRev7(i))));

  // Algorithm 9. stage is 1-based; i/j identify the two coefficient slots.
  // twiddleIndex preserves the index called i in FIPS 203 algorithm 9.
  function forward(input) {
    const normalized = normalize(input);
    const output = normalized.slice();
    const stages = [];
    const logs = [];
    let twiddleIndex = 1;
    let stage = 0;
    for (let len = 128; len >= 2; len /= 2) {
      stage++;
      for (let start = 0; start < N; start += 2 * len) {
        const index = twiddleIndex++;
        const zeta = ZETAS[index];
        for (let i = start; i < start + len; i++) {
          const j = i + len;
          const u = output[i];
          const v = output[j];
          const t = mod(zeta * v);
          const left = mod(u + t);
          const right = mod(u - t);
          output[i] = left;
          output[j] = right;
          logs.push({stage, len, i, j, zeta, u, v, t, left, right,
                     twiddleIndex: index, start});
        }
      }
      stages.push(output.slice());
    }
    return {input: normalized, output, stages, logs};
  }

  // Algorithm 10: inverse butterflies use the reversed forward twiddle table.
  // Their right branch is zeta * (right - left), followed by scale 128^-1.
  function inverse(input) {
    const output = normalize(input);
    let twiddleIndex = 127;
    for (let len = 2; len <= 128; len *= 2) {
      for (let start = 0; start < N; start += 2 * len) {
        const zeta = ZETAS[twiddleIndex--];
        for (let i = start; i < start + len; i++) {
          const j = i + len;
          const u = output[i];
          const v = output[j];
          output[i] = mod(u + v);
          output[j] = mod(zeta * mod(v - u));
        }
      }
    }
    return output.map(value => mod(value * 3303));
  }

  // Quadratic factor for NTT block b: X^2 - gamma(b).
  function gamma(block) {
    return power(ROOT, 2 * bitRev7(block) + 1);
  }

  // Algorithm 12, with X^2 = gamma. Output order: [constant, X coefficient].
  function baseMultiply(aPair, bPair, gammaValue) {
    const a = normalize(aPair, 2, 'aPair');
    const b = normalize(bPair, 2, 'bPair');
    if (!Number.isSafeInteger(gammaValue)) throw new TypeError('gamma must be a safe integer');
    const g = mod(gammaValue);
    return [mod(a[0] * b[0] + mod(a[1] * b[1]) * g),
            mod(a[0] * b[1] + a[1] * b[0])];
  }

  // Algorithm 11, accepting two already transformed arrays.
  function multiplyNTTs(aInput, bInput) {
    const a = normalize(aInput, N, 'a');
    const b = normalize(bInput, N, 'b');
    const output = new Array(N);
    for (let block = 0; block < 128; block++) {
      const i = 2 * block;
      const pair = baseMultiply([a[i], a[i + 1]], [b[i], b[i + 1]], gamma(block));
      output[i] = pair[0];
      output[i + 1] = pair[1];
    }
    return output;
  }

  // Full multiplication in Z_3329[X]/(X^256 + 1).
  function multiply(a, b) {
    return inverse(multiplyNTTs(forward(a).output, forward(b).output));
  }

  // Direct reference multiplication: high-degree coefficients fold with a minus.
  function schoolbook(aInput, bInput) {
    const a = normalize(aInput, N, 'a');
    const b = normalize(bInput, N, 'b');
    const output = new Array(N).fill(0);
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        const degree = i + j;
        const index = degree < N ? degree : degree - N;
        output[index] = mod(output[index] + (degree < N ? 1 : -1) * a[i] * b[j]);
      }
    }
    return output;
  }

  const api = Object.freeze({Q, N, ROOT, mod, bitRev7, forward, inverse, gamma,
                             baseMultiply, multiplyNTTs, multiply, schoolbook});
  root.RealNTT = api;
  if (typeof module === 'object' && module.exports) module.exports = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
