import type { SayingPage } from './types';

export const pagesData: SayingPage[] = [
  {
    id: 'page-45',
    pageNumber: 45,
    subtitle: 'Famous Sayings',
    sayings: [
      { saying: 'A picture is worth a thousand words', meaning: 'Una imagen vale más que mil palabras', example: 'The photo showed the damage - a picture is worth a thousand words.' },
      { saying: 'Actions speak louder than words', meaning: 'Las acciones говорят más que las palabras', example: 'He promised to help but never did - actions speak louder than words.' }
    ]
  },
  {
    id: 'page-46',
    pageNumber: 46,
    subtitle: 'Famous Sayings',
    sayings: [
      { saying: 'Better late than never', meaning: 'Mejor tarde que nunca', example: 'I finally finished the project - better late than never!' },
      { saying: 'Birds of a feather flock together', meaning: 'Dios los cria y ellos se juntan', example: 'They both love gaming - birds of a feather flock together.' }
    ]
  },
  {
    id: 'page-47',
    pageNumber: 47,
    subtitle: 'Famous Sayings',
    sayings: [
      { saying: 'Curiosity killed the cat', meaning: 'La curiosidad mató al gato', example: 'I opened the mysterious email - curiosity killed the cat.' },
      { saying: 'Don\'t count your chickens before they hatch', meaning: 'No cuentes tus pollos antes de que nazcan', example: 'I got the job interview but I won\'t celebrate yet - don\'t count your chickens.' }
    ]
  },
  {
    id: 'page-48',
    pageNumber: 48,
    subtitle: 'Famous Sayings',
    sayings: [
      { saying: 'Every cloud has a silver lining', meaning: 'Todo tiene su lado positivo', example: 'I lost my job but found a better one - every cloud has a silver lining.' },
      { saying: 'Fortune favors the bold', meaning: 'La fortuna favorece a los audaces', example: 'She applied for the CEO position - fortune favors the bold.' }
    ]
  }
];

export const STUDY_MODES = ['flashcards', 'speaking', 'writing'] as const;