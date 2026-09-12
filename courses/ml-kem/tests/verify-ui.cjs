'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const {JSDOM,VirtualConsole}=require('jsdom');
const dir=path.resolve(__dirname,'..'),errors=[];
const vc=new VirtualConsole();vc.on('jsdomError',e=>errors.push(e.message));vc.on('error',(...e)=>errors.push(e.join(' ')));
const dom=new JSDOM(fs.readFileSync(path.join(dir,'index.html'),'utf8'),{url:'https://course.test/',runScripts:'outside-only',pretendToBeVisual:true,virtualConsole:vc});
const w=dom.window,d=w.document;w.scrollTo=()=>{};
for(const name of ['crypto-bundle.js','math.js','real-ntt.js','extra.js','app.js'])w.eval(fs.readFileSync(path.join(dir,name),'utf8'));
const $=id=>d.getElementById(id),fire=(el,type)=>el.dispatchEvent(new w.Event(type,{bubbles:true}));
const nav=id=>{w.history.replaceState({},'',`#${id}`);w.dispatchEvent(new w.HashChangeEvent('hashchange'));assert.ok($('lesson').textContent.trim());};
const click=act=>{const el=d.querySelector(`[data-act="${act}"]`);assert.ok(el,act);el.click();};
const select=(id,value)=>{const el=$(id);assert.ok(el,id);el.value=value;fire(el,'input');fire(el,'change');};
const input=(id,value)=>{const el=$(id);assert.ok(el,id);el.value=String(value);fire(el,'input');};
function finish(){for(let i=0;i<20&&$('nextBtn')&&!$('nextBtn').disabled;i++)click('next');}
const lessons=['start','overview','noise','scalar','polynomial','wrap','module','compression','roots','ntt4','butterfly','ntt','realntt','kem','register','security','reading'];
for(const id of lessons){nav(id);assert.equal(d.querySelector('[aria-current="page"]').getAttribute('href'),'#'+id);if($('nextBtn')){finish();assert.ok($('nextBtn').disabled);click('prev');click('reset');}}
nav('ntt4');for(const v of ['basic','dense','identity','wrap']){select('x-four-preset',v);finish();assert.match($('labOutput').textContent,/与直接循环卷积逐系数相同/);}
input('x-four-a-1',-3);assert.equal($('x-four-preset').value,'custom');nav('start');nav('ntt4');assert.equal($('x-four-a-1').value,'-3');assert.equal($('x-four-preset').value,'custom');
input('x-four-a-1','');assert.equal($('x-four-a-1').getAttribute('aria-invalid'),'true');assert.equal($('inputWarning').hidden,false);select('x-four-preset','basic');assert.equal($('inputWarning').hidden,true);finish();
nav('polynomial');for(const v of ['dense','hand','fold','single']){select('polyPreset',v);finish();assert.match($('labOutput').textContent,/最终结果/);}
nav('roots');for(const v of ['1','16','4','13']){select('x-root',v);finish();assert.match($('labOutput').textContent,v==='1'||v==='16'?/取值点提前重复/:/四个点互不重复/);}
nav('butterfly');input('x-bf-v',3);finish();assert.match($('labOutput').textContent,/输出 \[13,6\]/);
nav('realntt');for(const v of ['small','wrap','dense']){select('x-real-preset',v);input('x-real-block',127);finish();assert.match($('labOutput').textContent,/全部 256 个系数与直接负循环卷积一致/);assert.ok(!$('labOutput').textContent.includes('NaN'));}
nav('register');input('x-reg-old',8);input('x-reg-next',9);finish();assert.match($('labOutput').textContent,/本次写入有 1 位改变/);
nav('security');select('budgetOp','encaps');nav('start');nav('security');assert.equal($('budgetOp').value,'encaps');
nav('scalar');select('scalarPreset','fail');finish();assert.match($('labOutput').textContent,/噪声超过判决裕量/);nav('start');nav('scalar');assert.equal($('scalarPreset').value,'fail');
nav('kem');input('tamperOffset',-1);select('realMode','fixed');assert.equal($('tamperOffset').getAttribute('aria-invalid'),null);assert.equal($('inputWarning').hidden,true);for(const level of ['512','768','1024']){select('realLevel',level);click('real-all');assert.match($('labOutput').textContent,/双方得到完全相同的 32 字节 K/);click('real-tamper');assert.ok(!d.querySelector('.error-message')?.textContent);click('real-restore');}
(async()=>{nav('ntt4');click('reset');select('speed','600');click('play');await new Promise(r=>setTimeout(r,680));click('play');assert.match($('stepCount').textContent,/1 \/ 8/);const before=$('stepCount').textContent;await new Promise(r=>setTimeout(r,680));assert.equal($('stepCount').textContent,before);assert.deepEqual(errors,[]);console.log(JSON.stringify({suite:'DOM interactions (no layout / browser rendering)',chapters:lessons.length,scenarios:['single-step/reset','presets and return navigation','invalid input recovery','real NTT all presets','three real KEM levels','tamper and restore','play and pause'],status:'passed'},null,2));w.close();})().catch(e=>{w.close();console.error(e);process.exitCode=1;});
