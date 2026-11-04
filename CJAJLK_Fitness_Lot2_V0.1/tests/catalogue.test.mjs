import test from 'node:test';
import assert from 'node:assert/strict';
import {EXERCISES,selectExercises} from '../src/exercises.js';
test('30 fiches uniques et complètes, sources HTTPS',()=>{assert.equal(EXERCISES.length,30);assert.equal(new Set(EXERCISES.map(e=>e.id)).size,30);for(const e of EXERCISES){for(const k of ['name','category','zone','equipment','position','setup','movement','caution','easy','variant','dose','source','visualLabel'])assert.ok(e[k],`${e.id}: ${k}`);assert.ok(e.source.startsWith('https://'));}});
test('recherche insensible aux accents et filtres cumulés',()=>{assert.equal(selectExercises({q:'pedalier assis'})[0].id,'ex-29');assert.equal(selectExercises({q:'ÉPAULES'}).length,selectExercises({q:'epaules'}).length);assert.equal(selectExercises({equipment:'rameur',position:'Assis'}).length,1);assert.equal(selectExercises({equipment:'rameur',position:'Debout'}).length,0);assert.equal(selectExercises({q:'inexistant-xyz'}).length,0);});

