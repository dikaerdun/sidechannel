// Browser-only classroom adapter. Pinned dependencies: @noble/post-quantum 0.7.1, @noble/hashes 2.4.0.
import {ml_kem512,ml_kem768,ml_kem1024} from '@noble/post-quantum/ml-kem.js';
import {sha3_256,sha3_512,shake256} from '@noble/hashes/sha3.js';
import {bytesToHex,hexToBytes,concatBytes} from '@noble/hashes/utils.js';
globalThis.MLKEM={
  algorithms:{512:ml_kem512,768:ml_kem768,1024:ml_kem1024},
  sha3_256,sha3_512,shake256,bytesToHex,hexToBytes,concatBytes,
  equal:(a,b)=>a.length===b.length&&a.every((v,i)=>v===b[i]),
  random:n=>{if(!globalThis.crypto?.getRandomValues)throw new Error('当前环境没有安全随机源，请选择公开的固定课堂种子。');return globalThis.crypto.getRandomValues(new Uint8Array(n));},
  version:'0.7.1',
};
