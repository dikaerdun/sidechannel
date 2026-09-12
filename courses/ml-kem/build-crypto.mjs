import {build} from 'esbuild';
await build({entryPoints:['src/crypto-entry.mjs'],outfile:'crypto-bundle.js',bundle:true,format:'iife',target:'es2020',platform:'browser',minify:true,legalComments:'inline'});
