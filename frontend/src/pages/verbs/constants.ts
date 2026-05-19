import type { VerbPage } from './types';

export const pagesData: VerbPage[] = [
  {
    id: 'page-32',
    pageNumber: 32,
    subtitle: 'Regular Verbs',
    verbs: [
      { base: 'To Work', pastSimple: 'Worked', pastParticiple: 'Worked', spanish: 'Trabajar' },
      { base: 'To Play', pastSimple: 'Played', pastParticiple: 'Played', spanish: 'Jugar' },
    ]
  },
  {
    id: 'page-33',
    pageNumber: 33,
    subtitle: 'Regular Verbs',
    verbs: [
      { base: 'To Study', pastSimple: 'Studied', pastParticiple: 'Studied', spanish: 'Estudiar' },
      { base: 'To Cook', pastSimple: 'Cooked', pastParticiple: 'Cooked', spanish: 'Cocinar' },
    ]
  },
  {
    id: 'page-34',
    pageNumber: 34,
    subtitle: 'Regular Verbs',
    verbs: [
      { base: 'To Talk', pastSimple: 'Talked', pastParticiple: 'Talked', spanish: 'Hablar' },
      { base: 'To Wait', pastSimple: 'Waited', pastParticiple: 'Waited', spanish: 'Esperar' },
    ]
  },
  {
    id: 'page-36',
    pageNumber: 36,
    subtitle: 'Irregular Verbs',
    isIrregular: true,
    verbs: [
      { base: 'To Be', pastSimple: 'Was/Were', pastParticiple: 'Been', spanish: 'Ser/Estar' },
      { base: 'To Have', pastSimple: 'Had', pastParticiple: 'Had', spanish: 'Tener' },
    ]
  },
  {
    id: 'page-37',
    pageNumber: 37,
    subtitle: 'Irregular Verbs',
    isIrregular: true,
    verbs: [
      { base: 'To Go', pastSimple: 'Went', pastParticiple: 'Gone', spanish: 'Ir' },
      { base: 'To Do', pastSimple: 'Did', pastParticiple: 'Done', spanish: 'Hacer' },
    ]
  },
  {
    id: 'page-38',
    pageNumber: 38,
    subtitle: 'Irregular Verbs',
    isIrregular: true,
    verbs: [
      { base: 'To Write', pastSimple: 'Wrote', pastParticiple: 'Written', spanish: 'Escribir' },
      { base: 'To See', pastSimple: 'Saw', pastParticiple: 'Seen', spanish: 'Ver' },
    ]
  },
  {
    id: 'page-39',
    pageNumber: 39,
    subtitle: 'Irregular Verbs',
    isIrregular: true,
    verbs: [
      { base: 'To Eat', pastSimple: 'Ate', pastParticiple: 'Eaten', spanish: 'Comer' },
      { base: 'To Drink', pastSimple: 'Drank', pastParticiple: 'Drunk', spanish: 'Beber' },
    ]
  },
];

export const STUDY_MODES = ['flashcards', 'speaking', 'writing'] as const;