'use strict';
const assert=require('node:assert/strict');
const path=require('node:path');
const M=require('../math.js');
const E=require('../extra.js').math;
let count=0;
function eq(a,b){assert.deepEqual(a,b);count++;}
eq(E.fourProduct([1,2,0,0],[3,1,0,0]),{A:[3,9,16,10],B:[4,7,2,16],P:[12,12,15,7],raw:[12,11,8,0],c:[3,7,2,0],direct:[3,7,2,0]});
for(let k=0;k<24;k++){
 const a=Array.from({length:4},(_,i)=>(k*7+i*5)%33-16),b=Array.from({length:4},(_,i)=>(k*3+i*9)%33-16),d=E.fourProduct(a,b);
 eq(d.c,d.direct);eq(E.inverse(E.dft(a)),a.map(x=>E.mod(x)));
}
eq(E.cyclic([0,0,0,1],[0,0,1,0]),[0,1,0,0]);
eq(M.polyMul([0,0,0,1],[0,0,1,0]),[0,16,0,0]);
for(const mode of ['none','mild','strong','cancel'])for(let m=0;m<16;m++){
 const bits=Array.from({length:4},(_,i)=>(m>>i)&1),d=M.moduleExample(mode,bits);
 eq(d.w,d.mu.map((x,i)=>M.mod(x+d.totalNoise[i])));
}
eq([E.hw(9),E.hw(0^9),E.hw(8^9),E.hw(9^9)],[2,2,1,0]);
eq(E.hw(65536-3320),7);
console.log(JSON.stringify({suite:'course arithmetic',assertions:count,status:'passed'},null,2));
