(function(root){
'use strict';
const mod=(x,q=17)=>((x%q)+q)%q;
const center=(x,q=17)=>{const r=mod(x,q);return r>q/2?r-q:r};
const compress=(x,d,q=3329)=>mod(Math.floor(mod(x,q)*2**d/q+.5),2**d);
const decompress=(x,d,q=3329)=>Math.floor(q*x/2**d+.5);
const decode=(w,q=17)=>compress(w,1,q);
const encode=(m,q=17)=>decompress(m,1,q);
const pow=(a,n,q=17)=>{let r=1;for(a=mod(a,q);n>0;n=Math.floor(n/2),a=mod(a*a,q))if(n%2)r=mod(r*a,q);return r};
function scalar(p){const q=17,mu=encode(p.m,q),t=mod(p.a*p.s+p.e,q),u=mod(p.a*p.r+p.e1,q),v=mod(t*p.r+p.e2+mu,q),su=mod(p.s*u,q),w=mod(v-p.s*u,q),noise=p.e*p.r+p.e2-p.s*p.e1;return {...p,q,mu,t,u,v,su,w,noise,decoded:decode(w,q),success:decode(w,q)===p.m};}
function polyMulRaw(a,b){const n=a.length,out=Array(n).fill(0);for(let i=0;i<n;i++)for(let j=0;j<n;j++)out[(i+j)%n]+=(i+j<n?1:-1)*a[i]*b[j];return out;}
const polyMul=(a,b,q=17)=>polyMulRaw(a,b).map(x=>mod(x,q));
const add=(a,b)=>a.map((v,i)=>v+b[i]);
const sub=(a,b)=>a.map((v,i)=>v-b[i]);
const dot=(a,b)=>a.map((x,i)=>polyMulRaw(x,b[i])).reduce(add,Array(a[0].length).fill(0));
function polyTrace(a,b,q=17){let acc=Array(a.length).fill(0);const rows=[];for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++){let degree=i+j,index=degree%a.length,sign=degree<a.length?1:-1,value=sign*a[i]*b[j];acc[index]+=value;rows.push({i,j,degree,index,sign,value,product:a[i]*b[j],acc:[...acc],residue:acc.map(v=>mod(v,q))});}return rows;}
const moduleData={A:[[[3,1,4,1],[5,9,2,6]],[[5,3,5,8],[9,7,9,3]]],s:[[1,0,-1,0],[0,1,0,-1]],e:[[1,0,0,0],[0,1,0,0]],r:[[1,0,0,1],[0,1,0,0]],e1:[[0,1,0,0],[0,0,0,1]],e2:[0,1,0,0],m:[1,0,1,1]};
function moduleExample(mode='none',m=moduleData.m){
 const {A,s,e,r,e1,e2}=moduleData,q=17,n=4,k=2,mu=m.map(x=>encode(x,q));
 const as=A.map(row=>dot(row,s)),at=[0,1].map(i=>dot(A.map(row=>row[i]),r));
 const t=as.map((v,i)=>add(v,e[i]).map(x=>mod(x,q))),u=at.map((v,i)=>add(v,e1[i]).map(x=>mod(x,q)));
 const tr=dot(t,r),v=add(add(tr,e2),mu).map(x=>mod(x,q));
 const er=dot(e,r),se1=dot(s,e1),noise=sub(add(er,e2),se1);
 const du=mode==='none'?null:mode==='mild'?4:3,dv=mode==='none'?null:mode==='cancel'?2:3;
 const uc=du?u.map(a=>a.map(x=>compress(x,du,q))):null,vc=dv?v.map(x=>compress(x,dv,q)):null;
 const ur=du?uc.map(a=>a.map(x=>decompress(x,du,q))):u,vr=dv?vc.map(x=>decompress(x,dv,q)):v;
 const su=dot(s,ur),w=sub(vr,su).map(x=>mod(x,q)),decoded=w.map(x=>decode(x,q));
 const deltaU=ur.map((a,i)=>a.map((x,j)=>center(x-u[i][j],q))),deltaV=vr.map((x,i)=>center(x-v[i],q)),compressionNoise=sub(deltaV,dot(s,deltaU)),totalNoise=add(noise,compressionNoise);
 return{A,s,e,r,e1,e2,m:[...m],mu,q,n,k,as,at,t,u,v,tr,su,w,er,se1,noise,du,dv,uc,vc,ur,vr,deltaU,deltaV,compressionNoise,totalNoise,decoded,success:decoded.every((x,i)=>x===m[i])};
}
function bitReverse(i,bits){let out=0;for(let j=0;j<bits;j++){out=out*2+(i&1);i>>=1;}return out;}
function nttTrace(input,omega=2,q=17){
 const n=input.length,bits=Math.log2(n),permutation=input.map((_,i)=>bitReverse(i,bits)),start=permutation.map(i=>mod(input[i],q));let a=[...start];const logs=[],stages=[start];
 for(let len=2,stage=0;len<=n;len*=2,stage++){
  const rootPower=pow(omega,n/len,q);
  for(let base=0;base<n;base+=len){let zeta=1;for(let j=0;j<len/2;j++){
   const i=base+j,k=i+len/2,u=a[i],v=a[k],weighted=mod(v*zeta,q),left=mod(u+weighted,q),right=mod(u-weighted,q);
   a[i]=left;a[k]=right;logs.push({stage,len,i,j:k,u,v,zeta,weighted,left,right,values:[...a]});zeta=mod(zeta*rootPower,q);
  }}stages.push([...a]);
 }return {input:[...input],omega,q,permutation,start,logs,stages,output:[...a]};
}
const inverseNTT=(a,omega=2,q=17)=>nttTrace(a,pow(omega,q-2,q),q).output.map(x=>mod(x*pow(a.length,q-2,q),q));
const api={mod,center,compress,decompress,decode,encode,pow,scalar,polyMulRaw,polyMul,polyTrace,add,sub,dot,moduleData,moduleExample,nttTrace,inverseNTT};
root.LabMath=api;if(typeof module!=='undefined'&&module.exports)module.exports=api;
})(globalThis);
