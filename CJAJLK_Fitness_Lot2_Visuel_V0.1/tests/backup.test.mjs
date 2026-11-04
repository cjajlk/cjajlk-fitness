import test from 'node:test';
import assert from 'node:assert/strict';
import {encryptBackup,decryptBackup,validateBackup} from '../src/backup.js';
const sample={schemaVersion:1,exportedAt:'2026-11-02',profiles:[{id:'one',name:'CJ',goals:['abdos'],equipment:['haltères']}],health:[{profileId:'one',limitations:['dos']}],settings:[{key:'activeProfile',value:'one'}]};
test('sauvegarde AES-GCM protégée et restaurée fidèlement',async()=>{
 const cipher=await encryptBackup(sample,'mot-de-passe-assez-long');
 assert.doesNotMatch(cipher,/"CJ"|"dos"/);
 assert.deepEqual(await decryptBackup(cipher,'mot-de-passe-assez-long'),sample);
});
test('mot de passe incorrect rejeté',async()=>{
 const cipher=await encryptBackup(sample,'mot-de-passe-assez-long');
 await assert.rejects(decryptBackup(cipher,'mauvais-mot-de-passe'),/Mot de passe incorrect/);
});
test('mot de passe trop court rejeté',async()=>{
 await assert.rejects(encryptBackup(sample,'court'),/8 caractères/);
});
test('format incorrect et profil orphelin refusés',async()=>{
 assert.throws(()=>validateBackup({...sample,health:[{profileId:'missing',limitations:[]}]}),/incohérentes/);
 await assert.rejects(decryptBackup('{}','inconnu'),/non reconnu/);
});
test('les sauvegardes de taille normale dépassant la limite des arguments JS sont supportées',async()=>{
 const big={...sample,profiles:Array.from({length:60},(_,i)=>({id:`profile-${i}`,name:`Personne ${i}`,goals:['reprise'],equipment:[]})),health:[],settings:[],notes:'X'.repeat(140000)};
 const cipher=await encryptBackup(big,'mot-de-passe-assez-long');
 const restored=await decryptBackup(cipher,'mot-de-passe-assez-long');
 assert.equal(restored.notes.length,140000);
});
